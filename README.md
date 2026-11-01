# Shorty

## Obsługa ręczna

Dla URL `http://localhost`

Zapisywanie URL, które pobiera skrót

```bash
curl -i -X POST http://localhost:8000/api/ \
  -H "Content-Type: application/json" \
  -d '{
    "url": "http://localhost"
  }'
```

Pobieranie skróconego URL

Dla pobrania skrócenego URL `shrt`

```bash
curl -i -X GET http://localhost:8000/api/shrt/
```
