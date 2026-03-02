# 🎤 VoxGraph

VoxGraph is a full-stack AI demo that converts speech into a **structured knowledge graph**. Users provide a public audio URL, and the app:

1. Transcribes the audio using **Mistral Voxtral**.
2. Extracts entities and relations with **Mistral chat models**.
3. Builds and renders a knowledge graph in the browser using **React + Cytoscape**.

---
<img width="955" height="276" alt="image" src="https://github.com/user-attachments/assets/1fc8014e-b920-4b51-afe9-5a7b26dd2948" />


## 🧰 Tech Stack

- **Backend**: FastAPI, Python, Requests  
- **Frontend**: React, Vite, Cytoscape.js  
- **AI Models**: Mistral Voxtral for audio transcription, Mistral chat models for entity/relation extraction  
- **Deployment**: Local development (can be extended to cloud)

---

## ⚡ Features

- Supports public audio URLs (`.mp3` or `.wav`)  
- Automatic transcription + entity/relation extraction  
- Knowledge graph visualization with nodes and edges  
- CORS-enabled for local frontend-backend integration  

---

## 📦 Setup Instructions

### 1. Clone the repository
```bash
git clone <your-repo-url>
cd vox_graph

### 2. Backend Setup

Navigate to the backend folder:

cd backend

Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate       # Windows

Install dependencies:

pip install -r requirements.txt

Create a .env file in backend/ with your Mistral API key:

MISTRAL_API_KEY=<your-mistral-api-key>

Run the backend:

uvicorn backend.application:app --reload

Runs on http://localhost:8000 by default.

### 3. Frontend Setup

Navigate to the frontend folder:

cd ../frontend

Install dependencies:

npm install

Run the frontend:

npm run dev

Opens on http://localhost:5173.

### 📝 Usage

Open your browser to http://localhost:5173.

Paste a publicly accessible audio URL (.mp3 or .wav).

Click “Build Knowledge Graph”.

Wait a few seconds — the transcript and graph will appear.

Tip: Use raw GitHub URLs for audio files. Example:
https://raw.githubusercontent.com/username/repo/main/audio.mp3

### ⚙️ Configuration

CORS is enabled for * origins in application.py.

Update the Voxtral model in mistral_client.py:

MODEL = "voxtral-mini-latest"

Ensure your audio URL is publicly accessible — private links will fail.

🚀 Project Structure
vox_graph/
├── backend/
│   ├── application.py        # FastAPI backend
│   ├── models.py             # Pydantic models
│   ├── graph_builder.py      # Graph construction logic
│   ├── mistral_client.py     # Voxtral + Mistral API calls
│   
├── frontend/
│   ├── app.jsx               # Main React app
│   ├── api.js                # Axios calls to backend
│   ├── graph.jsx             # Cytoscape graph rendering
│   ├── main.jsx              # React entrypoint
│   ├── styles.css            # Styling
│   └── vite.config.js        # Vite config
└── README.md
⚠️ Notes

The app requires public URLs for audio files. Private storage services may fail.

Backend calls Mistral’s Voxtral model — ensure you have a valid API key.

The transcription and entity/relation extraction can take a few seconds per audio.

📄 License

MIT License © 2026



