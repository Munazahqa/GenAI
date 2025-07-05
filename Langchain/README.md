# LangChain

## Requirements
- Python 3.8 or higher
- Install dependencies:
  - langchain
  - langchain-openai
  - langchain-community
  - streamlit
  - python-dotenv
  - faiss-cpu
  - youtube-transcript-api

You can install all dependencies using pip:

```bash
pip install langchain langchain-openai langchain-community streamlit python-dotenv faiss-cpu youtube-transcript-api
```

## Usage

### Pet Name Generator
A Streamlit web application that generates cool names for pets based on animal type and color.

```bash
streamlit run Langchain/main.py
```

### LangChain Helper Functions
The `langchain_helper.py` file contains utility functions for:
- Pet name generation using LLM chains
- Agent initialization with tools (Wikipedia, math)
- YouTube video processing and vector storage   (working on this)

### Running Individual Scripts
You can run specific functions:

```bash
python Langchain/langchain_helper.py
```

## Features
- **Pet Name Generator**: Interactive web app using Streamlit
- **LangChain Agents**: Wikipedia and math tools integration
- **LLM Chains**: Custom prompt templates and chain execution
- **Vector Storage**: FAISS integration for document processing

## Environment Setup
- Set up your environment variables in a `.env` file
- Configure your API keys for OpenAI/OpenRouter
- Ensure all dependencies are installed before running

## Project Structure
```
Langchain/
├── main.py              # Streamlit pet name generator app
├── main1.py             # Additional main script
├── langchain_helper.py  # Core LangChain utilities and functions
└── README.md           # This file
``` 