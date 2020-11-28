# Basket

setup node:
```
echo "installing nodejs12lts"
curl -sL https://deb.nodesource.com/setup_12.x | sudo -E bash -
sudo apt-get install -y nodejs

echo "installing packages"
npm install --dev
```

Build and Run api dev-server:
```
npm run-script start
```

Update frontend angular api services from swagger.yaml
```
sudo docker run -it --rm -v  $PWD:/basket swaggerapi/swagger-codegen-cli-v3:latest generate -i /basket/swagger.yaml -l typescript-angular -o basket/angular-nginx-client/src/api --additional-properties ngVersion=8.2.14,modelPropertyNaming=original
```
