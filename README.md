# AI-Legal-Intelligence-Platform

## Overview
- Built this project to explore how AI can simplify understanding of legal and regulatory documents  
- Designed a system that converts complex legal text into structured, searchable insights  
- Focused on making compliance analysis more accessible and explainable  
- Combines embeddings, retrieval-based generation, and knowledge graphs  

---

## What This Project Does
- Processes raw legal or regulatory documents  
- Extracts and organizes key information  
- Supports natural language queries  
- Generates context-aware answers  
- Evaluates compliance scenarios and highlights risks  

---

## Key Features

### Document Handling
- Upload support for PDF and HTML files  
- Automatic text extraction and segmentation  
- Prepares data for downstream processing  

### Semantic Search
- Converts text into embeddings for meaning-based search  
- Improves accuracy compared to keyword-based approaches  

### Knowledge Graph Creation
- Extracts entities such as rules, violations, and penalties  
- Builds relationships between them  
- Helps in structuring unorganized legal data  

### Question Answering System
- Retrieval-based pipeline (RAG approach)  
- Fetches relevant context before generating answers  
- Ensures responses are grounded in actual documents  

### Compliance Analysis
- Analyzes business scenarios against regulations  
- Identifies potential risks  
- Suggests improvements and recommendations  

### Web Interface
- Simple UI for document upload and interaction  
- Real-time query handling  
- Displays analysis results clearly  

---

## Tech Stack

### Backend
- Python  
- FastAPI  
- Alibaba Cloud Bailian APIs  
- scikit-learn  

### Data Processing
- PyPDF2 (PDF parsing)  
- BeautifulSoup (HTML parsing)  

### Frontend
- HTML  
- CSS  
- JavaScript  

### Storage
- JSON-based storage  
- Local file system for uploads  

---

## How It Works
1. Upload document and extract text  
2. Convert text into embeddings  
3. Retrieve relevant content during queries  
4. Generate answers using retrieved context  
5. Build knowledge graph for relationships  
6. Apply compliance logic for insights  

---

## Setup

### Requirements
- Python 3.8 or higher
- ## Environment Variables

Create a `.env` file:

```env
ALIBABA_API_KEY=your_api_key
QWEN_MODEL=qwen-turbo
EMBEDDING_MODEL=text-embedding-v1
DATA_DIR=./data
UPLOAD_DIR=./uploads
```

---

## Run the Project

### Option 1
```bash
python run_system.py
```

### Option 2
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

- Open: http://localhost:8000  
- API Docs: http://localhost:8000/docs  

---

## API Routes
- Upload documents  
- Query regulations  
- Build knowledge graph  
- Perform compliance analysis  
- Search regulations  

---

## Project Structure
```
AI-Legal-Intelligence-Platform/
├── app/
├── static/
├── tests/
├── data/
├── uploads/
├── main.py
├── run_system.py
└── requirements.txt
```

---

## What I Learned
- Building backend systems using FastAPI  
- Applying embeddings and semantic search  
- Designing a retrieval-based AI pipeline  
- Structuring data using knowledge graphs  
- Integrating APIs with a frontend  

---

## Future Improvements
- Add authentication and user roles  
- Replace JSON storage with a database  
- Improve UI/UX  
- Support more document formats  
- Deploy on cloud  

---

## Author
Riya

### Installation
```bash
pip install -r requirements.txt
