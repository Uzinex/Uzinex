# Uzinex Freelance Backend

Backend MVP marketplace for clients and freelancers built with Django REST Framework.

## Requirements
- Python 3.12
- PostgreSQL 16

## Local setup
```bash
cp .env.example .env  # adjust values
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_demo  # optional demo data
python manage.py runserver
```
Visit http://localhost:8000/api/docs/ for Swagger UI and http://localhost:8000/admin/ for admin panel.

## Docker
```bash
docker-compose up --build
```
Application will be available at http://localhost:8000/api/docs/.

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
