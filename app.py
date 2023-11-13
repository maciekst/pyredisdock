from fastapi import FastAPI, HTTPException

import redis

app = FastAPI()

# Połączenie z serwerem Redis
redis_client = redis.StrictRedis(host='redis', port=6379, db=0)

@app.post("/add_item/{item}")
async def add_item(item: str):
    """
    Dodaje element do kolejki Redis.
    """
    redis_client.rpush('queue', item)
    return {"message": f"Element {item} dodany do kolejki."}

@app.delete("/remove_item")
async def remove_item():
    """
    Usuwa element z kolejki Redis.
    """
    item = redis_client.lpop('queue')
    if item is not None:
        return {"message": f"Usunięto element {item.decode('utf-8')} z kolejki."}
    else:
        raise HTTPException(status_code=404, detail="Kolejka jest pusta.")

@app.get("/get_items")
async def get_items():
    """
    Zwraca wszystkie elementy z kolejki Redis.
    """
    items = redis_client.lrange('queue', 0, -1)
    items = [item.decode('utf-8') for item in items]
    return {"items": items}
