# FastAPI sandbox
Pruebas para crear la documentacion de una API bajo los protocolos de [OpenAPI](https://www.openapis.org/) utilizando el framework de [FastAPI](https://fastapi.tiangolo.com/)

## requerimientos
[python](https://www.python.org/)
[pip](https://pypi.org/project/pip/)

## instalación
Clona el repositorio y entra en la carpeta en la que lo clonaste.
```
git clone git@github.com:flkt-crnpio/fastapi-sandbox.git

cd fastapi-sandbox/
```

Crea tu entorno virtual e instala los requerimientos. Este ejemplo crea el entorno con virtualenv
```
python3 -m pip install virtualenv
python3 -m virtualenv env

source env/bin/activate

pip install -r requirements.txt
```

## prueba entorno local
Para correr la API 
```
uvicorn main:app --reload 
```

La documentación que se genera de la  API se puede ver en localhost
```
http://127.0.0.1:8000/nombredelaurl
``` 
