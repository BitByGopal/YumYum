# 🍔 YumYum — Food Delivery Web App

> A full-stack food delivery platform built with Django, featuring multi-restaurant ordering, real-time order tracking, and integrated payment flow.

![Python](https://img.shields.io/badge/Python-3.11-blue?style=flat-square&logo=python)
![Django](https://img.shields.io/badge/Django-4.2-green?style=flat-square&logo=django)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-3.0-38bdf8?style=flat-square&logo=tailwindcss)
![SQLite](https://img.shields.io/badge/Database-SQLite-lightgrey?style=flat-square&logo=sqlite)
![Status](https://img.shields.io/badge/Status-Live-success?style=flat-square)

## 🌐 Live Demo
**[yumyum-app.up.railway.app](https://web-production-58c6.up.railway.app/)**

> **Demo Credentials**
> - Customer: `demo_user` / `demo1234`
> - Restaurant Owner: `demo_restaurant` / `demo1234`

---

## ✨ Features

### Customer Side
- 🔍 Search and filter restaurants by category (Biryani, Pizza, Burger, etc.)
- 🛒 Add to cart with quantity controls
- 🏪 Multi-restaurant aware cart (prevents mixing orders)
- 💳 Payment flow with UPI, Card, and Netbanking support
- 📦 Real-time order status tracking (Pending → Accepted → Preparing → Delivered)
- 👤 User authentication with role-based access

### Restaurant Owner Side
- 🍴 Restaurant dashboard to manage incoming orders
- ✅ One-click order status updates
- 📋 View itemized order details per customer

### Technical Highlights
- 🔒 Login-protected routes with `@login_required`
- 🛡️ CSRF protection on all forms
- 🖼️ Media file handling for restaurant and food images
- 📱 Fully responsive UI (mobile + desktop)
- ⚡ Clean URL routing across 3 Django apps

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 4.2 (Python 3.11) |
| Frontend | HTML5, Tailwind CSS, Vanilla JS |
| Database | SQLite (dev) → PostgreSQL (prod) |
| Auth | Django Custom User Model |
| Hosting | Railway |
| Media | Django Media Files |

---

## 📁 Project Structure

```
YumYum/
├── accounts/          # Custom User model (customer / restaurant roles)
├── restaurants/       # Restaurant & FoodItem models, home + menu views
├── orders/            # Cart, CartItem, Order, OrderItem models + payment
├── templates/         # All HTML templates (Tailwind-based)
├── static/            # CSS and JS assets
├── media/             # Uploaded restaurant & food images
└── YumYum/            # Project settings, main urls.py
```

---

## ⚙️ Local Setup

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/yumyum.git
cd yumyum/YumYum

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run migrations
python manage.py migrate

# 5. Create superuser (for admin panel)
python manage.py createsuperuser

# 6. Start server
python manage.py runserver
```

Visit `http://127.0.0.1:8000` 🎉

---

## 🗃️ Database Models

```
User (accounts)
 └── role: customer | restaurant

Restaurant (restaurants)
 ├── owner → User
 ├── category, rating, delivery_time
 └── image

FoodItem (restaurants)
 └── restaurant → Restaurant

Cart + CartItem (orders)
 └── user → User, food_item → FoodItem

Order + OrderItem (orders)
 ├── user → User, restaurant → Restaurant
 ├── status: pending | accepted | preparing | delivered
 └── is_paid, payment_id
```

---

## 🚀 Deployment (Railway)

This app is deployed on [Railway](https://railway.app):

1. Pushed to GitHub
2. Connected Railway to GitHub repo
3. Added `Procfile`, `requirements.txt`, `runtime.txt`
4. Set environment variables on Railway dashboard
5. Auto-deploys on every `git push`

---

## 📸 Screenshots

> *(Add screenshots of Home, Menu, Cart, Payment, Orders pages here)*

---

## 👨‍💻 Author

**Prince Gopal Yadav**
- 3rd Year BTech CSE (AI & ML) — LPU
- Frontend Developer Intern @ 1Stop.AI
- [GitHub](https://github.com/YOUR_USERNAME) · [LinkedIn](https://linkedin.com/in/YOUR_PROFILE)

---

## 📄 License

MIT License — feel free to use this project for learning purposes.
