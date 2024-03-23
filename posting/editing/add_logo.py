def add_logo_to_image(image, logo, logo_size=(100, 100)):
    logo = logo.resize(logo_size)
    image.paste(logo, (image.width - logo.width - 10, 10), logo)
    return image


if __name__ == "__main__":
    image_path = "image/output_image.jpg"  # 이미지 파일 경로
    logo_path = "logo/logo4.png"  # 로고 파일 경로
    output_path = "output_image_with_logo5.jpg"  # 결과 이미지 파일 경로

    add_logo_to_image(image_path, logo_path, output_path)
