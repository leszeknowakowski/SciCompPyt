from PIL import Image
import requests
from io import BytesIO

#import an image from url, from https://stackoverflow.com/questions/7391945/how-do-i-read-image-data-from-a-url-in-python
image_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/4/47/Panorama_Dolina_Litworowa_a2.JPG/1920px-Panorama_Dolina_Litworowa_a2.JPG"
response = requests.get(image_url)

with Image.open(BytesIO(response.content)) as image:
    print("Mode:", image.mode) #mode: RGB
    print("Size:", image.size) #Size: (1920, 692)
    print("Format:", image.format) #Format: JPEG
    image.thumbnail((128,128))
    image.save("thumbanil.png", "PNG")