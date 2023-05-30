from django.test import TestCase

# Create your tests here.
from pathlib import Path
from transformers import AutoTokenizer, pipeline
from optimum.onnxruntime import ORTModelForSeq2SeqLM
import os

onnx_path = Path("/onnx")
task = "summarization"

print(os.getcwd())


tokenizer = AutoTokenizer.from_pretrained(onnx_path)
model = ORTModelForSeq2SeqLM.from_pretrained(onnx_path, file_name="model_optimized_quantized.onnx")