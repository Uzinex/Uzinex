# Uzinex Freelance Backend

Backend MVP marketplace for clients and freelancers built with Django REST Framework.

## Requirements
- Python 3.12

## Local setup

### Вариант A (SQLite, без настроек БД)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # оставить DATABASE_URL закомментированным
python manage.py migrate
python manage.py runserver
```

### Вариант B (Docker Postgres)

```bash
docker compose up -d
cp .env.example .env
# в .env раскомментировать DATABASE_URL=postgres://uzinex:uzinexpass@127.0.0.1:5432/uzinex
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### Проверка

```bash
python manage.py check
python - <<<'from django.conf import settings; print(settings.DATABASES["default"]["ENGINE"])'
```

Visit http://localhost:8000/api/docs/ for Swagger UI and http://localhost:8000/admin/ for admin panel.

## Sample requests
```bash
# register user
curl -X POST http://localhost:8000/api/auth/register/ \
  -H 'Content-Type: application/json' \
  -d '{"username":"client1","email":"c1@x.com","password":"password123","role":"client"}'

# obtain token
curl -X POST http://localhost:8000/api/auth/token/ \
  -H 'Content-Type: application/json' \
  -d '{"username":"client1","password":"password123"}'

# create project (use JWT token)
curl -X POST http://localhost:8000/api/marketplace/projects/ \
  -H 'Authorization: Bearer <token>' \
  -H 'Content-Type: application/json' \
  -d '{"title":"Landing","description":"React SPA","skills":["React","UI"],"budget_min":300,"budget_max":800}'

# create proposal
curl -X POST http://localhost:8000/api/marketplace/proposals/ \
  -H 'Authorization: Bearer <token>' \
  -H 'Content-Type: application/json' \
  -d '{"project":1,"cover_letter":"Готов сделать","bid_amount":500,"eta_days":10}'
```

## SSR Pages & Static

HTML templates live in `templates/` and static assets in `static/`.

Collect static files for production:

```bash
python manage.py collectstatic --noinput
```

To add a new server-rendered page:

1. Create a template inside `templates/pages/`.
2. Add a corresponding class-based view and URL pattern.

