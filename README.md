#  Document Chunk-inizer = Docling + Ollama 

## Introduction

**Document Chunk-inizer**! This experimental integration leverages Docling for document parsing and Ollama to run local language models. It uses LlamaIndex to implement a RAG (Retrieval-Augmented Generation) workflow, allowing users to interact with their PDFs and other supported files through a user-friendly Streamlit graphical interface.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python**:  Python version >3.10 installed. 
- **Pip**: Ensure pip is installed to manage Python packages. It usually comes with Python.
- **venv(Conda)**: virtual environment to manage dependencies. 
- **Ollama**: Make sure Ollama is installed and llama3.2 model is pulled.
- **Docker**:  et of platform as a service products that use OS-level virtualization to deliver software in packages.
- **Milvus-Lite**:  lightweight, embedded version of the open-source vector database.
- **conda**: open-source, cross-platform, language-agnostic package manager and environment management system.
- **Streamlit**:  Open source framework for dynamic UI/UX.

## Prerequisites 
1. **Install Python**:
    ***Ubuntu/Linux***
    ```bash
    sudo apt update
    sudo apt install python3
    sudo apt install python3-pip
    ```
   ***Windows***
    > Download and run executable [Python Release For Windows](https://www.python.org/downloads/windows/)
    
2. **Install Conda**:
    ***Ubuntu/Linux***
    ```bash
    curl -O https://repo.anaconda.com/archive/Anaconda3-2020.11-Linux-x86_64.sh
    bash Anaconda3-2020.11-Linux-x86_64.sh start
    ```
   ***Windows***
    > Download and run executable [Installing Conda on Windows](https://docs.conda.io/projects/conda/en/stable/user-guide/install/windows.html) 
    
3. **Install Ollama**:
    ***Ubuntu/Linux***
    ```bash
    curl -fsSL https://ollama.com/install.sh | sh
    ```
   ***Windows***
    > Download and run executable [Download For Windows](https://ollama.com/download/windows)

3. **Install Docker**:
    ***Ubuntu/Linux***
    ```bash
     sudo apt-get update
     sudo apt-get install ./docker-desktop-amd64.deb // systemctl --user start docker-desktop # start docker
    ```
   ***Windows***
    > Download and run executable [Install Docker For Windows](https://docs.docker.com/desktop/setup/install/windows-install/)
    
4. **Install Milvus-Lite**:
    ***Ubuntu/Linux***
    ```bash
    pip install pymilvus[milvus_lite]
    ```
    
## Setup

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
      conda create -n <environement_name> python=3.11 -y 
      conda env list  
      conda activate <environement_name> 
    ```
    Or Use Python VENV:
    ```bash
    python3 -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```

4. **Install the dependencies**:

    ```bash
    pip install langchain_ollama langchain_docling angchain_text_splitters langchain_milvus langchain_huggingface

    pip install torch 
    pip install numpy 
    pip install streamlit 
    pip install pdfplumber 
    pip install git+https://github.com/huggingface/transformers 

    pip install llama-index-core llama-index-readers-docling llama-index-node-parser-docling llama-index-readers-file python-dotenv llama-index-llms-ollama llama-index-embeddings-huggingface llama-index-llms-huggingface-api

    ```

5. **Start Docker**:
   
    run Docker
    ```bash
    sudo systemctl status docker
    sudo systemctl start docker
    ```

7. **Serve Vector DB**:

    Milvus-Lite Installation
    ```bash
    sudo docker pull milvusdb/milvus:v2.6.4
    curl -sfL https://raw.githubusercontent.com/milvus-io/milvus/master/scripts/standalone_embed.sh -o standalone_embed.sh
    bash standalone_embed.sh start
    ```
    
8. **Ollama**:

    Make sure Ollama is running 
    > check ***http://localhost:11434*** if Ollama is running.


## Running the Tool

To run **Document Chunk-inizer**, execute the following command:

```bash
streamlit run app.py
```

Open your browser and go to `http://localhost:8501` to see the tool in action, if it doesnt open automatically.

## Usage

Upload a local PDF from the left-hand panel, then begin your chat session with the document.


## License

This project is licensed under the APACHE 2.0 License - see the `LICENSE` file for details.


### Snapshot demo
<img src="https://github.com/zF-9/DocuChunk-inizer/blob/22605be5014105a5160dd22df22dcc4661daf6db/images/docuchunkinizer.png">
<img src="https://github.com/zF-9/DocuChunk-inizer/blob/22605be5014105a5160dd22df22dcc4661daf6db/images/dochunk-backend.png">
<img src="https://github.com/zF-9/DocuChunk-inizer/blob/22605be5014105a5160dd22df22dcc4661daf6db/images/dochubk-ready.png">



