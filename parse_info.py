from PIL import Image
import pytesseract

def extract_text_from_image(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    print(text)
    return text

if __name__ == "__main__":
    extract_text_from_image("test/output_0015.png")
    
