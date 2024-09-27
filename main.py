
import directory_utils
import image_utils
import os        
        

# base_path = '/Users/vikasverma/temp/' 
base_path='/Users/vikasverma/Desktop/ss/'

def main():
    max_size = (800, 800)  # Max size (width, height)
    images = directory_utils.list_files_in_directory(base_path)
    image_extensions = ['.jpg','.png','.jpeg']
    os.makedirs(base_path+"thumbnails")
    total = len(images)
    c = 0
    for image in images:
        file_name, file_extension = directory_utils.separate_file_name_and_extension(image) 
        
        print("Total work done: "+ f"{c*100/total:.0f}" + '%')
        
        if  (file_name == '' 
                 or file_extension == '' 
                 or file_extension.lower() not in image_extensions):
            print('invalid file')
            continue
        
        image_utils.reduce_image_size(base_path+file_name + file_extension, 
                          base_path+"thumbnails/"+file_name+'_thumbnail'+file_extension, 
                          max_size)
        c = c + 1 
    print("Total work done: "+ f"{c*100/total:.0f}" + '%')
    print("done!") 
# Example usage

if __name__ == "__main__":
    # directory_utils.unzip_dir(base_path + "temp.zip")
    main()   
    