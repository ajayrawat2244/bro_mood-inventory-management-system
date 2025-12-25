## Run locally (quick)
1. Clone:
   `git clone https://github.com/ajayrawat2244/bro_mood-inventory-management-system.git`
2. Create venv:
   `python -m venv venv && source venv/bin/activate` (Windows: `venv\Scripts\activate`)
3. Install:
   `pip install -r requirements.txt`
4. Setup DB (MySQL):
   - create database `inventory_db`
   - update `bro_mood_inventory_system/settings.py` `DATABASES` with credentials (or use sqlite for quick test)
5. Migrate & create superuser:
   `python manage.py migrate`
   `python manage.py createsuperuser`
6. Run:
   `python manage.py runserver`
7. API docs / endpoints:
   - `GET /api/products/` — list products
   - `POST /api/orders/` — place order
8. Notes:
   - Remove `SECRET_KEY` from settings before sharing. Use environment variables in production.
