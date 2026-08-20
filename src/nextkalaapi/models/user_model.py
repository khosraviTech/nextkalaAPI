from enum import Enum


from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Enum as SQLEnum, String

class Base(DeclarativeBase):#alchemy db model
    pass
class Role(str, Enum):
    ADMIN = "admin"
    MODERATOR = "moderator"
    USER = "user"
class User(Base):
    id:Mapped[int]=mapped_column(primary_key=True)
    first_name:Mapped[str]=mapped_column(nullable=False)
    last_name:Mapped[str]=mapped_column(nullable=False)
    email:Mapped[str]=mapped_column(nullable=False,index=True,unique=True)
    password:Mapped[str]=mapped_column(nullable=False)
    age: Mapped[int] =mapped_column(nullable=True)
    gender: Mapped[bool] =mapped_column(nullable=True)
    phone: Mapped[str] =mapped_column(nullable=True)
    username: Mapped[str] =mapped_column(nullable=True,index=True)
    birth_date: Mapped[str] =mapped_column(nullable=True)
    image: Mapped[str] =mapped_column(nullable=True)
    blood_group: Mapped[str] =mapped_column(nullable=True)
    height: Mapped[float] =mapped_column(nullable=True)
    weight: Mapped[float] =mapped_column(nullable=True)
    ip: Mapped[str] =mapped_column(nullable=True)
    address: Mapped[str] =mapped_column(nullable=False,String(255),index=True)
    mac_address: Mapped[str] =mapped_column(nullable=True)
    university: Mapped[str] =mapped_column(nullable=True)
    bank: Mapped[str] =mapped_column(nullable=True)
    company: Mapped[str] =mapped_column(nullable=True)
    role: Mapped[Role] =mapped_column(
        SQLEnum(Role),
        default=Role.USER,
        nullable=False
    )
    
