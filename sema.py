from pydantic import BaseModel



class Osoba(BaseModel):
    id:int
    ime:str
    prezime:str
    grad:str
    adresa:str
    transakcija:bool
    
class pravi_osobu(Osoba):
    pass