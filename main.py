from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def read_root(name: str = "Luna-Corn"):
    name = name.strip().title()
    return  f"Hello {name}"



@app.get("/calc/add/")
def add(a: int, b: int):
    res = a + b
    return {
        "result": res
    }


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)