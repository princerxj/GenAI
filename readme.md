# GenAI Learning Repository

This repository contains hands-on experiments and small applications built while
learning generative AI, LangChain, LangGraph, retrieval-augmented generation
(RAG), agents, and structured model outputs.

The repository is intentionally incremental: the notebooks introduce concepts
in order, while the scripts in [`apps/`](D:/GenAI/apps) turn several of those
concepts into runnable command-line or Streamlit applications.

## Contents

- **Foundations:** prompts, chat history, streaming, structured output, and
  tokenization.
- **Agents:** tool-calling agents, Google Search integration, multi-agent
  workflows, and human-in-the-loop patterns.
- **RAG:** document loading, chunking, embeddings, vector stores, PDF question
  answering, and graph-based retrieval.
- **Applications:** chatbots, a task-management SQL agent, a web-search agent,
  and a PDF question-answering app.

## Repository layout

```text
.
├── apps/
│   ├── 1_qna_bot.py
│   ├── 2_google_agent.py
│   ├── 3_qna_bot_with_groq.py
│   ├── 4_sql_agent.py
│   ├── 5_rag_agent.py
│   ├── 6_langgraph_qna_bot.py
│   ├── doc_files/
│   │   ├── data_science_syllabus.pdf
│   │   └── medical_report.pdf
│   └── my_tasks.db
├── data/
│   ├── chat.txt
│   ├── data_science_syllabus.pdf
│   ├── employee_records.csv
│   ├── medical_report.pdf
│   ├── speech.txt
│   └── sql_prompt.txt
├── notebooks/
│   ├── 1_basic_langchain_with_openai.ipynb
│   ├── 2_prompt_chains.ipynb
│   ├── 3_basic_memory_with_langchain.ipynb
│   ├── 4_structured_outputs.ipynb
│   ├── 5_ollama.ipynb
│   ├── 6_groq.ipynb
│   ├── 7_streaming_response.ipynb
│   ├── 8_basic_agents.ipynb
│   ├── 9_google_search_agent.ipynb
│   ├── 10_rag_load_document.ipynb
│   ├── 11_rag_splitter.ipynb
│   ├── 12_vector_embeddings.ipynb
│   ├── 13_rag_based_pdf_qna_bot.ipynb
│   ├── 14_rag_ai_agent.ipynb
│   ├── 15_pydantic_data_validation.ipynb
│   ├── 16_langgraph_basic.ipynb
│   ├── 17_langgraph_qna_bot.ipynb
│   ├── 18_multi_ai_agent.ipynb
│   ├── 19_rag_with_graph.ipynb
│   ├── 20_human_in_the_loop.ipynb
│   └── vector_db/                 # Generated Chroma persistence files
├── requirements.txt
├── tok.ipynb                      # Standalone tiktoken experiment
├── .gitignore
└── readme.md
```

The `.venv/` directory and `.env` file are intentionally ignored by Git. The
vector database and SQLite database are local development artifacts/data used
by the examples; they are not production database deployments.

## Applications

Run the commands below from the repository's `apps` directory unless noted
otherwise. This is important because the SQL agent opens `my_tasks.db` and the
RAG agent reads/writes `./doc_files/` using relative paths.

### 1. Basic Q&A bot

[`apps/1_qna_bot.py`](D:/GenAI/apps/1_qna_bot.py) is a Streamlit chat interface
that sends questions to a Groq-hosted model and keeps the conversation in
Streamlit session state.

```powershell
cd apps
streamlit run 1_qna_bot.py
```

### 2. Google Search agent

[`apps/2_google_agent.py`](D:/GenAI/apps/2_google_agent.py) is an interactive
terminal agent. It uses Groq for responses and Google Serper as a search tool
for current information. Enter `quit`, `exit`, or `bye` to stop it.

```powershell
cd apps
python 2_google_agent.py
```

### 3. Streaming search agent

[`apps/3_qna_bot_with_groq.py`](D:/GenAI/apps/3_qna_bot_with_groq.py) provides a
Streamlit version of the search agent and streams the generated answer into
the chat UI.

```powershell
cd apps
streamlit run 3_qna_bot_with_groq.py
```

### 4. SQL task-management agent

[`apps/4_sql_agent.py`](D:/GenAI/apps/4_sql_agent.py) uses a LangChain SQL
toolkit and the SQLite database [`apps/my_tasks.db`](D:/GenAI/apps/my_tasks.db).
It can create, read, update, and delete tasks through natural-language prompts.
The agent is instructed to limit list queries to ten recent rows and confirm
mutations with a follow-up query.

```powershell
cd apps
streamlit run 4_sql_agent.py
```

### 5. PDF RAG agent

[`apps/5_rag_agent.py`](D:/GenAI/apps/5_rag_agent.py) accepts one or more PDF
uploads, splits their text into overlapping chunks, creates local Ollama
embeddings, stores them in an in-memory vector store, and answers questions
using retrieved context.

```powershell
cd apps
streamlit run 5_rag_agent.py
```

The app expects the Ollama `nomic-embed-text` model to be available locally:

```powershell
ollama pull nomic-embed-text
```

### 6. LangGraph Q&A bot

[`apps/6_langgraph_qna_bot.py`](D:/GenAI/apps/6_langgraph_qna_bot.py) builds a
minimal LangGraph with a typed `ChatState`, one chatbot node, and in-memory
checkpointing. It runs in the terminal and uses the same exit commands as the
Google Search agent.

```powershell
cd apps
python 6_langgraph_qna_bot.py
```

## Notebook guide

| Notebook | Focus |
| --- | --- |
| [`1_basic_langchain_with_openai.ipynb`](D:/GenAI/notebooks/1_basic_langchain_with_openai.ipynb) | First LangChain chat model integration |
| [`2_prompt_chains.ipynb`](D:/GenAI/notebooks/2_prompt_chains.ipynb) | Prompt templates and chains |
| [`3_basic_memory_with_langchain.ipynb`](D:/GenAI/notebooks/3_basic_memory_with_langchain.ipynb) | Conversational memory |
| [`4_structured_outputs.ipynb`](D:/GenAI/notebooks/4_structured_outputs.ipynb) | Structured model responses |
| [`5_ollama.ipynb`](D:/GenAI/notebooks/5_ollama.ipynb) | Local Ollama models |
| [`6_groq.ipynb`](D:/GenAI/notebooks/6_groq.ipynb) | Groq model integration |
| [`7_streaming_response.ipynb`](D:/GenAI/notebooks/7_streaming_response.ipynb) | Streaming model output |
| [`8_basic_agents.ipynb`](D:/GenAI/notebooks/8_basic_agents.ipynb) | Agent fundamentals |
| [`9_google_search_agent.ipynb`](D:/GenAI/notebooks/9_google_search_agent.ipynb) | Search-enabled agents |
| [`10_rag_load_document.ipynb`](D:/GenAI/notebooks/10_rag_load_document.ipynb) | Loading source documents |
| [`11_rag_splitter.ipynb`](D:/GenAI/notebooks/11_rag_splitter.ipynb) | Splitting documents into chunks |
| [`12_vector_embeddings.ipynb`](D:/GenAI/notebooks/12_vector_embeddings.ipynb) | Embeddings and vector search |
| [`13_rag_based_pdf_qna_bot.ipynb`](D:/GenAI/notebooks/13_rag_based_pdf_qna_bot.ipynb) | PDF-based RAG chatbot |
| [`14_rag_ai_agent.ipynb`](D:/GenAI/notebooks/14_rag_ai_agent.ipynb) | RAG agent with retrieval tools |
| [`15_pydantic_data_validation.ipynb`](D:/GenAI/notebooks/15_pydantic_data_validation.ipynb) | Pydantic validation |
| [`16_langgraph_basic.ipynb`](D:/GenAI/notebooks/16_langgraph_basic.ipynb) | LangGraph state and edges |
| [`17_langgraph_qna_bot.ipynb`](D:/GenAI/notebooks/17_langgraph_qna_bot.ipynb) | Q&A bot implemented with LangGraph |
| [`18_multi_ai_agent.ipynb`](D:/GenAI/notebooks/18_multi_ai_agent.ipynb) | Multi-agent coordination and API tools |
| [`19_rag_with_graph.ipynb`](D:/GenAI/notebooks/19_rag_with_graph.ipynb) | Graph-based RAG |
| [`20_human_in_the_loop.ipynb`](D:/GenAI/notebooks/20_human_in_the_loop.ipynb) | Human approval/intervention in workflows |

[`tok.ipynb`](D:/GenAI/tok.ipynb) is a separate tokenization experiment. It
uses `tiktoken` to encode and decode text with a GPT-4 tokenizer.

## Data and generated stores

- [`data/`](D:/GenAI/data) contains text prompts/samples, a large employee CSV,
  and PDF examples used by notebook experiments.
- [`apps/doc_files/`](D:/GenAI/apps/doc_files) contains the PDFs used as the
  default upload directory for the Streamlit RAG app.
- [`apps/my_tasks.db`](D:/GenAI/apps/my_tasks.db) is the SQLite task database
  used by the SQL agent.
- [`notebooks/vector_db/`](D:/GenAI/notebooks/vector_db) contains Chroma
  persistence files produced by notebook-based vector-store experiments.

## Setup

Use Python 3.12 or a compatible recent Python 3 release. Create and activate a
virtual environment, then install the repository dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Create a `.env` file in the repository root for services that need credentials:

```dotenv
GROQ_API_KEY=your_groq_api_key
SERPER_API_KEY=your_serper_api_key
OPENAI_API_KEY=your_openai_api_key
WEATHER_API_KEY=your_weather_api_key
```

Only add the variables required by the example you are running. Do not commit
`.env` or API keys. `GROQ_API_KEY` is required by the Groq applications,
`SERPER_API_KEY` is required by the Google Search agents, and
`WEATHER_API_KEY` is used by the weather-tool experiment in notebook 18.
Notebook 1 and `tok.ipynb` may also require packages or credentials beyond the
shared application requirements.

## Dependency groups

[`requirements.txt`](D:/GenAI/requirements.txt) includes:

- LangChain, LangGraph, LangChain community integrations, and text splitters
- Groq, Google GenAI, OpenAI, and Ollama integrations
- Streamlit for the web applications
- PDF loading, Beautiful Soup, Wikipedia, Chroma, and Pydantic

Some notebooks are exploratory and may use an additional package not listed in
the shared requirements file. Install those packages in the active environment
only when the corresponding notebook reports a missing import.

## Learning path

```text
Models → Prompts → Memory → Structured output → Streaming
       → Agents and tools → RAG → LangGraph → Human-in-the-loop
       → Streamlit applications
```

This is a learning repository rather than a production service. Model names,
provider APIs, notebook APIs, and integration packages may change over time;
check the relevant provider documentation when an example no longer runs.
