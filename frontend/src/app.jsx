import React, { useState } from "react";
import { voxgraphAPI } from "./api.js";
import Graph from "./graph.jsx";

export default function App() {
  const [audioUrl, setAudioUrl] = useState("");
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const runVoxGraph = async () => {
    if (!audioUrl) return;
    try {
      setLoading(true);
      setError(null);
      const res = await voxgraphAPI(audioUrl);
      setData(res);
    } catch (e) {
      console.error(e);
      setError("Failed to process audio. Check backend + URL.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <h1>🎤 VoxGraph</h1>
      <p>Turn speech into structured knowledge</p>

      <div className="input-box">
        <input
          type="text"
          placeholder="Paste public audio URL (.wav/.mp3)"
          value={audioUrl}
          onChange={(e) => setAudioUrl(e.target.value)}
        />
        <button onClick={runVoxGraph}>Build Knowledge Graph</button>
      </div>

      {loading && <p className="loading">Processing audio with Voxtral...</p>}
      {error && <p style={{ color: "red" }}>{error}</p>}

      {data && (
        <>
          <div className="section">
            <h2>Transcript</h2>
            <div className="box">{data.transcript}</div>
          </div>

          <div className="section">
            <h2>Knowledge Graph</h2>
            <Graph graph={data.graph} />
          </div>
        </>
      )}
    </div>
  );
}