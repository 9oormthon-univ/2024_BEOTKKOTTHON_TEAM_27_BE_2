from PIL import Image, ImageFont, ImageDraw
import matplotlib.pyplot as plt


def put_text_on_image(image: Image, text1: str, text2: str, font_type: str, font_color: str):
    draw = ImageDraw.Draw(image)
    image_width, image_height = image.size

    x_position = 20
    y_position = image_height - 150 - 10

    # 1
    font = ImageFont.truetype(font_type, 80, encoding="UTF-8")
    draw.text((x_position, y_position), text1, font=font, fill=font_color, stroke_width=2, stroke_fill=(0, 0, 0))

    # 2
    font = ImageFont.truetype(font_type, 30, encoding="UTF-8")
    draw.text((x_position, y_position + 85), text2, font=font, fill=font_color, stroke_width=1, stroke_fill=(0, 0, 0))

    return image

if __name__ == "__main__":
    new_image = put_text_on_image(Image.open("IMG_6657.jpg"), "꿔바로우", "숙대 핫플레이스, 꿔바로우로 새로워진 속명여대점!", "../font/HakgyoansimJiugaeR.ttf", "white")
    plt.imshow(new_image)
    plt.axis('off')
    plt.show()