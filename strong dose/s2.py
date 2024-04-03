import numpy as np
from PIL import Image

# path of the image to work with
image_path = "1.jpg"


# opening the image, converting it into RGB image to ensure consistency
# converting image into a NumPy array
def get_image(img_path):
    """Get a numpy array of an image."""
    image = Image.open(img_path, "r")
    image.convert("RGB")
    return np.array(image)


# to calculate the brightness of a pixel, takes rgb tuple as input
def calculate_brightness(pixel):
    """Calculate brightness of a pixel."""
    return 0.21 * pixel[0] + 0.72 * pixel[1] + 0.07 * pixel[2]


# calculates typeA, typeB percentage
# then calculates brightness of each pixel and converts it into a black and white image based on threshold
def process_image(image_arr, threshold=(160, 160, 160), brightness_level=127):
    """Process the image."""
    typea_count = 0
    total_pixels = image_arr.shape[0] * image_arr.shape[1]
    for row in image_arr:
        for pixel in row:
            if all(value > threshold[i] for i, value in enumerate(pixel)):
                typea_count += 1

    typeb_count = total_pixels - typea_count
    typea_percentage = (typea_count / total_pixels) * 100
    typeb_percentage = (typeb_count / total_pixels) * 100

    print(f"Percentage of typeA pixels: {typea_percentage:.2f}%")
    print(f"Percentage of typeB pixels: {typeb_percentage:.2f}%")

    black_white_image = np.zeros_like(image_arr)
    for i in range(image_arr.shape[0]):
        for j in range(image_arr.shape[1]):
            brightness = calculate_brightness(image_arr[i, j])
            if brightness > brightness_level:
                black_white_image[i, j] = [255, 255, 255]  # White
            else:
                black_white_image[i, j] = [0, 0, 0]  # Black

    return black_white_image


# Load the image
image_array = get_image(image_path)

# Process the image
black_white = process_image(image_array)


# Display the black and white image
# converts the image array into a PIL image object and shows it using the show() func
black_white_img = Image.fromarray(black_white.astype(np.uint8))
black_white_img.show()
