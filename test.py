from fastapi import FastAPI, UploadFile, File
import os

app = FastAPI()

UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.get("/")
def home():
    return {"message": "API работает"}


@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    
    with open(file_path, "wb") as f:
        f.write(file.file.read())
    
    return {"filename": file.filename}


@app.get("/files")
def list_files():
    files = os.listdir(UPLOAD_FOLDER)
    return {"files": files}


@app.delete("/delete/{filename}")
def delete_file(filename: str):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    
    if os.path.exists(file_path):
        os.remove(file_path)
        return {"message": "deleted"}
    
    return {"error": "file not found"}

