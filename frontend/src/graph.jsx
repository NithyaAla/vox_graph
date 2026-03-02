import React from "react";
import CytoscapeComponent from "react-cytoscapejs";

export default function Graph({ graph }) {
  if (!graph || !graph.nodes || !graph.edges) return null;

  const elements = [
    ...graph.nodes.map((n) => ({
      data: { id: n.id, label: n.label, type: n.type }
    })),
    ...graph.edges.map((e) => ({
      data: {
        id: `${e.source}-${e.target}`,
        source: e.source,
        target: e.target,
        label: e.type
      }
    }))
  ];

  return (
    <div className="graph-container">
      <CytoscapeComponent
        elements={elements}
        style={{ width: "100%", height: "600px" }}
        layout={{ name: "cose" }}
        stylesheet={[
          {
            selector: "node",
            style: {
              label: "data(label)",
              "text-valign": "center",
              "text-halign": "center",
              "background-color": "#4f46e5",
              color: "#fff",
              "font-size": "10px",
              width: "label",
              height: "label",
              padding: "10px",
              "text-wrap": "wrap"
            }
          },
          {
            selector: "edge",
            style: {
              label: "data(label)",
              width: 2,
              "line-color": "#9ca3af",
              "target-arrow-color": "#9ca3af",
              "target-arrow-shape": "triangle",
              "curve-style": "bezier",
              "font-size": "8px",
              color: "#111827"
            }
          }
        ]}
      />
    </div>
  );
}