import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import { Button } from "./components/ui/button";

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <>
      <div className="flex flex-col items-center justify-center min-h-svh">
        <h1 className="text-3xl font-bold underline">Hello Vite + React!</h1>
        <Button>Click me</Button>
      </div>
    </>
  </StrictMode>
);
