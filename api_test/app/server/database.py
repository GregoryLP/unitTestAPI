import motor.motor_asyncio
from bson.objectid import ObjectId
import json

MONGO_DETAILS = "mongodb://localhost:27017"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

file = "json/data.json"

database = client.destinyClasse

destinyClasse = database.get_collection("destinyClasse_collection")

destinyClasse.insert_many(json.load(open(file)))


def classe_destiny(classe) -> dict:
    return {
        "id": str(classe["_id"]),
        "name": classe["name"],
        "doctrine": classe["doctrine"],
        "element": classe["element"],
    }

# all classes present in the database
async def present_classes():
    destinyClasses = []
    async for classe in destinyClasse.find():
        destinyClasse.append(classe_destiny(classe))
    return destinyClasses


# Add a new classe destiny into to the database
async def add_classe(classe_data: dict) -> dict:
    classe = await destinyClasse.insert_one(classe_data)
    new_classe = await destinyClasse.find_one({"_id": classe.inserted_id})
    return classe_destiny(new_classe)


# Update a classe with a matching ID
async def update_classe(id: str, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    classe = await destinyClasse.find_one({"_id": ObjectId(id)})
    if classe:
        updated_classe = await destinyClasse.update_one(
            {"_id": ObjectId(id)}, {"$set": data}
        )
        if updated_classe:
            return True
        return False


# Delete a classe from the database
async def delete_classe(id: str):
    classe = await destinyClasse.find_one({"_id": ObjectId(id)})
    if classe:
        await destinyClasse.delete_one({"_id": ObjectId(id)})
        return True