ENTITY_PROMPT = """
Extract structured entities from the text.

Return JSON ONLY.

Schema:
{
  "entities": [
    {
      "id": "E1",
      "type": "Person|Organization|Concept|Event|Location|Project|Paper|Topic|Decision|Risk",
      "name": "string",
      "confidence": 0.0-1.0
    }
  ]
}

Text:
"""

RELATION_PROMPT = """
Extract relationships between entities.

Return JSON ONLY.

Schema:
{
  "relations": [
    {
      "source": "E1",
      "relation": "works_at|collaborates_with|researches|founded|funded_by|influences|mentions|supports|contradicts|related_to|caused_by",
      "target": "E2",
      "confidence": 0.0-1.0
    }
  ]
}

Text:
"""

GRAPH_PROMPT = """
Convert this structured data into a graph format.

Return JSON ONLY.

Schema:
{
  "nodes": [
    {"id": "E1", "label": "Dr Smith", "type": "Person"}
  ],
  "edges": [
    {"source": "E1", "target": "E2", "type": "researches"}
  ]
}

Data:
"""