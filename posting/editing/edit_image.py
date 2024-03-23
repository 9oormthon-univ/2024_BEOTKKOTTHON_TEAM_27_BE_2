from PIL import Image, ImageFont, ImageDraw
import matplotlib.pyplot as plt

from editing.image_size import resize_image
from editing.add_logo import add_logo_to_image


class custom_stroke:
    def __init__(self, min_size: int, max_size: int):
        self.min_size = min_size
        self.max_size = max_size
        self.size = max_size


class custom_font:
    def __init__(self, min_size: int, max_size: int, stroke: custom_stroke, font_type: str):
        self.min_size = min_size
        self.max_size = max_size
        self.size = max_size
        self.stroke = stroke
        self.font = ImageFont.truetype(font_type, size=max_size, encoding="UTF-8")


def put_text_on_image(image: Image, text1: str, text2: str, font_type: str, font_color: str, logo_file: str, logo_size: tuple):
    image = resize_image(image, (1000, 1000))
    image = add_logo_to_image(image, Image.open(logo_file), logo_size)

    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size

    # font 초기화
    font1 = custom_font(100, 190, custom_stroke(5, 18), font_type)
    font2 = custom_font(30, 60, custom_stroke(5, 8), font_type)

    font1.font = ImageFont.truetype(font_type, size=font1.max_size, encoding="UTF-8")
    font2.font = ImageFont.truetype(font_type, size=font2.max_size, encoding="UTF-8")

    # text 크기 구하기
    text1_width, text1_height = get_text_dimensions(text1, font=font1.font)
    text2_width, text2_height = get_text_dimensions(text2, font=font2.font)

    # font 크기 재적용
    font1 = adjust_font_size(font1, text1, text1_width, image_width, font_type)
    font2 = adjust_font_size(font2, text2, text2_width, image_width, font_type)

    # text 크기 다시 구하기 (font 사이즈가 달라졌으니까)
    text1_width, text1_height = get_text_dimensions(text1, font1.font)
    text2_width, text2_height = get_text_dimensions(text2, font2.font)

    # 폰트 위치 구하기
    x_position1 = (image_width - text1_width) // 2
    y_position1 = image_height - text1_height - 10
    x_position2 = (image_width - text2_width) // 2
    y_position2 = y_position1 - text2_height - 30

    # 폰트 그리기
    draw.text((x_position1, y_position1), text1, font=font1.font, fill=font_color, stroke_width=font1.stroke.size, stroke_fill=(0, 0, 0))
    draw.text((x_position2, y_position2), text2, font=font2.font, fill=font_color, stroke_width=font2.stroke.size, stroke_fill=(0, 0, 0))

    return image


def get_text_dimensions(text_string, font):
    ascent, descent = font.getmetrics()

    text_width = font.getmask(text_string).getbbox()[2]
    text_height = font.getmask(text_string).getbbox()[3] + descent

    return text_width, text_height


def adjust_font_size(custom_font: custom_font, text: str, text_width: int, image_width: int, font_type: str):
    while True:
        if text_width > image_width - 70 and custom_font.min_size < custom_font.size <= custom_font.max_size:
            custom_font.size = custom_font.size - 10
            custom_font.font = ImageFont.truetype(font_type, size=custom_font.size, encoding="UTF-8")
            text_width, _ = get_text_dimensions(text, custom_font.font)

            if custom_font.stroke.size > custom_font.stroke.min_size:
                custom_font.stroke.size = custom_font.stroke.size - 1
        else:
            break

    return custom_font


if __name__ == "__main__":
    new_image = put_text_on_image(Image.open("image/mara.jpeg"), "가나다라마바사아자", "#마라킹 #용산구핫플 #가나다라마바사아자차", "../font/SDSamliphopangcheTTFOutline.ttf", "white", "logo/logo4.png", (130, 90))
    new_image.save("output_image.jpg")
    plt.imshow(new_image)
    plt.axis('off')
    plt.show()
