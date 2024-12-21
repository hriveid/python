from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def return_greet():
    print("Hi")
    return "Hello,World!"


