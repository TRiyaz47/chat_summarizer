#pip install transformers[sentencepiece] datasets sacrebleu rouge_score py7zr accelerate -q

from transformers import pipeline, set_seed

import matplotlib.pyplot as plt
from datasets import load_dataset
import pandas as pd
from datasets import load_dataset, load_metric

from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

import nltk
from nltk.tokenize import sent_tokenize

from tqdm import tqdm
import torch

nltk.download("punkt")

dataset_samsum = load_dataset("samsum")

tokenizer = AutoTokenizer.from_pretrained("tokenizer")

sample_text = dataset_samsum["test"][0]["dialogue"]
reference = dataset_samsum["test"][0]["summary"]

gen_kwargs = {"length_penalty": 0.8, "num_beams":8, "max_length": 128}
pipe = pipeline("summarization", model="pegasus-samsum-model",tokenizer=tokenizer)

print("Dialogue:")
print(sample_text)

print("\nReference Summary:")
print(reference)

print("\nModel Summary:")
print(pipe(sample_text, **gen_kwargs)[0]["summary_text"])
