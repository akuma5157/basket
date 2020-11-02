Build and Run api server:
```
pip install -r requirements-dev.txt
fastapi-codegen --input ../swagger.yaml --output app -t $PWD/templates/
uvicorn main:app
```

visit [Swagger UI](http://localhost:8000/docs)
