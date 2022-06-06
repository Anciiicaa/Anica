from sqlalchemy import Column, Integer, String, Boolean
from tables import Col
from konekcija import Base

class Osoba(Base):
    __tablename__ = "osobe"
    id = Column(Integer, primary_key = True, index = True)
    ime = Column(String, index = True)
    prezime = Column(String, index = True)
    grad = Column(String)
    adresa = Column(String)
    transakcija = Column(Boolean, default = True)
