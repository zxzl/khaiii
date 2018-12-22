# Finding nouns

### Launching
```bash 
docker build -t zxzl/khaiii-api .
docker run -it --rm -p 5000:5000 zxzl/khaiii-api
```

### Usage
Send Request
```bash
curl -X POST \
  http://localhost:5000/nouns \
  -H 'Content-Type: application/json' \
  -d '{
  "query": "아버지 가방에 들어가신다"
}'
```
Response
```json
[
    "아버지",
    "가방"
]
```
