from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from db import SessionLocal, engine, Base
import crud
import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Contacts API", version="1.0")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/contacts", response_model=schemas.ContactResponse)
def create_contact(contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    return crud.create_contact(db, contact)


@app.get("/contacts")
def get_contacts(db: Session = Depends(get_db)):
    return crud.get_contacts(db)


@app.get("/contacts/{contact_id}")
def get_contact(contact_id: int, db: Session = Depends(get_db)):
    return crud.get_contact(db, contact_id)


@app.put("/contacts/{contact_id}")
def update_contact(contact_id: int, contact: schemas.ContactCreate, db: Session = Depends(get_db)):
    return crud.update_contact(db, contact_id, contact)


@app.delete("/contacts/{contact_id}")
def delete_contact(contact_id: int, db: Session = Depends(get_db)):
    return crud.delete_contact(db, contact_id)


@app.get("/search")
def search(query: str, db: Session = Depends(get_db)):
    return crud.search_contacts(db, query)


@app.get("/birthdays")
def birthdays(db: Session = Depends(get_db)):
    return crud.upcoming_birthdays(db)