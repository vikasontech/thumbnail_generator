from PIL import Image

def reduce_image_size(input_image_path, output_image_path, max_size):
    # Open the original image
    with Image.open(input_image_path) as img:
        # Print original size
        # print(f"Original size: {img.size}")

        # Calculate the ratio to resize
        img.thumbnail(max_size)
        
        # Print new size
        # print(f"Reduced size: {img.size}")

        # Save the resized image
        img.save(output_image_path)
        # print(f"Image saved as: {output_image_path}")