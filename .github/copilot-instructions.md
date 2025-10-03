# Copilot instructions for Toñin Masajes repository

These notes are for automated coding agents (Copilot-style) to be immediately productive in this repo. Stay concise and concrete. Use only discoverable patterns; do not introduce new architectural choices without human approval.

Project at-a-glance
- Simple Flask web application. Backend code lives under `backend/`. Frontend templates under `frontend/templates/` and static assets under `static/`.
- Main app entry: `backend/app.py` — creates a Flask `app`, initializes SQLAlchemy (`models.db`), registers the `main` blueprint from `backend/routes.py`, and exposes `/` JSON health endpoint.
- Database models: `backend/models.py` — SQLAlchemy models: `Users`, `Therapists`, `MasterServices`, `Services`. Passwords are hashed via SQLAlchemy `before_insert`/`before_update` event listener.
- Routes: `backend/routes.py` — Blueprint `main` mounted at `/api`. Contains REST endpoints for `Users` (GET/POST/PUT/DELETE). Patterns are straightforward: `request.get_json()`, `serialize()` helpers on models, `db.session` for commits.
- Config: `backend/config.py` — `Config` class contains production-oriented values (MySQL URI, JWT secret). Note: `backend/app.py` currently overrides DB config and uses SQLite `mydatabase.db` and enables CORS.

What to change and how to run
- Running locally: `python backend/app.py` (app runs with `debug=True`). The code uses the sqlite URI defined in `backend/app.py`, not the `Config` class.
- If updating config, prefer changing `backend/app.py` to read from `backend/config.py` or env vars (file currently sets `app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'`).

Coding patterns and conventions
- Models include a `serialize()` method that returns a JSON-safe dict. Use these for API responses (e.g., `return jsonify([u.serialize() for u in users])`).
- Password hashing is handled by SQLAlchemy event listeners: when setting `Users.password`, assign the plaintext and let the event handler hash it before insert/update. Tests or patches that bypass model events must take care to hash passwords.
- Blueprints: `main = Blueprint('main', __name__)` in `backend/routes.py`. All API endpoints are under the `/api` prefix as registered in `backend/app.py`.
- Database migrations are not present. Schema changes require manual `db.create_all()` (already called in `backend/app.py` within app context) or adding a migration workflow (Alembic) if desired.

Files to reference when editing
- `backend/app.py` — startup, DB initialization, blueprint registration
- `backend/models.py` — data models and serialization
- `backend/routes.py` — API endpoints and request/response conventions
- `backend/config.py` — canonical place for production config values (MySQL URL, JWT key). Note mismatch with `app.py`.
- `frontend/templates/index.html` — example template referencing static assets via `url_for('static', filename='...')`.

Integration and external dependencies
- Uses Flask, Flask-CORS, Flask-SQLAlchemy, Flask-Bcrypt (password helpers), and SQLAlchemy events. The project expects a Python environment with these installed.
- `backend/config.py` suggests intended production DB: `mysql+pymysql://usuario:password@localhost/centro_masajes`. If implementing CI or deployments, use env vars and do not commit credentials.

Guidance for common tasks (concrete)
- Add a new API resource: add model in `backend/models.py` with `serialize()`, create routes in `backend/routes.py` under `main` blueprint, import model into `routes.py`, and use `db.session.add(...); db.session.commit()`.
- Update DB connection for production: modify `backend/app.py` to load `app.config.from_object('backend.config.Config')` or from env vars before `db.init_app(app)`.
- Seed data: create a short script that imports `backend.app` app context and uses `db.session.add(...)` then `db.session.commit()`; or run ad-hoc from REPL within `flask` app context.

Examples from repo
- Creating a user (in `backend/routes.py`): POST `/api/users` expects JSON with `name`, `email`, `password`. Duplicate emails return 400 with message `"El email ya está registrado"`.
- Model password hashing (in `backend/models.py`): assigning `user.password = 'plain'` will be hashed by `hash_user_password` listener before insert/update.

Don'ts for automated edits
- Do not insert secrets into `backend/config.py` or commit them. Prefer reading from environment variables.
- Don't assume a migration tool; modifying models may require manual DB reset or adding Alembic migrations.

If anything is unclear
- Ask which DB should be authoritative (SQLite used for local dev vs MySQL hinted in `config.py`).
- Ask whether you should wire `Config` into `app.py` or keep the current sqlite local-dev approach.

Please review and tell me if you want additional examples (e.g., adding a Therapist endpoint) or to wire config/environment variable usage.