from enum import Enum

from pydantic import BaseModel


class Gender(str, Enum):
    MALE = "male"
    FEMALE = "female"


class Role(str, Enum):
    ADMIN = "admin"
    MODERATOR = "moderator"
    USER = "user"


class Coordinates(BaseModel):
    lat: float
    lng: float


class Address(BaseModel):
    address: str
    city: str
    state: str
    state_code: str
    postal_code: str
    coordinates: Coordinates
    country: str


class Hair(BaseModel):
    color: str
    type: str


class Bank(BaseModel):
    card_expire: str
    card_number: str
    card_type: str
    currency: str
    iban: str


class Company(BaseModel):
    department: str
    name: str
    title: str
    address: Address


class Crypto(BaseModel):
    coin: str
    wallet: str
    network: str


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    maiden_name: str
    age: int
    gender: Gender
    email: str
    phone: str
    username: str
    password: str
    birth_date: str
    image: str
    blood_group: str
    height: float
    weight: float
    eye_color: str
    hair: Hair
    ip: str
    address: Address
    mac_address: str
    university: str
    bank: Bank
    company: Company
    ein: str
    ssn: str
    user_agent: str
    crypto: Crypto
    role: Role