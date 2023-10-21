# Configure Service

```shell
export SERVER_HOST=0.0.0.0
export SERVER_PORT=9000
export SERVER_RELOAD=True
export SERVER_PROXY_HEADERS=True

export PG_STORAGE_HOST=localhost
export PG_STORAGE_PORT=5432
export PG_STORAGE_USERNAME=postgres
export PG_STORAGE_PASSWORD=postgres
export PG_STORAGE_DATABASE=postgres

export JWT_PUBLIC_KEY=
```

```shell
docker build -t code-executor-image .
```

```shell
docker run -dp 9000:9000 code-executor-image
```
