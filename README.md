# Python Student Competence Analysis: AI-Powered Educational Assessment

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![CodeBERT](https://img.shields.io/badge/Model-CodeBERT-green.svg)](https://github.com/microsoft/CodeBERT)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![FOSSEE](https://img.shields.io/badge/Project-FOSSEE%20Internship-orange.svg)]()

> **🎯 An innovative AI system that combines CodeBERT with Abstract Syntax Tree analysis to assess Python student competence and generate meaningful educational prompts for deeper learning.**

## 📋 Project Overview

This project addresses **Python Screening Task 3** by developing an intelligent educational assessment system that revolutionizes how we evaluate student programming competence. By combining state-of-the-art AI models with traditional code analysis techniques, the system provides comprehensive insights into student understanding while generating pedagogically sound prompts that encourage deeper learning.

### 🎯 Key Capabilities

- **🔍 Multi-dimensional Code Analysis**: Combines AST structural analysis with CodeBERT semantic understanding
- **🧠 Intelligent Misconception Detection**: Identifies common Python learning difficulties through research-backed patterns
- **💡 Educational Prompt Generation**: Creates adaptive questions that guide learning without revealing solutions
- **📊 Comprehensive Assessment**: Provides detailed insights into student competence levels
- **⚡ Real-time Processing**: Supports both immediate feedback and batch analysis

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Git
- 4GB+ RAM (for CodeBERT model)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/student-competence-analysis
cd student-competence-analysis

# Set up the project structure
python setup_project.py

# Install dependencies
pip install -r requirements.txt
```

### Run the Demo

```bash
# Run the complete demonstration
python demo_runner.py
```

Expected output:
```
🚀 Python Student Competence Analysis - Live Demo
================================================================
📝 Analyzing: Function naming misconception
================================================================
🔍 Step 1: AST Feature Extraction
✅ AST Features: {'functions': 1, 'loops': 0, 'conditionals': 0, 'complexity': 1}
🧠 Step 2: CodeBERT Semantic Analysis
✅ Code Embedding Shape: torch.Size([1, 768])
💡 Step 3: Educational Prompt Generation
>> Educational Prompt: Your function is called 'add_numbers' but contains 
   subtraction. Why might that be confusing for someone reading your code?
```


## Research Plan

I will evaluate **CodeBERT (microsoft/codebert-base)** combined with Abstract Syntax Tree (AST) analysis to assess Python student competence. This hybrid approach uses AST parsing to capture structural features in student code while leveraging CodeBERT embeddings for semantic understanding. The goal is to detect common misconceptions (such as misuse of functions, scoping errors, or logic mistakes) and then generate educational prompts that guide deeper reasoning without giving solutions directly.

To validate the approach, I will test the model on multiple student code samples, measuring prompt quality against Bloom’s taxonomy alignment, learning objective relevance, and solution-avoidance accuracy. Prompt outputs will also be reviewed by educators to check pedagogical soundness. Technical validation will include AST parsing accuracy, semantic embedding consistency, and misconception detection precision. This ensures a balance of performance, interpretability, and educational effectiveness.

---

## Reasoning

**1. What makes a model suitable for high-level competence analysis?**  
It must understand both syntax and semantics of code, adapt to educational contexts through fine-tuning, and provide interpretable results that educators can trust.

**2. How would you test whether a model generates meaningful prompts?**  
By checking prompt quality against Bloom’s taxonomy, expert educator review, and ensuring prompts encourage reasoning without revealing direct solutions.

**3. What trade-offs exist between accuracy, interpretability, and cost?**  
Transformers like CodeBERT offer high accuracy but are compute-heavy, while AST-based features are lightweight and interpretable. The hybrid balances both but may still need fine-tuning for efficiency.

**4. Why CodeBERT, and what are its strengths/limitations?**  
*Strengths*: Strong code-text semantic understanding, open-source, proven for code tasks, active community support.  
*Limitations*: Requires fine-tuning for education, high compute requirements, not always interpretable without AST support.


### Development Setup
```bash
# Development installation
git clone https://github.com/yourusername/student-competence-analysis
cd student-competence-analysis
pip install -r requirements.txt

# Run tests
python -m pytest tests/

# Start interactive development
jupyter notebook notebooks/
```

## 📚 Documentation

- **📋 [research_plan.md](research_plan.md)**: Comprehensive research methodology and framework

## 🎯 Getting Started Checklist

Ready to explore the system? Follow this checklist:

- [ ] **Clone the repository** and run `setup_project.py`
- [ ] **Install dependencies** with `pip install -r requirements.txt`
- [ ] **Run the demo** using `python demo_runner.py`
- [ ] **Explore the code** in `src/python_code_analyzer.py`
- [ ] **Try your own examples** by modifying the demo code
- [ ] **Read the research plan** for detailed methodology
- [ ] **Contribute improvements** via pull requests

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.




---