# LangChain & LangSmith Hands-on Practice

## 📌 Project Overview

This repository contains a set of hands-on experiments with
**LangChain**, **LangSmith**, and **LangGraph**.\
It demonstrates how to build and trace different workflows using modern
LLM tooling, including:

-   Simple & Sequential Workflows\
-   Retrieval-Augmented Generation (RAG) system with PDF indexing\
-   LangChain **ReAct Agents** with external tools\
-   LangGraph-based structured essay evaluation pipeline

The project highlights **LangSmith tracing & observability** for all
major runs.

------------------------------------------------------------------------

## 🚀 Key Features

-   **PDF RAG System** → Load, split, embed, and query PDFs with FAISS.\
-   **Agent System** → ReAct-style agent with weather API + DuckDuckGo
    search.\
-   **LangGraph Workflow** → Parallel evaluation graph for essay
    grading.\
-   **Tracing with LangSmith** → All nodes and steps are observable in
    LangSmith.\
-   **Caching & Fingerprinting** → Avoid redundant index building with
    hash-based caching.

------------------------------------------------------------------------

## 🏗️ Technical Architecture

1.  **RAG System**
    -   Loads PDF (`PyPDFLoader`) → Splits into chunks
        (`RecursiveCharacterTextSplitter`)\
    -   Embeds chunks (`embedding_model`) → Stores in FAISS\
    -   Uses retriever to fetch context → LLM answers questions with
        context-only constraint
2.  **Agent System**
    -   Tools:
        -   DuckDuckGo Search\
        -   Weather API (GoWeather)\
    -   ReAct Prompt (from LangChain Hub)\
    -   AgentExecutor orchestrates reasoning + tool calls
3.  **LangGraph Workflow**
    -   StateGraph with parallel evaluation nodes:
        -   Language quality\
        -   Depth of analysis\
        -   Clarity of thought\
    -   Aggregated by final node → Overall feedback + average score

------------------------------------------------------------------------

## ⚙️ Installation Instructions

``` bash
# Clone the repository
git clone <your-repo-url>
cd <repo-folder>

# Install dependencies
pip install -U langchain langchain-openai langchain-community faiss-cpu pypdf python-dotenv langsmith langgraph pydantic requests
```

------------------------------------------------------------------------

## 📖 Usage Guide

### 1️⃣ Run the RAG PDF System

``` bash
python rag_pdf.py
```

-   Place your PDF as `Algos.pdf` (or update path).\
-   Ask natural language questions → system answers from PDF context.

### 2️⃣ Run the Agent System

``` bash
python agent.py
```

-   Example query: *"Birth Place of Narendra Modi and give me the
    current temperature"*\
-   Agent combines search + weather API to produce answer.

### 3️⃣ Run the LangGraph Essay Evaluator

``` bash
python essay_graph.py
```

-   Evaluates a given essay → Provides dimension-wise feedback + average
    score.

------------------------------------------------------------------------

## 📦 Dependencies

-   **LangChain** (core, community, openai)\
-   **LangSmith**\
-   **LangGraph**\
-   **FAISS** (vector store)\
-   **pypdf**\
-   **pydantic**\
-   **requests**\
-   **python-dotenv**

------------------------------------------------------------------------

## 🤝 Contribution Guidelines

1.  Fork the repo\
2.  Create a new feature branch (`git checkout -b feature-name`)\
3.  Commit changes with clear messages\
4.  Push branch and open PR

------------------------------------------------------------------------

## 📜 License

This project is licensed under the **MIT License** -- feel free to use
and adapt with attribution.
