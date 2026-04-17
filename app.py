from flask import Flask, render_template, request, redirect, abort, session, g
from werkzeug.security import check_password_hash
from database.db import get_db, init_db, seed_db, register_user, get_user_by_email

app = Flask(__name__)
app.secret_key = "spendly-dev-secret-key-change-in-production"


# ------------------------------------------------------------------ #
# Routes                                                              #
# ------------------------------------------------------------------ #

def logged_in_user():
    """Return the current user_id from session, or None if not logged in."""
    return session.get("user_id")


@app.before_request
def set_current_user():
    g.user_id = logged_in_user()


@app.teardown_request
def clear_current_user(exception=None):
    g.pop("user_id", None)


@app.route("/")
def landing():
    return render_template("landing.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if logged_in_user():
        return redirect("/")

    if request.method == "GET":
        return render_template("register.html")

    # POST — handle registration
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")

    if not name or not email or not password:
        return render_template("register.html", error="All fields are required.")

    if len(password) < 8:
        return render_template("register.html", error="Password must be at least 8 characters.")

    user_id = register_user(name, email, password)

    if user_id is None:
        return render_template("register.html", error="Email already registered.")

    return redirect("/login")


@app.route("/login", methods=["GET", "POST"])
def login():
    if logged_in_user():
        return redirect("/")

    if request.method == "GET":
        return render_template("login.html")

    # POST
    email = request.form.get("email", "").strip().lower()
    password = request.form.get("password", "")

    if not email or not password:
        return render_template("login.html", error="Email and password are required.")

    user = get_user_by_email(email)
    if user is None:
        return render_template("login.html", error="Invalid email or password.")

    if not check_password_hash(user["password_hash"], password):
        return render_template("login.html", error="Invalid email or password.")

    session["user_id"] = user["id"]
    return redirect("/profile")


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/privacy")
def privacy():
    return render_template("privacy.html")


# ------------------------------------------------------------------ #
# Placeholder routes — students will implement these                  #
# ------------------------------------------------------------------ #

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


@app.route("/profile")
def profile():
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("login"))

    context = {
        "user": {
            "name": "Aria Novak",
            "email": "aria.novak@example.com",
            "initials": "AN",
            "member_since": "January 2024",
        },
        "stats": {
            "total_spent": 3847.50,
            "transaction_count": 42,
            "top_category": "Bills",
        },
        "transactions": [
            {"date": "Apr 14, 2026", "description": "Electricity bill",       "category": "Bills",         "amount": 120.00},
            {"date": "Apr 10, 2026", "description": "Whole Foods groceries",  "category": "Food",          "amount": 67.40},
            {"date": "Apr 8, 2026",  "description": "Netflix subscription",   "category": "Entertainment", "amount": 15.99},
            {"date": "Apr 5, 2026",  "description": "Uber ride",             "category": "Transport",     "amount": 22.50},
            {"date": "Apr 2, 2026",  "description": "Gym membership",        "category": "Health",       "amount": 45.00},
        ],
        "categories": [
            {"name": "Bills",         "amount": 420.00, "pct": 55},
            {"name": "Food",          "amount": 380.00, "pct": 40},
            {"name": "Transport",     "amount": 150.00, "pct": 20},
            {"name": "Entertainment", "amount": 80.00,  "pct": 12},
            {"name": "Health",        "amount": 45.00,  "pct": 8},
        ],
    }
    return render_template("profile.html", **context)


@app.route("/expenses/add")
def add_expense():
    return "Add expense — coming in Step 7"


@app.route("/expenses/<int:id>/edit")
def edit_expense(id):
    return "Edit expense — coming in Step 8"


@app.route("/expenses/<int:id>/delete")
def delete_expense(id):
    return "Delete expense — coming in Step 9"


if __name__ == "__main__":
    with app.app_context():
        init_db()
        seed_db()
    app.run(debug=True, port=5001)
