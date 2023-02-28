from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from server.database import (
    add_classe,
    delete_classe,
    present_classes,
    update_classe,
)

from server.model.classeDestiny import (
    ResponseModel,
    ClasseSchema,
    UpdateClasseDestinyModel,
)

router = APIRouter()

@router.post("/", response_description="Une nouvelle classe destiny à été ajouté")
async def add_destiny_classe(classe: ClasseSchema = Body(...)):
    classe = jsonable_encoder(classe)
    new_classe_Destiny = await add_classe(classe)
    return ResponseModel(new_classe_Destiny, "Classe destiny ajouté avec succes.")

@router.get("/{id}", response_description="Récupération des classes destiny")
async def get_classe_destiny(id):
    classes_Destiny = await present_classes(id)
    if classes_Destiny:
        return ResponseModel(classes_Destiny, "Classe destiny récupérer avec succes")


@router.put("/{id}")
async def update_classe_destiny(id: str, req: UpdateClasseDestinyModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_classes = await update_classe(id, req)
    if updated_classes:
        return ResponseModel(
            "Destiny classe avec ID: {} et le nom update avec succes".format(id),
            "Nom de la classe destiny update avec succes",
        )


@router.delete("/{id}", response_description="Student data deleted from the database")
async def delete_classe(id: str):
    deleted_classes = await delete_classe(id)
    if deleted_classes:
        return ResponseModel(
            "La classe destiny avec l'id: {} à été supprimé".format(
                id), "Suppression réussi"
        )