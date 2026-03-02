from fastapi import FastAPI
from .models import AudioRequest
from .mistral_client import voxtral_transcribe, mistral_chat
from .prompts import ENTITY_PROMPT, RELATION_PROMPT
from .graph_builder import build_graph
import json
from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(__file__), ".env"))
app = FastAPI(title="VoxGraph API")

@app.post("/voxgraph")
def create_voxgraph(req: AudioRequest):

    # 1. Voxtral
    voxtral_data = voxtral_transcribe(req.audio_url)

    transcript = voxtral_data.get("transcript", "")

    # 2. Entity extraction
    entity_response = mistral_chat(ENTITY_PROMPT + transcript)
    entities = json.loads(entity_response)["entities"]

    # 3. Relation extraction
    relation_response = mistral_chat(RELATION_PROMPT + transcript)
    relations = json.loads(relation_response)["relations"]

    # 4. Graph build
    graph = build_graph(entities, relations)

    return {
        "transcript": transcript,
        "entities": entities,
        "relations": relations,
        "graph": graph
    }