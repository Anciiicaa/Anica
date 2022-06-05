from email.policy import default
from sqlalchemy import Column, Integer, String, Boolean
from tables import Col
from konekcija import Base

class Osoba(Base):
    __tablename__ = "osobe"
    id = Column(Integer, primary_key = True, index = True)
    ime = Column(String, index = True, default="Anica")
    prezime = Column(String, index = True,default = "Stojadinovic")
    grad = Column(String, default = "hna")
    adresa = Column(String, default="Zmaj jovina")
    transakcija = Column(Boolean, default = True)
