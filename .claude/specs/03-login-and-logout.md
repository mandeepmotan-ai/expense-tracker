# Spec: Login and Logout

## Overview

Implement user login and logout for Spendly. Users authenticate with email and password. On success, the session stores the logged-in user's ID. Logout clears the session. Only logged-in users can access protected routes.

## Depends on

Step 2 (Registration) — users must exist before they can log in.

---

## Routes

### New routes

- `GET /login` — renders `login.html` — **public access**
- `POST /login` — handles form submission — **public access**
- `GET /logout` — clears session, redirects to landing — **logged-in only**

---

## Database Changes

None.

### New function to add in `database/db.py`

#### `get_user_by_email(email)`

- Accepts `email` string
- Returns a `sqlite3.Row` with `id`, `name`, `email`, `password_hash` if found
- Returns `None` if no user matches
- Uses parameterized query only

---

## Templates

### Modify: `templates/login.html`

- Add a POST form with `email` and `password` fields
- Add a "Remember me" checkbox (optional, not stored)
- Display `{{ error }}` passed from the route on failed login
- Display `{{ success }}` passed from the route on redirect after logout
- Use `url_for()` for form action — no hardcoded URLs

---

## Files to Change

- `app.py` — add POST handler for `/login`, implement `/logout`
- `database/db.py` — add `get_user_by_email()` function

---

## Files to Create

None.

---

## New Dependencies

No new pip packages. Uses:
- `werkzeug.security.check_password_hash` (already in `requirements.txt`)

---

## Rules for Implementation

- **No SQLAlchemy or ORMs**
- **Parameterised queries only** — never use f-strings or concatenation in SQL
- **Passwords verified with `werkzeug.security.check_password_hash`**
- Use Flask `session` to store `user_id` after login
- All DB logic in `database/db.py` — never inline in routes
- Use `abort(401)` for invalid login, not bare string returns
- After successful login, redirect to `/dashboard` (stub for now, redirect to profile)
- After logout, redirect to `/` with a `success` message

---

## Definition of Done

- [ ] `GET /login` renders the login form
- [ ] `POST /login` with valid credentials sets `session['user_id']` and redirects
- [ ] `POST /login` with invalid credentials shows error on login page
- [ ] `GET /logout` clears the session and redirects to `/`
- [ ] `get_user_by_email()` exists in `database/db.py`
- [ ] Login form uses `url_for()` for action URL
- [ ] All templates extend `base.html`
- [ ] Error messages are displayed using Jinja2 `{{ error }}` variable