from xmlrpc.client import boolean
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from typing import List

import crud, model, sema
from konekcija import SessionLocal, engine


model.Base.metadata.create_all(bind=engine)


app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    

@app.post("/osobe/", response_model=sema.Osoba)
def create_osobe(osoba: sema.pravi_osobu, db: Session = Depends(get_db)):
    db_user = crud.dodaj_u_tabelu(db, id=osoba.id)
    if db_user:
        raise HTTPException(status_code=400, detail="ID already exist")
    return crud.createOsoba(db=db, osoba=osoba)


@app.get("/osobe/", response_model=List[sema.Osoba])
def read_osobe(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    osobe = crud.get_osobe(db, skip=skip, limit=limit)
    return osobe

#Ovde mi lepo dodaje u tabelu, ali mi pise da je greska 500 i ovo sve ostalo kad pozovem izlazi mi greska 500, ne znam sto
@app.post("/osobe/dodaj/", response_model=sema.pravi_osobu)
def dodaj_osobu(id: int, ime:str, prezime:str, adresa:str, grad:str, transakcija:bool, item:sema.pravi_osobu, db:Session = Depends(get_db)):
    return crud.createOsobanova(db = db, osoba=item, id = id, ime = ime,prezime = prezime, adresa = adresa, grad = grad, transakcija=transakcija)

@app.get("/osoba/{osoba_id}", response_model=sema.Osoba)
def ispisiOsobu(id: int, db: Session = Depends(get_db)):
    db_osoba = crud.uzmiOsobusaID(db = db, id = id)
    if db_osoba is None:
        raise HTTPException(status_code=400, detail="ID not exist")
    return db_osoba
        

    



        
        

            