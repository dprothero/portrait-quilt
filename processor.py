from PIL import Image, ImageOps


def process_image(image, colors):
    image = ImageOps.autocontrast(image)
    image = image.convert('L')  # black & white

    bits = 2 if colors == 4 else 3
    image = ImageOps.posterize(image, bits)
    if colors > 4 and colors < 8:
        image = image.quantize(colors, 1)

    return image


if __name__ == '__main__':
    image = process_image(Image.open("C:\\Users\\david\\Downloads\\portrait500.jpg"), 8)
    image.save("C:\\Users\\david\\Downloads\\_portrait500.png")
