from PIL import Image


def crop(path):
    '''Crop an image into a square'''

    image = Image.open(path)
    width, height = image.size # current size

    if width > height:
        left = (width - height) / 2
        right = left + height
        image = image.crop((left, 0, right, height))   # (left, top, right, bottom)
    elif width < height:
        top = (height - width) / 2 
        bottom = top + width
        image = image.crop((0, top, width, bottom))
    return image.save(path)
