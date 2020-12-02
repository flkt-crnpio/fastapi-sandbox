from typing import Optional
from fastapi import FastAPI

tags_metadata = [
    {
        "name": "users",
        "description": "Aquí valdría la pena poner _la definición_ de la **colección** y un resumen de que información se puede encontrar",
    },
    {
        "name": "items",
        "externalDocs": {
            "description": "Referencia externa",
            "url": "http://ligadereferencia.com",
        },
    },
]

app = FastAPI(
    title="DVcell test",
    description="Proyecto rápido para probar la creación de documentación y pruebas de una API bajo los protocolos de OpenAPI utilizando el framework de FastAPI",
    version="0.0.0",
    openapi_tags=tags_metadata,
    docs_url="/nombredelaurl",
    redoc_url=None
)

# mocks
mock_users = {"1":{"name":"juanito", "lastname":"perez"}, "2":{"name":"miguel", "lastname":"cervantes"}}
mock_items = {"1":{"name":"Foo"}, "2":{"name":"Bar"}, "3":{"name":"Baz"}}

# rutas
@app.get("/users/", tags=["users"])
async def get_users():
    return mock_users

@app.get("/items/", tags=["items"])
async def get_items():
    return mock_items

@app.get("/items/{item_id}", tags=["items"])
def read_item(item_id: str, q: Optional[str] = None):
    if q:
        return {"item_id": item_id, "item": mock_items.get(item_id), "q": q}
    return mock_items.get(item_id)
