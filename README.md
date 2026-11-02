# Shorty

## Struktura 

`config` - konfiguracja Django
`config/settings/` - ustawienia dla dev/prod
`mappings` - modele skracania URL
`api` - interfejs API

## Instalacja 

Konfiguracja środowiska
```bash
cp .env.example .env
```

Generowanie SECRET_KEY
```bash
uv run python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Uruchomienie
```bash
uv sync --dev
uv run --env-file .env src/manage.py migrate
uv run --env-file .env src/manage.py runserver
```

## Testowanie 

```bash
uv run --env-file .env src/manage.py test src
```

## Obsługa ręczna API

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

Dla pobrania skrócenego URL `shrtshrt`

```bash
curl -i -X GET http://localhost:8000/api/shrtshrt/
```
