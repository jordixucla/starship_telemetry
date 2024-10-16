from PIL import ImageGrab
import pytesseract

from PIL import Image

def get_image_from_png_file(file_path):
    image = Image.open(file_path)
    return image

def extract_region_from_image(image, bbox):
    return image.crop(bbox)

# Capture a screenshot
# screenshot = ImageGrab.grab(bbox=(340, 900, 500, 950))  # Adjust the bbox as needed

# screenshot = ImageGrab.grab(bbox=(340, 900, 500, 950))  # Adjust the bbox as needed

for i in range(4, 4078):
    image_path = f"test/output_{i:04d}.png"
    image = get_image_from_png_file(image_path)

    region_time = extract_region_from_image(image, (865,43,1042,96))
    text_time = pytesseract.image_to_string(region_time,config=r'--psm 10 -c tessedit_char_whitelist="+:0123456789"').strip()

    region_speed = extract_region_from_image(image, (350,10,430,50))
    text_speed = pytesseract.image_to_string(region_speed,config=r'--psm 10 -c tessedit_char_whitelist="0123456789"').strip()
    # region_speed.save(f"tmp/speed_{i}.png")

    region_altitude = extract_region_from_image(image, (350,40,430,80))
    text_altitude = pytesseract.image_to_string(region_altitude,config=r'--psm 10 -c tessedit_char_whitelist="0123456789"').strip()
    # region_altitude.save(f"tmp/altitude_{i}.png")

    region_speed_ss = extract_region_from_image(image, (1515,10,1610,50))
    text_speed_ss = pytesseract.image_to_string(region_speed_ss,config=r'--psm 10 -c tessedit_char_whitelist="0123456789"').strip()

    region_altitude_ss = extract_region_from_image(image, (1515,40,1610,80))
    text_altitude_ss = pytesseract.image_to_string(region_altitude_ss,config=r'--psm 10 -c tessedit_char_whitelist="0123456789"').strip()


    # print(f"data {i}: {text_time}:\t {text_altitude} \t {text_speed} \t {text_altitude_ss} \t {text_speed_ss}")
    with open("telemetry.txt", "a") as file:
        file.write(f"{text_time}\t{text_altitude}\t{text_speed}\t{text_altitude_ss}\t{text_speed_ss}\n")

