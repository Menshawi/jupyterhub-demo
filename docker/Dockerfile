# Build as jupyterhub/singleuser
# Run with the DockerSpawner in JupyterHub

ARG BASE_IMAGE=jupyter/base-notebook
FROM $BASE_IMAGE
MAINTAINER Project Jupyter <jupyter@googlegroups.com>

ARG JUPYTERHUB_VERSION=master
# install pinned jupyterhub and ensure notebook is installed
RUN python3 -m pip install jupyterhub==0.8.0b3 && \
    python3 -m pip install notebook

