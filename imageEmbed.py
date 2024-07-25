from PIL import Image

def add_black_pixels_to_top(image_path, output_path):
    #Open original image
    original = Image.open(image_path)
    width, height = original.size

    #Create new image with new pixels
    new_image = Image.new("RGB", (width, height), "red")

    # Paste original onto the new image
    new_image.paste(original, (10, 4))

    #Save new image
    new_image.save(output_path)
    print(f"Image saved to {output_path}")

#Usage 
add_black_pixels_to_top("input.jpg", "output.jpg")
