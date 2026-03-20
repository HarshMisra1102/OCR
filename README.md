# 📄 Shayak AI — OCR API & Document Scanner

🚀 High-performance OCR API for extracting text from images and PDFs  
Built using FastAPI, OpenCV, and Tesseract OCR, and deployed with Docker on Render

---

## 🔥 Overview

Shayak AI OCR is a production-ready document processing system designed to convert unstructured visual data (images and PDFs) into clean, machine-readable text.

It combines image preprocessing techniques with Tesseract OCR to achieve reliable text extraction across real-world inputs.

The system is exposed as a REST API and integrated with a live frontend.

---

## 🌐 Live Deployment

Frontend  
https://ocr-sipg.vercel.app/

API Base URL  
https://ocr-api-opk6.onrender.com

API Documentation  
https://ocr-api-opk6.onrender.com/docs

---

## ✨ Features

📸 Image OCR — Extract text from images and scanned documents  
📄 PDF OCR — Multi-page PDF text extraction  
🧠 Smart Preprocessing — Resizing, denoising, thresholding  
🌍 Multi-language Support — English + Hindi  
🧹 Text Cleaning — Removes noise and fixes OCR errors  
⚡ FastAPI Backend — High-performance REST API  
🐳 Docker Deployment — Production-ready containerized setup  
🌐 Cloud Hosted — Public API with real-world usability  

---

## 🛠️ Tech Stack

Category            Technology  
Language            Python  
Framework           FastAPI  
Image Processing    OpenCV  
OCR Engine          Tesseract OCR  
PDF Handling        pdf2image  
Data Handling       NumPy  
Text Processing     Regex  

---

## 📁 Project Structure

OCR/
│
├── Backend/
│   ├── main.py            # FastAPI entry point
│   ├── ocr_engine.py      # API-OCR bridge
│
├── ocr/
│   ├── preprocess.py      # Image preprocessing
│   ├── extract.py         # OCR execution
│   ├── utils.py           # Text cleaning
│   ├── pipeline.py        # Full pipeline
│
├── frontend/              # UI (Vercel deployed)
│   ├── index.html
│   ├── script.js
│   ├── style.css
│
├── Dockerfile             # Deployment configuration
├── requirements.txt

---

## ⚙️ Installation

### 1️⃣ Clone the repository

git clone https://github.com/HarshMisra1102/OCR.git  
cd OCR  

---

### 2️⃣ Install dependencies

pip install -r requirements.txt  

---

### 3️⃣ Run backend locally

uvicorn Backend.main:app --reload --port 8001  

---

## ▶️ API Usage

### Endpoint

POST /scan  

---

### Example Request

curl -X POST https://ocr-api-opk6.onrender.com/scan \
-F "file=@sample.pdf"

---

### Example Response

{
  "text": "Extracted text here..."
}

---

## 🔄 Pipeline Flow

Input (Image/PDF)  
      ↓  
Preprocessing (Resize + Denoise + Threshold)  
      ↓  
OCR (Tesseract Engine)  
      ↓  
Text Cleaning & Correction  
      ↓  
Final Output (JSON)  

---

## 📊 Performance

🎯 Accuracy: 85–90% on clean documents  
⚡ Processing Time: ~1 second per image  
📄 Supports: Images and multi-page PDFs  

---

## 🚀 Deployment

Backend  
- Dockerized FastAPI service  
- Deployed on Render  

Frontend  
- Static UI deployed on Vercel  

---

## 🧠 Challenges Solved

- Handling noisy and low-quality images  
- Improving OCR accuracy via preprocessing  
- Supporting multi-page PDF extraction  
- Reducing common OCR recognition errors  

---

## 🔮 Future Improvements

📐 Automatic document detection and cropping  
🌍 Expanded multi-language OCR support  
⚡ Async processing for scalability  
🧾 Structured data extraction (tables, forms, resumes)  

---

## 👨‍💻 Author

Harsh Misra  
Backend Developer | OCR Engineer  

Built as part of an AI-powered system — Shayak AI  

---

## ⭐ Why This Project Matters

This project demonstrates:

- Real-world problem solving using computer vision  
- Integration of image processing and OCR systems  
- End-to-end API design and deployment  
- Production-ready backend engineering practices  

---

## 📌 License

Open-source for learning and development purposes