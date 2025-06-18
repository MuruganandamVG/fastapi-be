# routes/resume.py
from fastapi import FastAPI, UploadFile, File
from fastapi import APIRouter, UploadFile, File, Form
from utils.resume_parser import parse_resume


router = APIRouter()

@router.post("/parse_resume")
async def parse_upload_resume(file: UploadFile = File(...)):
    # resume_path = "sample_resume.pdf"

    # # Read local file like you would handle an uploaded file
    # with open(resume_path, "rb") as f:
    #     contents = f.read()

    # filename = resume_path
    contents = await file.read()
    filename = file.filename
    resume_text = parse_resume(filename, contents)
   
    return {"parsed_data": resume_text}
