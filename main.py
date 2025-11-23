import json
from fastapi import FastAPI, HTTPException, Query

app = FastAPI(title="Dog Profiles API")

# Load JSON once at startup
def load_dogs_json():
    try:
        with open("dogs.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        raise RuntimeError(f"Failed to load dogs.json: {repr(e)}")

DOGS_DATA = load_dogs_json()

# Endpoint: return all dogs
@app.get("/dogs")
def get_dogs(dog_name: str | None = Query(None), owner_name: str | None = Query(None)):
    filtered = []
    for dog_obj in DOGS_DATA:
        if dog_name and dog_name.lower() not in (dog_obj["dog"]["name"] or "").lower():
            continue
        if owner_name and owner_name.lower() not in (dog_obj["owner"]["name"] or "").lower():
            continue
        filtered.append(dog_obj)
    return filtered

# Endpoint: return one dog by dog_id
@app.get("/dogs/{dog_id}")
def get_dog(dog_id: str):
    for dog_obj in DOGS_DATA:
        if dog_obj["dog_id"] == dog_id:
            return dog_obj
    raise HTTPException(status_code=404, detail="Dog not found")