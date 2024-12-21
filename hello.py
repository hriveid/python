from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def return_greet():
    print("Hi")
    return "Hello,World!"


@app.post("/say_name")
def say_name(name:str):
    return f"Hello,{name}"
