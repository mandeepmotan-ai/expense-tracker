# Spec: Registration

## Overview

Implement user registration for Spendly. Users can create an account with a name, email, and password. The form validates uniqueness of email and hashes passwords before storing them. On success, the user is redirected to the login page.

## Depends on

Step 1 (Database Setup) — the `users` table must exist before this feature works.

---

## Routes

### Existing route to modify

- `GET /register` — renders `register.html` (already implemented, no change needed)
- `POST /register` — handles form submission — **public access**

---

## Database Changes

None — the `users` table was created in Step 1.

### New function to add in `database/db.py`

#### `register_user(name, email, password)`

- Accepts `name`, `email`, and plain `password`
- Hashes the password using `werkzeug.security.generate_password_hash`
- Inserts into `users` table
- Returns `user_id` (int) on success
- Returns `None` on `UNIQUE` constraint failure (duplicate email)
- Uses parameterized query only

---

## Templates

### Modify: `templates/register.html`

- The template already exists with a correct form structure
- No structural changes needed
- Ensure the template renders an `{{ error }}` variable if passed from the route

---

## Files to Change

- `app.py` — add POST handler for `/register`
- `database/db.py` — add `register_user()` function

---

## Files to Create

None.

---

## New Dependencies

No new pip packages. Uses:
- `werkzeug.security.generate_password_hash` (already in `requirements.txt`)

---

## Rules for Implementation

- **No SQLAlchemy or ORMs**
- **Parameterised queries only** — never use f-strings or concatenation in SQL
- **Passwords must be hashed** with `werkzeug.security.generate_password_hash`
- All routes in `app.py` — no blueprints
- All DB logic in `database/db.py` — never inline in routes
- Use `abort(400)` or `abort(409)` for error cases, not bare string returns
- After successful registration, redirect to `/login` with a success message

---

## Definition of Done

- [ ] `POST /register` with valid data creates a new user in the database
- [ ] `POST /register` with duplicate email shows error message on the form
- [ ] Password is hashed before storage (not stored in plain text)
- [ ] Successful registration redirects to `/login`
- [ ] `register_user()` function exists in `database/db.py`
- [ ] Route uses `abort()` for HTTP errors, not string returns
- [ ] All DB queries use parameterized `?` placeholders
