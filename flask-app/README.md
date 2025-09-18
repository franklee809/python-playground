## Run docker compose in debug mode

```shell
docker compose -f docker-compose.yml -f docker-compose.debug.yml up
```

### for rebuilding the docker image 
```bash
docker-compose up --build --force-recreate api 
docker-compose up 
docker-compose exec api flask db migrate && flask db upgrade
```