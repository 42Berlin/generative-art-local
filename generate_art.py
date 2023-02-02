import os
import re
import sys
import openai
from _0_prompt_generator_openAI import PromptGeneratorOpenAI
from _1_image_generator import ImageGenerator
from utils_colors import Colors
from utils_config import IMAGES_DIR, PROMPTS_DIR, URL, INPUT_PROMPT

def get_arguments():
    if (len(sys.argv) < 3):
        print(f"{Colors.ERROR}Error: {Colors.B_WHITE}usage: {Colors.ORANGE}python3 generate_art.py <prompts_output_file> <images_output_folder>{Colors.END}")
        exit(1)
    prompts_output_file = re.sub(r'\W+', '', str(sys.argv[1])[0:30])
    images_output_folder = re.sub(r'\W+', '', str(sys.argv[2])[0:30])
    return prompts_output_file, images_output_folder

def get_one_prompt(prompts_output_file):
    with open(PROMPTS_DIR + prompts_output_file, 'r') as f:
        last_line = f.read().splitlines()[-1]
        prompt = last_line[0:200]
        return prompt
    
def main():
    try:
        prompts_output_file, images_output_folder = get_arguments()
        promptGen = PromptGeneratorOpenAI(prompts_output_file, INPUT_PROMPT)
        promptGen.launch()
        prompt = get_one_prompt(prompts_output_file)
        imageGen = ImageGenerator(prompt, images_output_folder)
        imageGen.launch()
    except Exception as e:    
        print(f"{Colors.ERROR}Error: {Colors.B_WHITE}generate_art {Colors.RED}{e}{Colors.END}")
        exit(1)

if __name__ == '__main__':
    main()