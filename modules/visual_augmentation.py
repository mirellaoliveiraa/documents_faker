from PIL import ImageFilter, ImageEnhance
import random

def apply_visual_augmentation(image):
    image = image.filter(ImageFilter.GaussianBlur(radius=random.uniform(0, 1.5)))

    contraste = ImageEnhance.Contrast(image)
    image = contraste.enhance(random.uniform(0.8, 1.2))

    brilho = ImageEnhance.Brightness(image)
    image = brilho.enhance(random.uniform(0.9, 1.1))

    nitidez = ImageEnhance.Sharpness(image)
    image = nitidez.enhance(random.uniform(0.8, 1.3))

    image = image.rotate(random.uniform(-2, 2), expand=1, fillcolor=(255, 255, 255))

    return image
