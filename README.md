# Spendly - Personal Expense Tracker

A clean, modern personal expense tracking web application built with Python Flask. Track your daily expenses, understand spending patterns, and take control of your financial life — one transaction at a time.

![Spendly](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![Flask](https://img.shields.io/badge/flask-3.1.3-lightgrey)
![License](https://img.shields.io/badge/license-MIT-orange)

## Features

- **Log Expenses Instantly** - Add any expense in seconds with category, amount, date, and description
- **Understand Your Patterns** - See exactly where your money goes with category breakdowns and monthly summaries
- **Filter by Time Period** - View spending for any date range — last week, last month, or a custom period
- **Beautiful UI** - Clean, responsive design with modern aesthetics
- **Currency Support** - Built for Indian Rupee (₹)

## Tech Stack

| Component | Technology                               |
| --------- | ---------------------------------------- |
| Backend   | Python Flask 3.1.3                       |
| WSGI      | Werkzeug 3.1.6                           |
| Database  | SQLite                                   |
| Testing   | pytest 8.3.5, pytest-flask 1.3.0         |
| Frontend  | HTML5, CSS3, Vanilla JavaScript          |
| Fonts     | DM Serif Display, DM Sans (Google Fonts) |

## Project Structure

```
expense-tracker/
├── app.py                      # Main Flask application with routes
├── requirements.txt            # Python dependencies
├── .gitignore                  # Git ignore patterns
├── README.md                   # Project documentation
├── database/
│   ├── __init__.py             # Package initializer
│   └── db.py                   # Database utilities (SQLite connection, init, seed)
├── templates/
│   ├── base.html               # Base Jinja2 template with navbar/footer
│   ├── landing.html            # Landing/home page
│   ├── register.html           # User registration page
│   └── login.html              # User login page
├── static/
│   ├── css/
│   │   └── landing.css           # Complete styling (~530 lines)
│   └── js/
│       └── main.js             # Client-side JavaScript
└── tests/                      # Pytest test suite (to implement)
```

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd expense-tracker
   ```

2. **Create a virtual environment**

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   python app.py
   ```

5. **Open in browser**
   Navigate to `http://localhost:5001`

## Routes

| Route                   | Method    | Description       | Status       |
| ----------------------- | --------- | ----------------- | ------------ |
| `/`                     | GET       | Landing page      | Implemented  |
| `/register`             | GET, POST | User registration | UI Complete  |
| `/login`                | GET, POST | User login        | UI Complete  |
| `/logout`               | GET       | User logout       | To Implement |
| `/profile`              | GET       | User profile      | To Implement |
| `/expenses/add`         | GET, POST | Add new expense   | To Implement |
| `/expenses/<id>/edit`   | GET, POST | Edit expense      | To Implement |
| `/expenses/<id>/delete` | POST      | Delete expense    | To Implement |

## Database Schema (Planned)

The application uses SQLite for data persistence. The following tables are planned:

### Users

| Column        | Type    | Description          |
| ------------- | ------- | -------------------- |
| id            | INTEGER | Primary key          |
| name          | TEXT    | User's full name     |
| email         | TEXT    | Unique email address |
| password_hash | TEXT    | Hashed password      |

### Expenses

| Column      | Type    | Description                                             |
| ----------- | ------- | ------------------------------------------------------- |
| id          | INTEGER | Primary key                                             |
| user_id     | INTEGER | Foreign key to Users                                    |
| category    | TEXT    | Expense category (Bills, Food, Health, Transport, etc.) |
| amount      | REAL    | Amount in Rupees                                        |
| date        | DATE    | Transaction date                                        |
| description | TEXT    | Optional description                                    |

## Configuration

The application runs with the following defaults:

- **Debug Mode**: Enabled (for development)
- **Port**: 5001
- **Database**: `expense_tracker.db` (SQLite file)

### Environment Variables

Create a `.env` file for sensitive configuration:

```env
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///expense_tracker.db
```

## Testing

Run the test suite with pytest:

```bash
pytest
```

## Development

### Running in Production

For production deployment:

1. Disable debug mode in `app.py`
2. Use a production WSGI server like Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5001 app:app
   ```

### Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## Roadmap

- [ ] Complete user authentication (register/login/logout)
- [ ] Implement expense CRUD operations
- [ ] Add category spending visualizations
- [ ] Monthly spending summaries
- [ ] Custom date range filtering
- [ ] Export data to CSV
- [ ] Dark mode support

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [Flask](https://flask.palletsprojects.com/)
- Fonts by [Google Fonts](https://fonts.google.com/)
- Styled with custom CSS using CSS variables and responsive design

---

**Spendly** - Know where your money goes.
