.PHONY: all check_docker start_docker run_streamlit

all: check_docker run_streamlit


check_docker:
	@docker-compose ps -q LocalGptRedis | grep -q . || (echo "Starting Docker Compose services..." && make start_docker)

start_docker:
	@docker-compose up -d

run_streamlit:
	@echo "Running Streamlit app..."
	@streamlit run Chatbot.py
