FRONTEND_CONTAINER=re_frontend
ROOT_DIR=$(CURRENT_DIR)
PROJECT_DIR=src
CURRENT_USER=sudo
DOCKER_COMPOSE?=docker-compose
DOCKER_COMPOSE_RUN=$(DOCKER_COMPOSE) run --rm
DOCKER_EXEC_TOOLS_APP=$(CURRENT_USER) docker exec -it $(DOCKER_NAME) sh
NODE_INSTALL="yarn i"
SERVER_RUN="yarn dev"

#
# Exec containers
#
.PHONY: 

app:
	ls


# docker compose -f "docker-compose.yml" up -d --build 

