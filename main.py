from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, World!"}


@app.get("/name/{name}")
def greet_name(name:str):
    return {"message": f"Hello, {name}!"}


@app.get("/alter/{alter}")
def show_age(alter:int):
    return {"message": f"Dein Alter ist:{alter}"}


@app.get("/summe/{zahl1}/{zahl2}")
def add_age_numbers(zahl1:int, zahl2:int):
    ergebnis = zahl1 + zahl2
    return {"message": f"Die Summe aus {zahl1} + {zahl2} = {ergebnis}"}
