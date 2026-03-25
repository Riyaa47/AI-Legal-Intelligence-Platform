## AI Legal Intelligence Platform

A web-based application that analyzes legal documents (PDFs) and identifies potential risks such as missing clauses. Built using FastAPI and deployed on Render.

---

## Overview

The AI Legal Intelligence Platform allows users to upload legal documents and receive a risk analysis based on the presence or absence of key legal clauses such as:

* Termination clause
* Liability clause
* Confidentiality clause

The system assigns a risk score and highlights issues found in the document.

---

## Features

* Upload PDF legal documents
* Extract text using PyPDF2
* Detect missing important legal clauses
* Generate risk score (out of 100)
* Display issues clearly in UI
* Simple and clean web interface
* Fully deployed on cloud (Render)

---

## Tech Stack

* Backend: FastAPI
* Frontend: HTML, CSS (Jinja2 Templates)
* PDF Processing: PyPDF2
* Deployment: Render
* Language: Python

---

## Project Structure

```
AI-Legal-Intelligence-Platform/
│
├── main.py
├── requirements.txt
├── runtime.txt
├── templates/
│   ├── upload.html
│   └── result.html
├── static/
├── app/
└── README.md
```

---

## Installation (Local Setup)

### Clone the repository

```
git clone https://github.com/your-username/AI-Legal-Intelligence-Platform.git
cd AI-Legal-Intelligence-Platform
```

### Create virtual environment

```
python -m venv venv
venv\Scripts\activate   (Windows)
source venv/bin/activate (Mac/Linux)
```

### Install dependencies

```
pip install -r requirements.txt
```

### Run the application

```
uvicorn main:app --reload
```

### Open in browser

```
http://127.0.0.1:8000
```

---

## Usage

1. Open the application
2. Navigate to `/upload`
3. Upload a PDF legal document
4. View:

   * Risk Score
   * Missing clauses
   * Issues list

---

## API Endpoints

* GET `/` → Homepage
* GET `/upload` → Upload page
* POST `/upload` → Process uploaded file
* GET `/admin` → Admin portal
* GET `/test` → Test page
* GET `/health` → Health check

---

## Deployment

This project is deployed on Render.

### Steps followed:

* Connected GitHub repository
* Set build command:

```
pip install -r requirements.txt
```

* Set start command:

```
uvicorn main:app --host 0.0.0.0 --port 10000
```

* Added runtime.txt for Python version

---

## Common Issues & Fixes

### Internal Server Error on /upload

* Ensure correct template structure:

```
templates/
   upload.html
   result.html
```

* Avoid nested folders like:

```
templates/templates/ ❌
```

---

### TemplateResponse Error

Make sure this is correct:

```
return templates.TemplateResponse(
    "upload.html",
    {"request": request}
)
```

---

### PDF Not Working

* Ensure PDF is text-based (not scanned)
* PyPDF2 cannot extract text from images

---

## Future Improvements

* Integrate AI (GPT-based legal analysis)
* Add authentication system
* Improve UI/UX with modern frontend frameworks
* Add support for DOCX and scanned PDFs
* Store analysis history

---

## Author

Riya

---

## License

This project is for educational and demonstration purposes.
