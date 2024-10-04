from fastapi import FastAPI
import requests

### Create FastAPI instance with custom docs and openapi url
app = FastAPI(docs_url="/api/py/docs", openapi_url="/api/py/openapi.json")

@app.get("/api/py/helloFastApi")
def hello_fast_api():
    import requests
    # https://hooks.slack.com/services/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
    requests.post("https://hooks.slack.com/services/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",
     json={"text": "Hello FastAPI"})
    return {"message": "Hello FastAPI"}