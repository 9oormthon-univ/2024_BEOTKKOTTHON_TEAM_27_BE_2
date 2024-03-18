from PIL import Image, ImageFont, ImageDraw
import matplotlib.pyplot as plt


def put_text_on_image(image: Image, text: str, font_type: str, font_size: int, font_color: str):
    font = ImageFont.truetype("font/" + font_type, font_size, encoding="UTF-8")
    draw = ImageDraw.Draw(image)
    w, h = image.size
    draw.text((10, 10), text, font=font, fill=font_color)
    return image

if __name__ == "__main__":
    new_image = put_text_on_image(Image.open("../image/test_image.jpeg"), "안녕하세요", "../font/MaruBuri-Bold.ttf", 150, "black")
    plt.imshow(new_image)
    plt.axis('off')
    plt.show()