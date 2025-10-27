#  Document Chunk-inizer = Docling + Ollama 

## Introduction

**Document Chunk-inizer**! This tool is experimental integration based on of both Docling for document parsing and Ollama for local models. It enables you to use Docling and Ollama for RAG over PDF files (or other supported file format) with LlamaIndex. It provides you a sleek clean Streamlit GUI to chat with your own documents locally.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python**:  Python version >3.10 installed. 
- **Pip**: Ensure pip is installed to manage Python packages. It usually comes with Python.
- **venv**: virtual environment to manage dependencies. 
- **Ollama**: Make sure Ollama is installed and llama3.2 model is pulled.
- **Streamlit**:  Open source framework for dynamic UI/UX. 


## Installation

**Document Chunk-inizer** installation:

1. **Clone the repo**:

    ```bash
    git clone <git repo>
    ```

2. **Navigate to the project directory**:

    ```bash
    cd <project_folder>
    ```

3. **Create a virtual environment** (recommended):

    Use Conda: (recommended)
    ```bash
      conda create -n ai python=3.11 -y && conda activate ai
    ```
    Or Use Python VENV:
    ```bash
    python3 -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```

5. **Install the dependencies**:

    ```bash
    pip install torch 
    pip install numpy 
    pip install streamlit 
    pip install pdfplumber 
    pip install git+https://github.com/huggingface/transformers 

    pip install llama-index-core llama-index-readers-docling llama-index-node-parser-docling llama-index-readers-file python-dotenv llama-index-llms-ollama llama-index-embeddings-huggingface llama-index-llms-huggingface-api

    ```

## Running the Tool

To run **Document Chunk-inizer**, execute the following command:

```bash
streamlit run app.py
```

Open your browser and go to `http://localhost:8501` to see the tool in action, if it doesnt open automatically.

## Usage

From left panel, upload your local PDF file, and start chatting with them.


## License

This project is licensed under the APACHE 2.0 License - see the `LICENSE` file for details.

