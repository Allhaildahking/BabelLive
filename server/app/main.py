from fastapi import FastAPI

app = FastAPI(
    title="BabelLive API",
    description="AI-powered real-time speech translation platform.",
    version="0.1.0"
)


@app.get("/")
def root():
    return {
        "name": "BabelLive",
        "status": "running",
        "version": "0.1.0"
    }


@app.get("/health")
def health():
    return {
        "healthy": True,
        "message": "BabelLive is healthy"
    }


@app.get("/version")
def version():
    return {
        "version": "0.1.0"
    }