Run api dev-server:
```
cd python-fastapi-server
pip install -r requirements.txt
uvicorn app.main:app
```

Build basket apiserver docker image
```
docker build -t akuma5157/basket-api:local python-fastapi-server
```

Run basket apiserver docker container
```
docker run -p 8000:80 akuma5157/basket-api:local
```

visit [Swagger UI](http://localhost:8000/docs)
