from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
def return_greet():
    print("Hi")
    return "Hello,World!"


@app.get("/say_name")
def say_name(name:str):
    return f"Hello,{name}"
