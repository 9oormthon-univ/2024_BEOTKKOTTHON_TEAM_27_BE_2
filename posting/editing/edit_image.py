from PIL import Image, ImageFont, ImageDraw
import matplotlib.pyplot as plt

from editing.image_size import resize_image
from editing.add_logo import add_logo_to_image


def put_text_on_image(image: Image, text1: str, text2: str, font_type: str, font_color: str, logo_file: str, logo_size: tuple):
    image = resize_image(image, (1000, 1000))
    image = add_logo_to_image(image, Image.open(logo_file), logo_size)

    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size

    font1 = ImageFont.truetype(font_type, size=200, encoding="UTF-8")

    font2_max_size = 70
    font2 = ImageFont.truetype(font_type, size=font2_max_size, encoding="UTF-8")

    text1_width, text1_height = get_text_dimensions(text1, font=font1)
    text2_width, text2_height = get_text_dimensions(text2, font=font2)

    while True:
        if text2_width > image_width - 30 and font2_max_size > 30 and font2_max_size <= 60:
            font2_max_size = font2_max_size - 10
            font2 = ImageFont.truetype(font_type, font2_max_size, encoding="UTF-8")
            text2_width, _ = get_text_dimensions(text2, font2)
        else:
            break

    text2_width, text2_height = get_text_dimensions(text2, font=font2)

    font1_max_size = 200
    font1 = ImageFont.truetype(font_type, size=font1_max_size, encoding="UTF-8")

    while True:
        if text1_width > image_width - 100 and font1_max_size > 30 and font2_max_size <= 200:
            font1_max_size = font1_max_size - 20
            font1 = ImageFont.truetype(font_type, size=font1_max_size, encoding="UTF-8")
            text1_width, _ = get_text_dimensions(text1, font1)
        else:
            break

    text1_width, text1_height = get_text_dimensions(text1, font=font1)

    x_position1 = (image_width - text1_width) // 2
    y_position1 = image_height - text1_height - 10
    x_position2 = (image_width - text2_width) // 2
    y_position2 = y_position1 - text2_height - 30

    draw.text((x_position1, y_position1), text1, font=font1, fill=font_color, stroke_width=20, stroke_fill=(0, 0, 0))
    draw.text((x_position2, y_position2), text2, font=font2, fill=font_color, stroke_width=8, stroke_fill=(0, 0, 0))

    return image


def get_text_dimensions(text_string, font):
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return text_width, text_height


if __name__ == "__main__":
    new_image = put_text_on_image(Image.open("image/resized_tteokbokki.jpg"), "볶이", "#용산구핫플 # #B", "../font/SDSamliphopangcheTTFOutline.ttf", "white", "logo/logo4.png", (130, 90))
    new_image.save("output_image.jpg")
    plt.imshow(new_image)
    plt.axis('off')
    plt.show()

