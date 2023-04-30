from fastapi import FastAPI
from routers import paraphrase

app = FastAPI()

app.include_router(paraphrase.router)
