all: install build

build:
	docker build -t singleuser docker

install:
	./install.sh

start:
	supervisorctl start jupyterhub

restart:
	supervisorctl restart jupyterhub

stop:
	supervisorctl stop jupyterhub

clean-containers:
	-docker rm -f $(shell docker ps -a | grep 'jupyter-' | awk '{print $$1}')

clean-all: clean-containers
	rm -f jupyterhub_cookie_secret jupyterhub.sqlite
