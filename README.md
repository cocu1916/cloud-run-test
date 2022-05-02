#cloud-run deploy lab
 This repo's purpose is to hold all the files necessary to complete the colud-run deploy lab.  The repo contains a gitignore file, an app.py file, a docker-compose.yml file, a Dockerfile, a make-request.py file, a requirements.txt file, and a phishing model.  After completion, this lab sets up a flask app, sends a predict request, and allows the Flask container to be run via a docker-compose command.  The final goal of this repository is to serve a ML model.

Public URL: https://yay-my-service-khy5k7uyfq-uc.a.run.app/

### With `docker-compose` run Flask container
Build and run:
```bash
docker-compose up
```
### With `docker-compose` execute make-request.py within running container
Build and run:
```bash
docker-compose exec web python make-request.py
```
