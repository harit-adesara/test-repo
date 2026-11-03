# Task Manager API (self-healing CI/CD test project)

Flask + SQLite backend: auth (token based), users, tasks (CRUD, filtering, pagination).

    pip install -r requirements.txt
    flake8 app tests
    pytest -v

CI runs on GitHub Actions: `.github/workflows/ci.yml` (install -> lint -> test).
test
