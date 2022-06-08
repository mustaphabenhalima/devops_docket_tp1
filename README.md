# devops_docket_tp1



# Objectifs

L’objectif du TP est de créer un un wrapper qui retourne la météo d'un lieu donné avec sa latitude et sa longitude (passées en variable d'environnement) en utilisant Openweather API dans le langage de programmation python et packager son code dans une image Docker.

# Les repositories du TP

## GitHub repository

[GitHub - mustaphabenhalima/devops_docket_tp1](https://github.com/mustaphabenhalima/devops_docket_tp1)

## DockerHub

[Docker Hub](https://hub.docker.com/repository/docker/mustaben/firstimageapp)

# Creation du wrapper

### API call


```markdown
https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API key}
```

## Le wrapper

On utilise Python pour la creation du wrapper.

La donnée de la ville est récupéré avec la commande request avec un type Json.

### Le code:
Le code est dans le fichier main.py 

### Le Dockerfile
On utlise un environement python :

```docker
FROM python:3.8-alpine
RUN mkdir /app
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

### Le fichier requirements.txt

```markdown
requests
datetime
```

# Commande pour faire marcher le projet

## Container docker

### Build

```shell
docker build . -f docker.dockerfile -t  firstimageapp
```

### Execute

```shell
docker run --env LAT="5.902785" --env LONG="102.754175" --env API_KEY=2ceb1995c8cc45dbdfd4e287128c7057 myapp
```

### Résultat

```shell
{'coord': {'lon': 102.7542, 'lat': 5.9028}, 'weather': [{'id': 804, 'main': 'Clouds', 'description': 'overcast clouds', 'icon': '04n'}], 'base': 'stations', 'main': {'temp': 26.63, 'feels_like': 26.63, 'temp_min': 26.63, 'temp_max': 26.63, 'pressure': 1008, 'humidity': 74, 'sea_level': 1008, 'grnd_level': 981}, 'visibility': 10000, 'wind': {'speed': 2.7, 'deg': 276, 'gust': 2.85}, 'clouds': {'all': 100}, 'dt': 1654720085, 'sys': {'country': 'MY', 'sunrise': 1654728878, 'sunset': 1654773715}, 'timezone': 28800, 'id': 1736405, 'name': 'Jertih', 'cod': 200}

```

### Taguer l’image

```shell
docker tag myapp mustaben/firstimageapp
```

### Publier l’image sur mon depository DockerHub

```shell
docker push mustaben/firstimageapp
```
