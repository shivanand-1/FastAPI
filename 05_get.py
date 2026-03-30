from fastapi import FastAPI,HTTPException
app=FastAPI()
fake_id={1:"rice",2:"wheat",3:"corn"}
@app.get("/crops/{crops_id}")
def crops(crop_id:int):
    if crop_id not in fake_id:
        raise HTTPException(status_code=404,detail="Item not found")
    return fake_id