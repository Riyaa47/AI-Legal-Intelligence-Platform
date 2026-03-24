AI-Legal-Intelligence-Platform
Overview

AI-Legal-Intelligence-Platform is a project I built to explore how AI can simplify the process of understanding and applying legal and regulatory information. The goal was to design a system that can take complex legal documents and turn them into something searchable, explainable, and useful for decision-making.

The platform processes regulatory documents, enables intelligent search, and provides structured compliance insights using modern AI techniques like embeddings, retrieval-based generation, and knowledge graphs.

What This Project Does
Takes raw legal or regulatory documents as input
Extracts and organizes important information
Allows users to ask questions in natural language
Generates context-aware answers
Evaluates compliance scenarios and highlights risks
Key Features
Document Handling

I implemented support for uploading PDF and HTML files, followed by automated text extraction and segmentation to prepare the data for further processing.

Semantic Search

Instead of relying on keyword matching, the system converts text into embeddings. This allows it to find meaning-based matches, which works much better for legal content.

Knowledge Graph Creation

The system identifies important legal entities and builds relationships between them. This helps in structuring otherwise unorganized information and improves explainability.

Question Answering System

I integrated a retrieval-based pipeline where relevant information is first fetched and then used to generate answers. This ensures responses are grounded in actual documents.

Compliance Analysis

One of the core parts of the project is analyzing business scenarios and checking them against regulatory rules. The system highlights potential risks and suggests improvements.

Web Interface

I created a simple frontend where users can upload documents, ask questions, and view results without dealing with backend complexity.

Tech Stack
Backend
Python
FastAPI
AI APIs (Alibaba Cloud Bailian)
scikit-learn
Data Processing
PyPDF2 for PDF parsing
BeautifulSoup for HTML parsing
Frontend
HTML
CSS
JavaScript
Storage
JSON-based storage for simplicity
Local file system for uploaded data
How It Works (High-Level Flow)
Documents are uploaded and processed
Text is converted into embeddings
Relevant chunks are retrieved during queries
A language model generates answers using retrieved context
Knowledge graphs are built to represent relationships
Compliance logic is applied to generate insights
Setup
Requirements
Python 3.8+
Installation
pip install -r requirements.txt
Environment Variables

Create a .env file and add:

ALIBABA_API_KEY=your_api_key
QWEN_MODEL=qwen-turbo
EMBEDDING_MODEL=text-embedding-v1
DATA_DIR=./data
UPLOAD_DIR=./uploads
Running the Project
python run_system.py

or

uvicorn main:app --host 0.0.0.0 --port 8000

Then open:

http://localhost:8000
API Routes
Upload documents
Query regulations
Generate knowledge graph
Perform compliance analysis
Search regulations

(API docs available at /docs when the server is running)

Project Structure
AI-Legal-Intelligence-Platform/
├── app/
├── static/
├── tests/
├── data/
├── uploads/
├── main.py
├── run_system.py
└── requirements.txt
What I Learned
How to design a complete backend system using FastAPI
Practical use of embeddings and semantic search
Building a retrieval-based AI pipeline
Structuring unorganized data using knowledge graphs
Designing APIs and integrating them with a frontend
Possible Improvements
Add user authentication
Move from JSON storage to a database
Improve UI/UX
Support more document formats
Deploy on cloud for real-world usage
Author

Your Name
