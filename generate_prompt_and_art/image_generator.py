import re
import os
import io
import sys
import json
import uuid
import base64
import requests
from utils_colors import Colors
from utils_config import IMAGES_DIR, PROMPTS_DIR, URL
from PIL import Image, PngImagePlugin

class ImageGenerator:
    def __init__(self, prompt, output_folder="default", steps=5, width=1024, height=512):
        self.url = URL
        self.output_folder = output_folder[0:30]
        self.payload = ""
        self.prompt = prompt
        self.steps = steps
        self.width = width
        self.height = height
        self.response = {}
        
    def print_payload(self):
        for key, value in self.payload.items():
            print(f'{key}: {value}')

    def check_url(self):
        try:
            resp_header = requests.head(self.url, timeout=3)
            return resp_header.status_code == 200
        except requests.ConnectionError:
            print("Connection error. Please check that the server is on.")
            exit(1) 

    def fill_payload(self):
        self.payload = {
            "prompt": self.prompt,
            "steps": self.steps,
            "width": self.width,
            "height": self.height,
        }

    def call_api(self):
        response = requests.post(url=f'{self.url}/sdapi/v1/txt2img', json=self.payload)
        response.raise_for_status()
        self.response = response.json()

    def check_output_folder(self):
        self.output_folder = re.sub(r'\W+', '', self.output_folder)
        self.output_folder = IMAGES_DIR + self.output_folder
        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    def create_save_image(self):
        for i in self.response['images']:
            image = Image.open(io.BytesIO(base64.b64decode(i.split(",",1)[0])))
            png_payload = { "image": "data:image/png;base64," + i }
            response2 = requests.post(url=f'{self.url}/sdapi/v1/png-info', json=png_payload)
            pnginfo = PngImagePlugin.PngInfo()
            pnginfo.add_text("parameters", response2.json().get("info"))
            name = self.output_folder + "/" + self.payload["prompt"].replace(" ", "_") + "_" + str(uuid.uuid4())[:8] + ".png"
            image.save(name, pnginfo=pnginfo)
           
    def launch(self):
        try:
            self.check_url()
            self.fill_payload()
            self.call_api()
            self.check_output_folder()
            self.create_save_image()
        except Exception as e:    
            print(f"{Colors.ERROR}Error: {Colors.B_WHITE}image generation {Colors.RED}{e}{Colors.END}")
            exit(1)