# LLM Log Service

## Create Environments (for dev)

1. set the .env from the .env.example
    - set `MONGO_HOST` to localhost

### MongoDB Service

1. remove the backend in docker compose file
    ```bash
    docker compose up -d
    ```

### Backend Service

1. create conda environment
    ```bash
    conda create -n backend python=3.10
    conda activate backend
    ```

2. install python packages
    ```bash
    pip install -r requirements.txt
    ```

3. set .env from the .env.example

4. start the fastapi
    ```bash
    fastapi dev main.py
    ```

## Docker

````bash
docker compose up -d
```