# Shivonix Technology & Consulting - Auth Project

A complete Django authentication system with signup, login, logout, and home page.

## Project Structure

```
my_program/
├── my_program/              # Main project
│   ├── settings.py          # Django settings
│   ├── urls.py              # Project URL routing
│   ├── views.py
│   └── wsgi.py
├── user/                    # User app
│   ├── models.py            # UserProfile model
│   ├── forms.py             # SignUpForm, LoginForm
│   ├── views.py             # signup, login, logout, home views
│   ├── urls.py              # User app URL routing
│   ├── migrations/
│   └── admin.py
├── templete/                # HTML templates
│   ├── signup.html          # Sign-up form
│   ├── login.html           # Login form
│   └── home.html            # Welcome page
├── manage.py                # Django management script
├── db.sqlite3               # SQLite database
├── test_setup.py            # Test script
└── venv/                    # Virtual environment
```

## Features

### 1. **Sign-Up Page** (`/signup/`)
- Fields: Username, Email, Contact Number (optional), Password, Confirm Password
- Password validation: Both passwords must match
- Error messages if passwords don't match
- Automatic login after successful signup
- Redirects to home page

### 2. **Login Page** (`/login/`)
- Fields: Email, Password
- Authenticates user by email
- Error message for invalid credentials
- "Forgot Password?" link (optional)
- Redirects to home page after successful login

### 3. **Home Page** (`/`)
- Displays: "Welcome to Shivonix Technology & Consulting"
- Shows: "Your trusted partner in innovative tech solutions"
- Displays logged-in username
- Logout button
- Protected route (requires login)

### 4. **Logout** (`/logout/`)
- Logs out the user
- Redirects to login page

## Setup Instructions

### 1. Install Python & Django
```bash
python --version  # Python 3.8+
pip install django
```

### 2. Virtual Environment (Already Set Up)
```bash
# Activate virtual environment
.\venv\Scripts\Activate.ps1   # Windows PowerShell
source venv/bin/activate       # macOS/Linux
```

### 3. Database Migrations (Already Applied)
```bash
python manage.py migrate
```

### 4. Run Development Server
```bash
python manage.py runserver
```
Server starts at `http://127.0.0.1:8000/`

## Usage Flow

### First-Time User (Sign-Up)
1. Visit `http://127.0.0.1:8000/signup/`
2. Enter: Username, Email, Password, Confirm Password (Contact # optional)
3. Passwords must match; error shown if they don't
4. Click "Sign Up"
5. Account created and auto-logged in
6. Redirected to home page

### Returning User (Login)
1. Visit `http://127.0.0.1:8000/login/`
2. Enter: Email, Password
3. Must use the email from signup
4. Click "Login"
5. Redirected to home page if successful
6. Error message if email/password invalid

### Home Page
1. After login, visit `http://127.0.0.1:8000/`
2. See welcome message with username
3. Click "Logout" to exit

## Database Models

### User (Django's Built-in)
- `username` - Unique username
- `email` - User's email address
- `password` - Hashed password

### UserProfile (Custom)
- `user` - OneToOneField to User
- `contact_number` - Optional contact number

## Forms

### SignUpForm
- Validates email uniqueness
- Validates password match
- Uses Django's built-in password field

### LoginForm
- Email and password fields
- Authentication via email

## URL Routing

| Route | View | Purpose |
|-------|------|---------|
| `/` | `home` | Welcome page (protected) |
| `/signup/` | `signup` | Sign-up form |
| `/login/` | `login_view` | Login form |
| `/logout/` | `logout_view` | Logout handler |

## Testing

### Create Test User
```bash
python test_setup.py
```
Creates user: `testuser` / `test@example.com` / `testpass123`

### Manual Testing
1. Sign up with new email
2. Logout
3. Login with email and password
4. Verify home page shows username
5. Click logout to confirm redirect to login

## Security Notes

- Passwords are hashed using Django's default PBKDF2
- CSRF protection enabled on all forms
- Login required for home page (`@login_required`)
- Secret key in settings (change in production)
- DEBUG = True (for development only)

## Future Enhancements

- [ ] Email verification on signup
- [ ] "Forgot Password" functionality
- [ ] Password reset via email
- [ ] User profile edit page
- [ ] Social login (Google, GitHub)
- [ ] Two-factor authentication
- [ ] Remember me checkbox
- [ ] Session timeout

## Production Checklist

Before deploying:
1. Set `DEBUG = False` in settings.py
2. Generate a new `SECRET_KEY`
3. Use environment variables for sensitive data
4. Use PostgreSQL instead of SQLite
5. Configure static files with whitenoise or CDN
6. Enable HTTPS
7. Set `ALLOWED_HOSTS` properly
8. Use a production WSGI server (Gunicorn, uWSGI)

## Troubleshooting

### Template not found error
- Ensure `TEMPLATES['DIRS']` includes `BASE_DIR / 'templete'`
- Check file names match exactly

### ModuleNotFoundError: No module named 'user.forms'
- Ensure `user/forms.py` exists
- Run: `python manage.py makemigrations`

### Password mismatch error
- Both password fields must match exactly
- Check for leading/trailing spaces

### Login doesn't work
- Verify email is correct (case-sensitive)
- Ensure you signed up with that email first
- Check password is correct

## Support

For issues or questions, contact the development team.

---

**Project**: Shivonix Technology & Consulting Authentication System  
**Built with**: Django 6.0.1 + Python 3.12  
**Last Updated**: January 20, 2026
