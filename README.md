# transaction-webhook

This Django project provides a small webhook API for creating and retrieving transaction records.

The repository layout (relevant files):

- `manage.py` - Django entrypoint
- `webhook/settings.py` - Django settings
- `webhook/urls.py` - root URL config (mounts the API at `/api/v1/webhooks/`)
- `transaction_api/` - app with models, serializers, views and urls

This README explains how to run the project locally on Windows (PowerShell).

Prerequisites
- Python 3.8+ installed and on PATH
- Git (optional)

Quick local setup (PowerShell)

1. Open PowerShell and cd to the project root (where `manage.py` lives):

```powershell
cd D:\CodePlayGround\django-project\Webhook
```

2. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If you hit an execution policy error when activating, run (once) as Administrator:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

3. Install dependencies

If the repository includes a `requirements.txt` file, install from it:

```powershell
pip install -r requirements.txt
```

If there is no `requirements.txt`, install the essentials:

```powershell
pip install django djangorestframework
```

4. Create and apply migrations (SQLite database is used by default)

```powershell
python manage.py makemigrations
python manage.py migrate
```

5. (Optional) Create a superuser to access Django admin:

```powershell
python manage.py createsuperuser
```

6. Run the development server:

```powershell
python manage.py runserver
```

By default the server will be available at `http://127.0.0.1:8000/`.

API endpoints

This project mounts `transaction_api.urls` at `/api/v1/webhooks/` (see `webhook/urls.py`). The endpoints in `transaction_api/urls.py` are:

- `GET  /api/v1/webhooks/healthcheck/` — returns a health message and current time
- `POST /api/v1/webhooks/transactions/` — create a transaction via webhook (JSON body)
- `GET  /api/v1/webhooks/transactions/<transaction_id>/` — retrieve a transaction by its `transaction_id`

Example requests (PowerShell / curl)

Healthcheck:
```powershell
curl -i http://127.0.0.1:8000/api/v1/webhooks/healthcheck/
```

Create transaction (example JSON body):
```powershell
curl -X POST http://127.0.0.1:8000/api/v1/webhooks/transactions/ -H "Content-Type: application/json" -d '{
	"transaction_id": "tx123",
	"source_account": "acctA",
	"destination_account": "acctB",
	"amount": "100.00",
	"currency": "USD"
}'
```

Get transaction by id:
```powershell
curl http://127.0.0.1:8000/api/v1/webhooks/transactions/tx123/
```

Notes
- The `Transaction` model sets `status` default to `PROCESSING` and `created_at` uses `auto_now_add=True` so you don't need to pass those fields when creating a transaction.
- If you change models, run `makemigrations` and `migrate` again.
- For production deployment, use a production-ready server and a proper database. Do not use the dev server.

Troubleshooting
- 404 on endpoints: confirm the API prefix in `webhook/urls.py` (this README assumes `/api/v1/webhooks/`).
- Import errors: ensure the virtual environment is activated and dependencies are installed.

Want me to:
- Add a `requirements.txt` generated from your current environment?
- Add example unit tests or a Postman collection for the API?

---
Updated README to include local run instructions and API examples.
