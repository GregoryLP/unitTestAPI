from typing import Optional

from pydantic import BaseModel, Field


class ClasseSchema(BaseModel):
    name: str = Field(...)
    doctrine: str = Field(...)
    element: str = Field(...)

    class Config:
        schema_extra = {
            "example":     {
                "name": "Titan",
                "doctrine": "Solaire",
                "element": "Feu"
            }
        }


class UpdateClasseDestinyModel(BaseModel):
    name: Optional[str]
    doctrine: Optional[str]
    element: Optional[str]

    class Config:
        schema_extra = {
            "example":     {
                "name": "Titan",
                "doctrine": "Solaire",
                "element": "Feu"
            }
        }

def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }