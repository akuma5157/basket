Build and Run api dev-server:
```
pip install -r requirements-dev.txt
fastapi-codegen --input ../swagger.yaml --output app -t $PWD/templates/
uvicorn main:app
```

Build docker image
```
docker build -t akuma5157/basket-api:local .
```

Run docker container
```
docker run -p 8000:80 akuma5157/basket-api:local
```

visit [Basket Swagger UI](http://localhost:8000/docs)
