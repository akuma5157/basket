Install Python:
```
echo "installing python3.8"

sudo apt -y install software-properties-common
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt -y install python3.8 python3.8-venv

echo "setting up symlinks"
cd /usr/bin/
rm -rf python python3
sudo ln -s python3.9 python3
sudo ln -s python3.9 python
cd -

echo "setting up venv and installing libs"
virtualenv .
. bin/activate
pip install -r requirements-dev.txt
deactivate
```

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

Update backend code from swagger.yaml
```
cd python-fastapi-server
pip install -r requrirements-dev.txt
fastapi-codegen --input ../swagger.yaml --output app -t $PWD/templates"
```

visit [Basket Swagger UI](http://localhost:8000/docs)
