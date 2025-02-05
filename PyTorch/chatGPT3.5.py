import os
import requests
import json
import openai

openai.api_key = "b1e2f5d6a96c49d4be3e56d9fee925e9" # your API key here
openai.api_base = "https://openaitest1307.openai.azure.com/" # your endpoint should look like the following https://YOUR_RESOURCE_NAME.openai.azure.com/
openai.api_type = 'azure'
openai.api_version = '2023-05-15' # this may change in the future

deployment_name='gpt35turbo' #This will correspond to the custom name you chose for your deployment when you deployed a model. 

# Send a completion call to generate an answer
print('Sending a test completion job')
start_phrase = 'Write a tagline for an ice cream shop. '
response = openai.Completion.create(engine=deployment_name, prompt=start_phrase, max_tokens=250)
text = response['choices'][0]['text'].replace('\n', '').replace(' .', '.').strip()
print(start_phrase+text)