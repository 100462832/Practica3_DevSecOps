# NovaCorp — Company Management Platform

**NovaCorp Platform** is an internal web application for managing companies and their associated comments. It supports three roles (`admin`, `owner`, `user`) with different access levels.

---

## Installation and how to run

Use a Python environment and install the required dependencies:

```bash
pip install -r requirements.txt
```

Run main.py to start the application.

```bash
python main.py
```

Visit: `http://127.0.0.1:5000`

The database is automatically initialized on first run.

To restore the database, delete the files db/data.db and db/users.db then run main.py.

---

## Default Users

| Username | Password   | Role   | Notes                      |
|----------|------------|--------|----------------------------|
| `alice`  | password1  | user   | Standard employee          |
| `bob`    | password2  | owner  | Owns "Insegura Corp"       |
| `admin`  | admin123   | admin  | Full access                |

---

## Project Structure

```
.
├── main.py                 # Entry point
├── server.py               # Flask app configuration
├── db/
│   └── __init__.py         # Database initialization and helpers
├── routes/
│   ├── auth.py             # Login/logout
│   ├── companies.py        # Company views, dashboard, search
│   ├── companies_admin.py  # Admin company management
│   ├── users_admin.py      # Admin user management
│   └── profile.py          # User profiles
├── templates/
│   ├── base.html           # Shared layout
│   ├── dashboard.html      # Main dashboard
│   ├── auth/               # Login page
│   ├── companies/          # Company pages
│   ├── admin/              # Admin panels
│   ├── profile/            # User profile pages
│   └── errors/             # 404, 403 pages
├── static/
│   └── css/style.css       # Custom styles
└── requirements.txt
```

---

## Technologies

- Python 3 + Flask
- SQLite
- Bootstrap 5.3
- Jinja2 + Bootstrap Icons

## Integración de análisis de seguridad en CI/CD

Se ha implementado un pipeline de seguridad mediante GitHub Actions en el archivo `.github/workflows/security.yml`.

El pipeline se ejecuta automáticamente en cada `push` a la rama `main`, así como en cada `pull_request`.

El flujo realiza las siguientes acciones:

1. Descarga el código del repositorio mediante `actions/checkout`.
2. Prepara un entorno Python con `actions/setup-python`.
3. Instala las dependencias del proyecto desde `requirements.txt`.
4. Instala las herramientas de seguridad Semgrep y pip-audit.
5. Ejecuta un análisis SAST con Semgrep.
6. Ejecuta un análisis SCA con pip-audit.
7. Muestra los resultados en los logs de GitHub Actions.

### SAST con Semgrep

Se ha seleccionado Semgrep como herramienta SAST porque permite analizar estáticamente el código fuente de la aplicación Flask y detectar patrones inseguros, como consultas SQL inseguras, uso incorrecto de datos de entrada o configuraciones débiles.

### SCA con pip-audit

Se ha seleccionado pip-audit como herramienta SCA porque permite analizar las dependencias Python declaradas en `requirements.txt` y detectar versiones con vulnerabilidades conocidas.

### Estrategia de fallo del pipeline

El pipeline está configurado para fallar cuando Semgrep o pip-audit detectan hallazgos relevantes. Esta decisión permite bloquear cambios inseguros antes de que lleguen a la rama principal.