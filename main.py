from PIL import Image
from captcha.image import ImageCaptcha
from io import BytesIO

def main() -> None:
    text: str = 'HELLO'
    
    captcha: ImageCaptcha = ImageCaptcha(width=400,
                                         height=220,
                                         font_sizes=(40, 70, 100)) # type: ignore
    
    captcha.write(text, 'captcha.png')
    
    data: BytesIO = captcha.generate(text)
    image: Image.Image = Image.open(data)
    image.show('Sample captcha')
    
if __name__ == '__main__':
    main()
