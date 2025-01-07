# python fastapi logging

https://fastapi.tiangolo.com/advanced/custom-request-and-route/#accessing-the-request-body-in-an-exception-handler

# build

```sh
docker build . -t sample:latest
```

# run

```sh
docker run -p 8080:8080 sample:latest 
```

```
# /
curl 127.0.0.1:8080/

# POST /examine
curl -X POST 127.0.0.1:8080/examine --json '{"name": "foo", "item_id": "xxx"}'

# /items/{item_id}
curl 127.0.0.1:8080/items/1
