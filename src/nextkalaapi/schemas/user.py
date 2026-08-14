from enum import Enum

from pydantic import BaseModel


# user update
class UserInfoUpdate(BaseModel):
    first_name: str
    last_name: str
    email: str


class UserPasswordUpdate(BaseModel):
    password: str


# user create
class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    username: str
    password: str

# TODO: UserResponse

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    maiden_name: str | None = None
    age: int | None = None
    gender: Gender | None = None
    phone: str | None = None
    username: str | None = None
    password: str | None = None
    birth_date: str | None = None
    image: str | None = None
    blood_group: str | None = None
    height: float | None = None
    weight: float | None = None
    eye_color: str | None = None
    hair: Hair | None = None
    ip: str | None = None
    address: Address | None = None
    mac_address: str | None = None
    university: str | None = None
    bank: Bank | None = None
    company: Company | None = None
    ein: str | None = None
    ssn: str | None = None
    user_agent: str | None = None
    crypto: Crypto | None = None
    role: Role | None = None


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
