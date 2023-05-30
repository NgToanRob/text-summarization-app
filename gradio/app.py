import gradio as gr
import requests
import os
from dotenv import load_dotenv


load_dotenv()

def summarize_text(text):
    url = '{}/summarizer/'.format(os.getenv('API_ADDRESS'))
    data = {'text': text}
    response = requests.post(url, json=data)
    summary = response.json()['response']
    return summary

def feedback(text, summary):
    url = '{}/feedback/'.format(os.getenv('API_ADDRESS'))
    data = {'text': text, 'summary': summary}
    response = requests.post(url, json=data)
    response_text = response.json()['response']
    return response_text

with gr.Blocks() as demo:
    with gr.Column():
        title = gr.Markdown('# Text Summarization')
        description = gr.Markdown('Enter a long piece of text and get a summary of it in just a few sentences.')

        with gr.Row():
            # Input text
            with gr.Column():
                input_text = gr.Textbox(label='Your text',lines=3)
                submit_btn = gr.Button('Submit')
            
            # Output text
            with gr.Column():
                output_text = gr.Textbox(label='Summarized text', lines=3)
                contribute_btn = gr.Button('Contribute 🤗')
            

    # handle events          
    submit_btn.click(fn=summarize_text, inputs=input_text, outputs=output_text, api_name='summarize_text')
    contribute_btn.click(fn=feedback, inputs=[input_text, output_text], outputs=output_text, api_name='feedback')
            
demo.launch(server_name=os.getenv('SERVER_NAME'), server_port=int(os.getenv('SERVER_PORT')))