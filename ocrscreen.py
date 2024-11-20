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
ift_mission=6
save_data=True
for i in range(20, 3962):
    # image_path = f"in_ift3/img{i:03d}.jpg"
    image_path = f"in_ift{ift_mission}/output_{i:04d}.png"
    image = get_image_from_png_file(image_path)

    region_time = extract_region_from_image(image, (880,46,1050,93))
    text_time = pytesseract.image_to_string(region_time,config=r'--psm 10 -c tessedit_char_whitelist="+:0123456789"').strip()
    if (save_data):
        region_time.save(f"tmp/{i}_time.png")

    region_speed = extract_region_from_image(image, (342,10,430,50))
    text_speed = pytesseract.image_to_string(region_speed,config=r'--psm 10 -c tessedit_char_whitelist="0123456789"').strip()
    if (save_data):
        region_speed.save(f"tmp/{i}_speed.png")

    region_altitude = extract_region_from_image(image, (342,45,430,80))
    text_altitude = pytesseract.image_to_string(region_altitude,config=r'--psm 10 -c tessedit_char_whitelist="0123456789"').strip()
    if (save_data):
        region_altitude.save(f"tmp/{i}_altitude.png")

    region_speed_ss = extract_region_from_image(image, (1515,10,1605,50))
    text_speed_ss = pytesseract.image_to_string(region_speed_ss,config=r'--psm 10 -c tessedit_char_whitelist="0123456789"').strip()
    if (save_data):
        region_speed_ss.save(f"tmp/{i}_speed_ss.png")

    region_altitude_ss = extract_region_from_image(image, (1515,45,1605,80))
    text_altitude_ss = pytesseract.image_to_string(region_altitude_ss,config=r'--psm 10 -c tessedit_char_whitelist="0123456789"').strip()
    if (save_data):
        region_altitude_ss.save(f"tmp/{i}_altitude_ss.png")

    print(f"data {i}: {text_time}:\t {text_altitude} \t {text_speed} \t {text_altitude_ss} \t {text_speed_ss}")

    with open(f"telemetry_ift{ift_mission}.txt", "a") as file:
        file.write(f"{i}\t{text_time}\t{text_altitude}\t{text_speed}\t{text_altitude_ss}\t{text_speed_ss}\n")

    with open("sx/data.txt", "a") as file:
        file.write(f"{i}\t{text_time}\t{text_altitude}\t{text_speed}\t{text_altitude_ss}\t{text_speed_ss}\n")

