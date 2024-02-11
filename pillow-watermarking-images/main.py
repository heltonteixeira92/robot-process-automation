"""
Add a watermark overlay to an image
"""

from PIL import Image, ImageDraw, ImageFont
import os


def add_watermark_overlay(input_image_path, output_image_path, watermark_text):
    input_image = Image.open(input_image_path)
    # Convert the input image to RGBA mode (red, green, blue, alpha)
    input_image = input_image.convert('RGBA')

    # Get the width and height of the input image
    width, height = input_image.size

    # Create a new transparent overlay image with the same size as the input image
    overlay = Image.new('RGBA', input_image.size, (255, 255, 255, 0))

    # Create a drawing object to draw on the overlay image
    draw = ImageDraw.Draw(overlay)

    # Define the color and pattern for the watermark overlay lines
    watermark_color_pattern = (255, 255, 255, 30)

    # Draw diagonal lines on the overlay image with a pattern to create a watermark effect
    for i in range(0, width + height, 50):
        draw.line([(0, height - i), (i, height)], fill=watermark_color_pattern, width=5)

    font_size = 80

    # Load the Arial font with the specified font size
    font = ImageFont.truetype('arial.ttf', font_size)

    # Get the width and height of the watermark text
    _, _, text_width, text_height = draw.textbbox((0, 0), watermark_text, font)

    # Calculate the position to place the watermark text at the center
    x = (width - text_width) // 2
    y = (height - text_height) // 2

    watermark_color_text = (255, 255, 255, 80)

    # Draw the watermark text on the overlay image
    draw.text((x, y), watermark_text, fill=watermark_color_text, font=font)

    # Composite the input image and the overlay image to create the watermarked image
    watermarked_image = Image.alpha_composite(input_image, overlay)

    watermarked_image.save(output_image_path)


for file in os.listdir('images'):
    add_watermark_overlay(f'images/{file}', f'images/watermarked_{file.replace("jpg", "png")}', 'Hello World')
