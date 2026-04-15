from datetime import date, timedelta

from sqlalchemy.orm import Session
from sqlalchemy import or_

from models import Contact


def create_contact(db: Session, data):
    contact = Contact(**data.dict())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


def get_contacts(db: Session):
    return db.query(Contact).all()


def get_contact(db: Session, contact_id: int):
    return db.query(Contact).filter(Contact.id == contact_id).first()


def update_contact(db: Session, contact_id: int, data):
    contact = get_contact(db, contact_id)
    if contact:
        for key, value in data.dict().items():
            setattr(contact, key, value)
        db.commit()
    return contact


def delete_contact(db: Session, contact_id: int):
    contact = get_contact(db, contact_id)
    if contact:
        db.delete(contact)
        db.commit()
    return contact


def search_contacts(db: Session, query: str):
    return db.query(Contact).filter(
        or_(
            Contact.first_name.ilike(f"%{query}%"),
            Contact.last_name.ilike(f"%{query}%"),
            Contact.email.ilike(f"%{query}%"),
        )
    ).all()


def upcoming_birthdays(db: Session):
    today = date.today()
    next_week = today + timedelta(days=7)

    return db.query(Contact).filter(
        Contact.birthday >= today,
        Contact.birthday <= next_week,
    ).all()