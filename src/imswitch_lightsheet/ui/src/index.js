import React from "react";
import ReactDOM from "react-dom/client";
import LightsheetWidget from "./Widget"; // Ensure correct import

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <LightsheetWidget />
  </React.StrictMode>
);