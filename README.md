# Internship & Placement Management System

A web application built to help college students discover internship and placement opportunities, apply to them, and track their application status — while giving admins a simple dashboard to post opportunities and manage applicants.

This project was built as a 1-month college minor project by a team of 3, with a focus on learning proper full-stack development practices (clean separation of frontend/backend, a real database, Git collaboration) without overengineering for the project's scope.

## Features

- Student registration and login
- Admin login
- Student profile management
- Internship and placement listings
- Search and filter opportunities
- Apply for internships
- Application status tracking
- Admin CRUD operations on listings
- Student dashboard
- Admin dashboard

## Tech Stack

**Frontend:** HTML, CSS, JavaScript (vanilla, no framework)

**Backend:** Python, Flask

**Database:** SQLite

**Tools:** Git, GitHub, VS Code, Postman, DB Browser for SQLite

## Project Structure

```
internship-management-system/
│
├── frontend/
│   ├── pages/          # HTML pages, one per screen
│   ├── css/             # Stylesheets
│   ├── js/               # JavaScript, one file per feature area
│   └── assets/          # Images, icons
│
├── backend/
│   ├── app.py            # Flask entry point
│   ├── config.py         # App configuration
│   ├── routes/           # API route definitions
│   ├── services/         # Business logic
│   ├── models/           # Database queries
│   └── database/
│       ├── schema.sql    # Table definitions
│       └── internship.db # SQLite database file (not tracked in Git)
│
├── docs/
│   └── api_docs.md       # API endpoint documentation
│
├── .gitignore
├── requirements.txt
└── README.md
```

## Architecture

```
User → Frontend (HTML/CSS/JS) → Flask Routes → Business Logic (Services) → Database Layer (Models) → SQLite
```

The frontend never talks to the database directly — it only communicates with Flask through HTTP requests (JSON). Routes stay thin and simply call service functions; services hold the actual logic; models are the only layer that runs SQL queries.

## Getting Started

### Prerequisites

- Python 3.x installed
- Git installed
- A code editor (VS Code recommended)

### Setup (first time only)

> Run all commands below from the project's root folder (`internship-management-system`).

1. Clone the repo:
```
   git clone <repo-url>
   cd internship-management-system
```
2. Create a virtual environment:
```
   python -m venv venv
```
3. Activate it:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies:
```
   pip install -r requirements.txt
```
5. Initialize the database:
```
   python backend\models\db.py
```
6. Run the server:
```
   python backend\app.py
```
7. Open `http://127.0.0.1:5000` in your browser.

### Running it again later

You only need to repeat steps 3, 6, and 7 above — activate the virtual environment, run the server, open the browser. No need to reinstall dependencies or reinitialize the database unless `requirements.txt` or `schema.sql` changed.

## Team & Responsibilities

| Name | Role | Owns |
|---|---|---|
| Ansh | Backend, database, integration | `app.py`, `config.py`, `models/`, `database/schema.sql`, auth & internship routes/services |
| Alok | Backend/database support | Application & placement routes/services/models |
| Divya | Frontend | Everything in `frontend/` |

Shared files (`docs/api_docs.md`, `README.md`, `.gitignore`, `requirements.txt`) should only be edited after a quick heads-up to the team, since they're the highest conflict-risk files.

## Git Workflow

- `main` is always kept in a working state — nobody pushes directly to it (except initial setup).
- Create a feature branch for any change: `feature/<area>-<short-description>`, e.g. `feature/backend-application-api`, `feature/frontend-login-page`.
- Push your branch and open a Pull Request.
- Get at least one teammate to review before merging into `main`.
- After merging, everyone runs `git pull` to stay in sync.

## API Documentation

See [`docs/api_docs.md`](./docs/api_docs.md) for the full list of endpoints, request/response formats, and which frontend page calls each one.

## Database Schema

See [`backend/database/schema.sql`](./backend/database/schema.sql) for table definitions. Core tables: `users`, `students`, `internships`, `applications`.

## Scope Notes

This project intentionally uses Flask's built-in session-based authentication instead of JWT, and SQLite instead of a heavier database like PostgreSQL — appropriate choices for a single-server, 1-month college project. Docker, CI/CD, and cloud deployment were considered out of scope.

## License

Built for academic/educational purposes as part of a college minor project.