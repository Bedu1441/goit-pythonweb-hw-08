from datetime import date, timedelta

from sqlalchemy.orm import Session
from sqlalchemy import or_

from models import Contact
from schemas import ContactCreate, ContactUpdate


def create_contact(db: Session, data: ContactCreate):
    contact = Contact(**data.model_dump())
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


def get_contacts(db: Session):
    return db.query(Contact).all()


def get_contact(db: Session, contact_id: int):
    return db.query(Contact).filter(Contact.id == contact_id).first()


def update_contact(db: Session, contact_id: int, data: ContactUpdate):
    contact = get_contact(db, contact_id)
    if contact:
        update_data = data.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(contact, key, value)
        db.commit()
        db.refresh(contact)
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
    contacts = db.query(Contact).all()
    today = date.today()
    next_week = today + timedelta(days=7)

    result = []

    for contact in contacts:
        birthday_this_year = contact.birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        if today <= birthday_this_year <= next_week:
            result.append(contact)

    return result