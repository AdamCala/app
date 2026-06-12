az acr --name projektadamcdv2
docker build -t ts-api .
docker tag ts-api projektadamcdv2.azurecr.io/test-api:latest
docker push projektadamcdv2.azurecr.io/test-api:latest
