from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_somethin():
    return {"msg":"Hello bro"}