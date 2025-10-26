 🌐 SocialHub – A Django Social Media Platform

SocialHub is a mini social media web application built using **Django**, allowing users to **sign up, log in, post, like, and manage their profiles**.  
This project demonstrates user authentication, CRUD operations, static/media handling, and Django templating.

---

 🚀 Features

✅ User authentication (Signup, Login, Logout)  
✅ Create, edit, and delete posts  
✅ Like and unlike posts  
✅ User profile page with editable info  
✅ Responsive front-end with CSS  
✅ Media upload support for user posts  
✅ Secure access with Django’s authentication system  

---

## 🧱 Tech Stack

| Component | Technology |
|------------|-------------|
| Backend | Django 5.2.6 (Python 3.10) |
| Frontend | HTML, CSS, JavaScript |
| Database | SQLite3 |
| Authentication | Django Auth |
| Deployment Ready | ✅ (supports static + media setup) |

---

## 📁 Project Structure

socialhub/
│
├── socialhub/ # Project settings & URLs
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── social/ # Main app
│ ├── templates/social/ # HTML templates
│ ├── static/social/ # CSS, JS, Images
│ │ ├── style.css
│ │ └── script.js
│ ├── models.py
│ ├── views.py
│ ├── urls.py
│ └── forms.py
│
├── static/ # Optional global static folder
├── media/ # Uploaded media files
├── db.sqlite3
└── manage.py

yaml
Copy code

---

## ⚙️ Setup Guide

1. **Clone the repository** to your local system.  
2. **Create a virtual environment** and activate it.  
3. **Install required dependencies** using a `requirements.txt` file.  
4. **Apply database migrations** to create necessary tables.  
5. **Create a superuser** to access the Django admin panel.  
6. **Collect static files** to ensure CSS and JS load properly.  
7. **Run the server** and open the app in your browser at `http://127.0.0.1:8000/`.

---

## 🧩 Important Settings

Inside `socialhub/settings.py`, static and media configurations are:

🎨 UI Preview
Page	Preview  
Login Page	
Home Feed	
Profile	



🛠️ Troubleshooting
If CSS is not loading:

Make sure {% load static %} is added at the top of every HTML template.

Use {% static 'social/style.css' %} in your <link> tag.

Ensure STATICFILES_DIRS, STATIC_ROOT, and MEDIA_ROOT are correctly set in settings.py.

If you face signup errors:

Delete duplicate entries in the database or manage user profiles using signals.

💡 Future Enhancements
Add comments on posts

Implement follow/unfollow system

Add notifications

Integrate REST API with Django REST Framework

👨‍💻 Author
Lakshmi Prasad (Lucky)
💼 Full Stack Developer | Django Enthusiast

📝 License
This project is licensed under the MIT License.
Feel free to use and modify it for learning or development purposes.
