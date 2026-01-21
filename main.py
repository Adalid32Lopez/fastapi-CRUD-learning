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

@app.get("/api/contacts/{id_contact}")
def get_simple_contact(id_contact:str):
    contacts = md.read_contact()

    for contact in contacts:
        if contact["id"] == id_contact:
            return contact
