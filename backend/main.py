from fastapi import FastAPI, HTTPException, status, Path


app = FastAPI()


@app.get("/")
def root():
    return {"message": "Let's build this app!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}