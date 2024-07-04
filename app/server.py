from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from rag_chroma import chain as rag_chroma_chain
from dotenv import load_dotenv
import os

# # Load environment variables from .env file
# load_dotenv()

# # Get the API key from environment variables
# openai_api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")


# Edit this to add the chain you want to add
add_routes(app, rag_chroma_chain, path="/rag-chroma")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
