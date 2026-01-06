from fastapi import FastAPI
from src.lib.managedb import ManageDb


app = FastAPI()
md = ManageDb()
@app.get("/")
def root():
    return("hola desde fastapi")

@app.get("/api/contacs")
def get_all_contacs():
    return md.read_contact()

