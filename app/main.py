from fastapi import FastAPI
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response
app = FastAPI()
REQUEST_COUNT = Counter("fastapi_requests_total", "Total FastAPI requests", ["path", "method", "status"])
@app.get("/health")
def health():
    REQUEST_COUNT.labels(path="/health", method="GET", status="200").inc()
    return {"status": "ok"}
@app.get("/hello")
def hello():
    REQUEST_COUNT.labels(path="/hello", method="GET", status="200").inc()
    return {"message": "Hello from FastAPI!"}
@app.get("/metrics")
def metrics():
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)
