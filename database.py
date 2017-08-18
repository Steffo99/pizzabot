from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, BigInteger, Integer, String, ForeignKey, create_engine

# Init the sqlalchemy engine
engine = create_engine("postgres://steffo:HIDDENPASSWORD@royal.steffo.eu:5432/pizzadev")
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)

# Create a new default session
session = Session()


class TelegramUser(Base):
    """Basic Telegram user data"""
    __tablename__ = "tusers"

    tid = Column(BigInteger, primary_key=True)
    tusername = Column(String)
    tfirstname = Column(String, nullable=False)
    tlastname = Column(String)

    def __str__(self):
        if self.tusername is not None:
            return f"@{self.tusername}"
        elif self.tlastname is not None:
            return f"{self.tfirstname} {self.tlastname}"
        else:
            return f"{self.tfirstname}"

    def __repr__(self):
        return f"<User #{self.tid}>"