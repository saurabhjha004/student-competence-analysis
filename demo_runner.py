from src.python_code_analyzer import PythonCodeAnalyzer
from transformers import AutoTokenizer, AutoModel
import torch

# Load CodeBERT
tokenizer = AutoTokenizer.from_pretrained("microsoft/codebert-base")
model = AutoModel.from_pretrained("microsoft/codebert-base")

# Example student code with a bug
student_code = """
def add_numbers(a, b):
    return a - b   # subtraction instead of addition
print(add_numbers(3, 2))
"""

# --- AST Analysis ---
analyzer = PythonCodeAnalyzer()
parsed = analyzer.parse_code(student_code)
if parsed["success"]:
    features = analyzer.extract_features(parsed["tree"])
    print("AST Features:", features)
else:
    print("Syntax Error:", parsed["error"])

# --- Embeddings with CodeBERT ---
inputs = tokenizer(student_code, return_tensors="pt", truncation=True, max_length=256)
with torch.no_grad():
    outputs = model(**inputs)
embedding = outputs.last_hidden_state.mean(dim=1)
print("Code Embedding Shape:", embedding.shape)

# --- Educational Prompt ---
if "-" in student_code:
    print("Educational Prompt: Your function is called 'add_numbers' but contains subtraction. Why might that be?")