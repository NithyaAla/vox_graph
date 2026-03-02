from pydantic import BaseModel
from typing import List

class AudioRequest(BaseModel):
    audio_url: str

class Node(BaseModel):
    id: str
    label: str
    type: str
    confidence: float

class Edge(BaseModel):
    source: str
    target: str
    type: str
    confidence: float