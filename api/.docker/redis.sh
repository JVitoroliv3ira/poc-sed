#!/bin/bash

# Nome do container Redis
CONTAINER_NAME="sed_redis_container"

# Verificar se o container já está em execução
if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    echo "O container Redis ($CONTAINER_NAME) já está em execução."
else
    # Verificar se o container já existe mas não está em execução
    if [ "$(docker ps -aq -f status=exited -f name=$CONTAINER_NAME)" ]; then
        echo "O container Redis ($CONTAINER_NAME) existe, mas não está em execução. Iniciando o container..."
        docker start $CONTAINER_NAME
    else
        echo "Não existe um container Redis em execução. Criando e iniciando um novo container..."
        docker run --name $CONTAINER_NAME -p 6379:6379 -d redis
    fi
    echo "Redis está em execução no container ($CONTAINER_NAME)."
fi
