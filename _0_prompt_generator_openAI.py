import os
import re
import openai
from stability_sdk import client
from utils_colors import Colors

class PromptGeneratorOpenAI:
    def __init__(self, path, prompt):
        self.path = path
        self.dir = "prompts/"
        self.output_prompt = ""
        self.model = "text-davinci-003"
        self.prompt = prompt
        self.temperature = 1
        self.max_tokens = 100
        self.stability_key = ""

    def init_keys(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        
    def generatePrompt(self):
        response = openai.Completion.create(model=self.model, prompt=self.prompt, temperature=self.temperature, max_tokens=self.max_tokens)
        self.output_prompt = response.choices[0]['text'].replace('\"','') + " Digital art" + '\n'
        self.output_prompt = self.output_prompt.lstrip()
        
    def appendPromptToFile(self):
        with open(self.path,'ab') as f:
            f.write(self.output_prompt.encode('utf-8'))

    def clean_path(self):
        self.path = re.sub(r'\W+', '', self.path) # remove non-alphanumeric characters to avoid injection
        self.path = self.dir + self.path
        if not os.path.exists(self.dir):
            os.makedirs(self.dir)

    def launch(self):
        try:
            self.init_keys()
            self.clean_path()
            self.generatePrompt()
            self.appendPromptToFile()
        except Exception as e:    
            print(f"{Colors.ERROR}Error: {Colors.B_WHITE}prompt generation {Colors.RED}{e}{Colors.END}")
            exit(1)
