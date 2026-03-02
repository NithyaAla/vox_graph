def build_graph(entities, relations):
    node_ids = set()
    nodes = []
    edges = []

    for e in entities:
        if e["id"] not in node_ids:
            node_ids.add(e["id"])
            nodes.append({
                "id": e["id"],
                "label": e["name"],
                "type": e["type"],
                "confidence": e.get("confidence", 1.0)
            })

    for r in relations:
        edges.append({
            "source": r["source"],
            "target": r["target"],
            "type": r["relation"],
            "confidence": r.get("confidence", 1.0)
        })

    return {
        "nodes": nodes,
        "edges": edges
    }
