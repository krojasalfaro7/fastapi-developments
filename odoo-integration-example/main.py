from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"result": "Odoo Integration Example"}
