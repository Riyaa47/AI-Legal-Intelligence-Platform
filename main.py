from fastapi import UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os
from dotenv import load_dotenv
from app.api import router

templates = Jinja2Templates(directory="templates")

load_dotenv()

app = FastAPI(title="Legal Intelligence Platform", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/upload", response_class=HTMLResponse)
def upload_page(request: Request):
    return templates.TemplateResponse("upload.html", {"request": request})

import PyPDF2
from io import BytesIO

@app.post("/upload", response_class=HTMLResponse)
async def upload_file(request: Request, file: UploadFile = File(...)):
    import PyPDF2
    from io import BytesIO

    content = await file.read()

    try:
    pdf = PyPDF2.PdfReader(BytesIO(content))
except Exception:
    return HTMLResponse(content="""
    <h2 style='color:red;'>Error reading PDF</h2>
    <p>Make sure you upload a valid text-based PDF.</p>
    <a href="/upload">Go Back</a>
    """)

    text = ""

for page in pdf.pages:
    page_text = page.extract_text()
    if page_text:
        text += page_text

risks = []

    if "termination" not in text.lower():
        risks.append(" Missing termination clause")

    if "liability" not in text.lower():
        risks.append(" No liability clause found")

    if "confidential" not in text.lower():
        risks.append(" Confidentiality clause missing")

    score = max(0, 100 - (len(risks) * 20))

    return templates.TemplateResponse(
        "result.html",
        {
            "request": request,
            "filename": file.filename,
            "score": score,
            "issues": risks
        }
    )
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router, prefix="/api")

@app.get("/", response_class=HTMLResponse)
async def customer_portal():
    """Customer portal - Legal Q&A and Compliance Analysis"""
    try:
        with open("static/customer.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        return HTMLResponse(content="""
        <html>
            <body>
                <h1>Legal Intelligence Platform</h1>
                <p>Customer portal is being developed...</p>
                <p>API documentation: <a href="/docs">/docs</a></p>
            </body>
        </html>
        """)

@app.get("/admin", response_class=HTMLResponse)
async def admin_portal():
    """Admin portal - Document Upload, Knowledge Graph, System Statistics"""
    try:
        with open("static/admin.html", "r", encoding="utf-8") as f:
            return HTMLResponse(content=f.read())
    except FileNotFoundError:
        return HTMLResponse(content="""
        <html>
            <body>
                <h1>Legal-Intelligence-Platform - Admin</h1>
                <p>Admin portal is being developed...</p>
                <p>API documentation: <a href="/docs">/docs</a></p>
            </body>
        </html>
        """)

@app.get("/test", response_class=HTMLResponse)
async def test_page():
    """Test page for debugging"""
    with open("test_stats.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "AI Legal Compliance Assistant System is running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
