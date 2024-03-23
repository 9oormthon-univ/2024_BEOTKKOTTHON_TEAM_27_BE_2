from PIL import Image, ImageFont, ImageDraw
import matplotlib.pyplot as plt

# from editing.image_size import resize_image
# from editing.add_logo import add_logo_to_image
from image_size import resize_image
from add_logo import add_logo_to_image


def put_text_on_image(image: Image, text1: str, text2: str, font_type: str, font_color: str, logo_file: str, logo_size: tuple):
    image = resize_image(image, (1000, 1000))
    image = add_logo_to_image(image, Image.open(logo_file), logo_size)

    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size

    # font 초기화
    font1_max_size = 200
    stroke1_max_size = 20
    font1 = ImageFont.truetype(font_type, size=font1_max_size, encoding="UTF-8")

    font2_max_size = 70
    stroke2_max_size = 8
    font2 = ImageFont.truetype(font_type, size=font2_max_size, encoding="UTF-8")

    # text 크기 구하기
    text1_width, text1_height = get_text_dimensions(text1, font=font1)
    text2_width, text2_height = get_text_dimensions(text2, font=font2)

    # font 크기 재적용
    font1_max_size, font1, stroke1_max_size = adjust_font_size(text1_width, image_width, font1_max_size, 30, font_type, stroke1_max_size, text1)
    font2_max_size, font2, stroke2_max_size = adjust_font_size(text2_width, image_width, font2_max_size, 30, font_type, stroke2_max_size, text2)

    # text 크기 다시 구하기 (font 사이즈가 달라졌으니까)
    text1_width, text1_height = get_text_dimensions(text1, font=font1)
    text2_width, text2_height = get_text_dimensions(text2, font=font2)

    # 폰트 위치 구하기
    x_position1 = (image_width - text1_width) // 2
    y_position1 = image_height - text1_height - 10
    x_position2 = (image_width - text2_width) // 2
    y_position2 = y_position1 - text2_height - 30

    # 폰트 그리기
    draw.text((x_position1, y_position1), text1, font=font1, fill=font_color, stroke_width=stroke1_max_size, stroke_fill=(0, 0, 0))
    draw.text((x_position2, y_position2), text2, font=font2, fill=font_color, stroke_width=stroke2_max_size, stroke_fill=(0, 0, 0))

    return image


def adjust_font_size(text_width, image_width, max_size, min_size, font_type, stroke_width, text, encoding="UTF-8"):
    font = ImageFont.truetype(font_type, size=max_size, encoding=encoding)
    while text_width > image_width - min_size and max_size > min_size:
        max_size -= 20 if max_size > 30 else 10
        font = ImageFont.truetype(font_type, size=max_size, encoding=encoding)
        text_width, _ = get_text_dimensions(text, font)

        if stroke_width >= 5:
            stroke_width = stroke_width - 1

    return max_size, font, stroke_width


def get_text_dimensions(text_string, font):
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return text_width, text_height


if __name__ == "__main__":
    new_image = put_text_on_image(Image.open("image/resized_tteokbokki.jpg"), "마라 항정살", "#용산구핫플 # #B", "../font/SDSamliphopangcheTTFOutline.ttf", "white", "logo/logo4.png", (130, 90))
    new_image.save("output_image.jpg")
    plt.imshow(new_image)
    plt.axis('off')
    plt.show()
