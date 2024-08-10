#!/bin/bash

# Parâmetros configuráveis
DB_NAME=${1:-sed}
DB_USER=${2:-sed}
DB_PASSWORD=${3:-@myStrongPassword}
SA_PASSWORD=${4:-@myStrongPassword}
CONTAINER_NAME=${5:-sed_database_container}
SQL_SERVER_VERSION=${6:-2019-latest}

# Verificar se o Docker está instalado
if ! command -v docker &> /dev/null; then
    echo "Docker não está instalado. Instale o Docker e tente novamente."
    exit 1
fi

# Verificar se o contêiner já está em execução
if [ "$(docker ps -q -f name=$CONTAINER_NAME)" ]; then
    echo "O contêiner '$CONTAINER_NAME' já está em execução."
else
    # Verificar se o contêiner existe mas está parado
    if [ "$(docker ps -aq -f status=exited -f name=$CONTAINER_NAME)" ]; then
        echo "O contêiner '$CONTAINER_NAME' existe mas está parado. Iniciando..."
        docker start $CONTAINER_NAME
    else
        # Iniciar um novo contêiner do SQL Server
        echo "Iniciando um novo contêiner '$CONTAINER_NAME' do SQL Server..."
        docker run -e "ACCEPT_EULA=Y" -e "SA_PASSWORD=$SA_PASSWORD" \
            -e "MSSQL_PID=Developer" \
            --network=host \
            -p 1433:1433 \
            --name $CONTAINER_NAME \
            -d mcr.microsoft.com/mssql/server:$SQL_SERVER_VERSION
    fi
fi

# Aguardar o SQL Server iniciar
echo "Aguardando o SQL Server iniciar..."
sleep 20

# Criar o banco de dados e o usuário
docker exec -it $CONTAINER_NAME /opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $SA_PASSWORD -Q "
IF NOT EXISTS (SELECT name FROM sys.databases WHERE name = N'$DB_NAME')
BEGIN
    CREATE DATABASE [$DB_NAME];
END;
GO
USE [$DB_NAME];
GO
IF NOT EXISTS (SELECT name FROM sys.server_principals WHERE name = N'$DB_USER')
BEGIN
    CREATE LOGIN [$DB_USER] WITH PASSWORD = '$DB_PASSWORD';
    CREATE USER [$DB_USER] FOR LOGIN [$DB_USER];
    ALTER ROLE db_owner ADD MEMBER [$DB_USER];
END;
GO
"

echo "SQL Server configurado com sucesso."
echo "Nome do Banco de Dados: $DB_NAME"
echo "Usuário: $DB_USER"
echo "Senha: $DB_PASSWORD"
echo "Contêiner Docker: $CONTAINER_NAME"
