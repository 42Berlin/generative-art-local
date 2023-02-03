# generative-art-local
Scripts that generate images through stable-diffusion API running locally on 42 Berlin supercomputer

## Stable Diffusion

Stable Diffusion is an open source deep learning model that generates visuals.
In 42 Berlin, we are running the [Automatic1111](https://github.com/AUTOMATIC1111/stable-diffusion-webui#readme) version on a supercomputer and make it available **from clusters computers**.
It provides many features, have a look at the [API documentation](http://10.11.250.225:7860/docs)

## Example

This example generates prompts that generate images.
To run it, create a virtual environment first and install requirements.

`python3 -m venv venv && . venv/bin/activate`  
`pip3 install --upgrade pip`  
`pip3 install -r requirements.txt`  
`python3 generate_art.py <prompts_output_file> <images_output_folder>`  

This simply generates a prompt in the <prompts_output_file>, from an initial one defined in `utils_config.py`, which is used to generate images in the <images_output_folder>

How does it work? It uses the [API](http://10.11.250.225:7860/docs) `/sdapi/v1/txt2img` POST request.

## What's next

As you can see, there are many parameters that can be set, and may other requests that can be used. You are more than welcome to contribute to this repository, you can make a pull request or contact us directly if you want to add your own scripts.  
**Have fun**, play around, and generate art!  
Then we will run the new programs all-day long to display your creations on the lobby screen :rainbow: