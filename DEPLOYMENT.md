# Django Deployment Guide - Free Hosting Options

Your Django project can be deployed for **FREE** on multiple platforms. Choose one below:

---

## Option 1: **Render.com** ⭐ (RECOMMENDED - Easiest)

### Why Render?
- ✅ **Completely Free** - No credit card needed
- ✅ **Auto-deploy** from GitHub
- ✅ **Free PostgreSQL database**
- ✅ **Free SSL certificate**
- ✅ **Easy to use**

### Step-by-Step:

#### 1. Initialize Git Repository
```bash
cd C:\Users\Ajay kumar thakur\projects\my_program
git init
git add .
git commit -m "Initial commit"
```

#### 2. Push to GitHub
```bash
# Create a new repo on GitHub.com (name: my-auth-project)
git remote add origin https://github.com/YOUR_USERNAME/my-auth-project.git
git branch -M main
git push -u origin main
```

#### 3. Create Render Account
- Go to [render.com](https://render.com)
- Sign up with GitHub account
- Click "New +" → "Web Service"
- Connect your GitHub repository
- Select: `my-auth-project`

#### 4. Configure on Render
- **Name**: `my-auth-project`
- **Environment**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn my_program.wsgi:application`

#### 5. Add Environment Variables
- Click "Environment"
- Add these variables:
  - `DEBUG` = `False`
  - `SECRET_KEY` = (generate new one: https://djecrety.ir/)
  - `DATABASE_URL` = (auto-provided by Render)

#### 6. Deploy
- Click "Deploy"
- Wait 2-3 minutes
- Your site will be live at: `https://my-auth-project.onrender.com`

**Cost**: FREE forever ✅

---

## Option 2: **Railway.app** (Simple & Fast)

### Why Railway?
- ✅ **$5/month free credit** (usually lasts 6 months+)
- ✅ **Automatic GitHub deployment**
- ✅ **PostgreSQL included**
- ✅ **Simple dashboard**

### Step-by-Step:

#### 1. Push Code to GitHub (same as above)

#### 2. Create Railway Account
- Go to [railway.app](https://railway.app)
- Sign up with GitHub
- Click "New Project" → "Deploy from GitHub repo"
- Select your repository

#### 3. Configure
- Railway auto-detects Django
- Add environment variables:
  - `DEBUG` = `False`
  - `SECRET_KEY` = (new key from djecrety.ir)

#### 4. Deploy
- Click "Deploy"
- Your app is live!

**Cost**: FREE tier (or use $5 free credit)

---

## Option 3: **PythonAnywhere** (Python-Specific)

### Why PythonAnywhere?
- ✅ **Free tier available**
- ✅ **Built for Python/Django**
- ✅ **Web-based file editor**
- ✅ **No credit card needed**

### Step-by-Step:

#### 1. Create Account
- Go to [pythonanywhere.com](https://www.pythonanywhere.com)
- Sign up (free account)

#### 2. Upload Code
- Go to "Files"
- Upload your project folder or use Git
```bash
git clone https://github.com/YOUR_USERNAME/my-auth-project.git
```

#### 3. Create Web App
- Click "Web" → "Add a new web app"
- Choose "Python 3.12"
- Choose "Django"
- Point to your project: `/home/yourusername/my-auth-project`

#### 4. Configure WSGI
- Edit WSGI configuration file
- Point to: `my_program.wsgi`

#### 5. Reload
- Click "Reload" button
- Your app is live!

**Cost**: FREE forever (with limitations) ✅

---

## Comparison Table

| Feature | Render | Railway | PythonAnywhere |
|---------|--------|---------|----------------|
| **Cost** | Free ✅ | $5/mo | Free ✅ |
| **Database** | Free PostgreSQL | Free | Optional |
| **SSL** | Free ✅ | Free ✅ | Free ✅ |
| **Ease** | Very Easy | Easy | Medium |
| **Support** | Good | Excellent | Good |
| **Uptime** | 99.9% | 99.9% | 99% |

---

## Important: Update Your Project for Production

Your project already has these, but verify:

### 1. Install Production Dependencies
```bash
pip install gunicorn whitenoise psycopg2-binary
pip freeze > requirements.txt
```

### 2. Update settings.py (Already done ✅)
- DEBUG should use environment variable
- ALLOWED_HOSTS = ['*']
- SECRET_KEY should use environment variable

### 3. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 4. Test Locally
```bash
python manage.py runserver 0.0.0.0:8000
```

---

## Database Considerations

### For Free Tier:
- **SQLite** (current) works but limited to single process
- **PostgreSQL** (recommended for production):
  - Render: Free tier included
  - Railway: Included
  - PythonAnywhere: Optional ($5/month if needed)

### Switch to PostgreSQL:
```bash
pip install psycopg2-binary
```

Update `settings.py`:
```python
import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:///db.sqlite3',
        conn_max_age=600
    )
}
```

---

## Custom Domain (Optional)

All three platforms allow custom domains:
1. Buy domain from: GoDaddy, Namecheap, etc.
2. Add CNAME record pointing to your deployment platform
3. Enable HTTPS on your deployment platform

---

## Monitoring & Maintenance

### Monitor Your App:
- Render: Dashboard → Logs
- Railway: Dashboard → Logs
- PythonAnywhere: Web → View logs

### Keep Dependencies Updated:
```bash
pip list --outdated
pip install --upgrade package-name
```

### Database Backups:
- Render: Auto backups included
- Railway: Manual backup option
- PythonAnywhere: Use admin panel

---

## Troubleshooting

### Static Files Not Loading
- Run: `python manage.py collectstatic`
- Add to requirements.txt: `whitenoise`

### 500 Error
- Check logs: See "Monitoring" section above
- Common issue: DEBUG = False without proper configuration

### Database Connection Failed
- Verify DATABASE_URL environment variable is set
- Check database credentials
- Ensure migrations ran: `python manage.py migrate`

### Login Redirects to /admin
- Verify LOGIN_URL = 'login' in settings.py ✅ (Already set)

---

## Next Steps

1. **Choose platform** (Render recommended for ease)
2. **Push to GitHub**
3. **Connect to deployment platform**
4. **Add environment variables**
5. **Deploy and test!**

Your project is ready to deploy. Pick one platform above and follow the steps.

**Questions?** Check the platform's documentation or Django deployment guide.

---

**Important Security Notes:**
- ❌ Never commit `.env` files
- ✅ Use environment variables for secrets
- ✅ Generate new SECRET_KEY for production
- ✅ Set DEBUG = False in production
- ✅ Use HTTPS only

---

**Deployment Path:**
```
Local Development → GitHub → Deployment Platform → Live Website
```

Start with Render! It's the easiest. 🚀
