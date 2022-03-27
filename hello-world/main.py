from typing import Optional
from enum import Enum

from pydantic import BaseModel, Field

from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()


# Models

class HairColor(Enum):
    white = "White"
    black = "Black"
    red = "Red"


class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    last_name: str = Field(
        ...,
        min_length=1,
        max_length=50
        )
    age: int = Field(
        ...,
        gt=0,
        le=115
        )
    hair_color: Optional[HairColor] = Field(default=None)
    is_married: Optional[bool] = Field(default=None)


class Location(BaseModel):
    city: str
    state: str
    country: str


@app.get("/")
def home():
    return {"hello": "World"}


@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person


@app.get("/person/detail")
def person_detail(
        name: Optional[str] = Query(
            default=None,
            min_length=1,
            max_length=50,
            title="Person Name",
            description="This is a person name. It's between 1 and 50 character"),
        age: int = Query(...)

):
    return {
        "name": name,
        "age": age
    }


@app.get("/person/detail/{person_id}")
def person_detail(person_id: int = Path(..., gt=0)):
    return {
        "person_id": person_id
    }


@app.put("/person/{person_id}")
def update_person(
        person_id: int = Path(..., title="Person ID", description="This is the person ID", gt=0),
        person: Person = Body(...),
        location: Location = Body(...)
):
    # results = person.dict()
    # results.update(location.dict())
    results = dict()
    results.update(dict(person))
    results.update(dict(location))
    return results
