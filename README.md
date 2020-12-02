# FastAPI sandbox
Pruebas para crear la documentacion de una API bajo los protocolos de OpenAPI utilizando el framework de FastAPI


## instalación
```

python3 -m pip install virtualenv
python3 -m virtualenv env

source env/bin/activate

pip install -r requirements.txt

```

## pruebas
Para correr la API 
```
uvicorn main:app --reload 
```

La documentación que se genera de la  API se puede ver en localhost
```
http://127.0.0.1:8000/nombredelaurl
``` 
