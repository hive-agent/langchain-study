import os

from dotenv import load_dotenv

from langchain_community.llms import Replicate

load_dotenv()

text2image = Replicate(model="stability-ai/stable-diffusion-3.5-large",
                       model_kwargs={"prompt_strength": 0.82, "cfg": 4.5, "steps": 40, "aspect_ratio": "1:1",
                                     "output_format": "webp", "output_quality": 100, "seed": 42})

result = text2image.invoke("A beautiful sunset over a calm ocean")

print(result)

