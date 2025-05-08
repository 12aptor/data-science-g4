from PIL import Image, ImageFont, ImageDraw

def main():
    image = Image.open("matrix.jpg")
    print(image.size)
    print(image.format)
    print(image.mode)

    width = image.size[0]
    height = image.size[1]
    print('Ancho de la imagen:', width)
    print('Alto de la imagen:', height)

    new_width = width // 2
    new_height = height // 2

    new_size = (new_width, new_height)

    new_image = image.resize(new_size)
    print(new_image.size)

    draw = ImageDraw.Draw(new_image)
    draw.text(
        (10, 10), # Posición del texto
        "Hola Python", # Texto
        (255, 255, 255), # Color del texto (RGB)
    )
    new_image.save('matrix_resized.jpg', 'JPEG', quality=90)
    new_image.show()

if __name__ == "__main__":
    main()