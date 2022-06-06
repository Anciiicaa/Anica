from sqlalchemy.orm import Session
import model, sema
import sys


def get_osobe(db: Session, skip: int = 0, limit: int = 100):
    return db.query(model.Osoba).offset(skip).limit(limit).all()

def createOsoba(db: Session, osoba: sema.Osoba):
    db_osoba = model.Osoba(id = osoba.id, ime = osoba.ime, prezime = osoba.prezime, grad = osoba.grad, adresa = osoba.adresa, transakcija = osoba.transakcija)
    db.add(db_osoba)
    db.commit()
    db.refresh(db_osoba)
    return db_osoba


def dodaj_u_tabelu(db: Session, id: str):
    return db.query(model.Osoba).filter(model.Osoba.id == id).first()

def createOsobanova(db: Session, osoba: sema.Osoba, id:str, ime:str, prezime:str, grad:str, adresa:str, transakcija:bool):
    db_osoba = model.Osoba(id = id, ime = ime, prezime = prezime, grad = grad, adresa = adresa, transakcija = transakcija)
    db.add(db_osoba)
    db.commit()
    db.refresh(db_osoba)
    return db_osoba

def uzmiOsobusaID(db: Session, id:int):
    return db.query(model.Osoba).filter(model.Osoba.id == id).first()


    

