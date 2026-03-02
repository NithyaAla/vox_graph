import axios from "axios";

export const voxgraphAPI = async (audioUrl) => {
  const res = await axios.post("http://localhost:8000/voxgraph", {
    audio_url: audioUrl
  });
  return res.data;
};