from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from .models import Feedback
from pathlib import Path
from transformers import AutoTokenizer, pipeline
from optimum.onnxruntime import ORTModelForSeq2SeqLM
import os

ONNX_PATH = Path(os.path.join(os.getcwd(), "bot", "onnx"))
TASK = "summarization"


class Summarizer:
    def __init__(self):
        self.tokenizer = AutoTokenizer.from_pretrained(ONNX_PATH)
        self.model = ORTModelForSeq2SeqLM.from_pretrained(
            ONNX_PATH, file_name="model_optimized_quantized.onnx")
        self.pipeline = pipeline(
            TASK, model=self.model, tokenizer=self.tokenizer)

    def summarize(self, text):
        output = self.pipeline(text + "</s>")
        response = output[0]['summary_text']
        return response


class HealthCheckView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        return Response({'status': 'ok'})


class SummarizerBotView(APIView):
    renderer_classes = [JSONRenderer]
    summarizer = Summarizer()

    def post(self, request):
        """
        POST request handler that receives text data from request and returns a summarized version
        of the text. Expects a 'text' parameter in the request data. Returns a JSON object with the
        summarized text under the 'response' key.

        Args:
            request (Request): The HTTP request object.

        Returns:
            Response: The HTTP response object containing a JSON object with the summarized text.
        """

        text = request.data.get('text')
        response = self.summarizer.summarize(text)
        return Response({'response': response})


class FeedbackView(APIView):
    renderer_classes = [JSONRenderer]

    def post(self, request):
        text = request.data.get('text')
        summary = request.data.get('summary', '')
        feedback = Feedback(text=text, summary=summary)
        feedback.save()

        response = summary + "\n\nThank you for your contributing!"
        return Response({'response': response})
    