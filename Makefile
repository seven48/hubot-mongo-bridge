default: docker_build

docker_build:
	@docker build -t hubot-mongo-bridge-server .
