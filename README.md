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

Update frontend angular api services from swagger.yaml
```
sudo docker run -it --rm -v  $PWD:/basket swaggerapi/swagger-codegen-cli-v3:latest generate -i /basket/swagger.yaml -l typescript-an
gular -o basket/angular-nginx-client/src/api --additional-properties ngVersion=8.2.14,modelPropertyNaming=original
```

Update backend code from swagger.yaml
```
cd python-fastapi-server
pip install -r requrirements-dev.txt
fastapi-codegen --input ../swagger.yaml --output app -t $PWD/templates"
```