# Smart Expo Lead Capture System

A Django-based **Visitor Management & Lead Automation System** designed for exhibitions, tech expos, and business stalls.
The system captures visitor details, scores leads automatically, captures photos via QR-based camera access, and sends automated WhatsApp follow-ups.

---

## 🚀 Features

* 📋 Visitor Registration System
* 👥 Group Visitor Registration
* 🔥 Intelligent Lead Scoring (Hot / Warm / Cold)
* 📷 QR-Based Camera Capture for Visitors
* 📱 Automated WhatsApp Follow-up Messaging
* 📊 Admin Analytics Dashboard
* 📺 Live TV Welcome Display for Visitors
* 📤 Excel Export of Visitor Data
* 🔐 Admin Login Panel

---

## 🧠 Lead Scoring Logic

Visitors are automatically classified based on category and provided information.

| Category       | Score  |
| -------------- | ------ |
| Investor       | Hot 🔥 |
| Business Owner | Hot 🔥 |
| Vendor         | Warm   |
| Job Seeker     | Warm   |
| Student        | Cold   |

Additional score is added if the visitor provides:

* Company name
* Email address

---

## 🏗 System Workflow

1. Visitor scans QR code at the stall
2. Visitor fills registration form
3. System calculates **lead score**
4. Visitor photo captured through QR camera page
5. Visitor appears on **TV welcome display**
6. Automated **WhatsApp message** is sent
7. Admin can view analytics & export leads

---

## 🖥 Tech Stack

Backend:

* Python
* Django

Frontend:

* HTML
* CSS
* JavaScript

Automation:

* Selenium
* WhatsApp Web

Database:

* SQLite

Other Libraries:

* OpenPyXL
* QRCode

---

## 📂 Project Structure

```
expo_signin/
│
├── expo_signin/        # Django project settings
├── visitors/           # Main application
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── services/
│   └── templates/
│
├── media/              # Visitor images
├── manage.py
└── README.md
```

---

## ⚙ Installation

Clone the repository:

```
git clone https://github.com/yashtaksale/smart-expo-lead-system.git
```

Navigate into project folder:

```
cd smart-expo-lead-system
```

Create virtual environment:

```
python -m venv venv
```

Activate environment:

Windows

```
venv\Scripts\activate
```

Install dependencies:

```
pip install django selenium openpyxl qrcode pillow
```

Run migrations:

```
python manage.py migrate
```

Start the server:

```
python manage.py runserver
```

---

## 🔐 Admin Access

Admin login password is defined inside:

```
settings.py
```

---

## 📈 Future Improvements

* AI-based lead scoring
* Cloud deployment (AWS / Render)
* Twilio WhatsApp integration
* Visitor analytics dashboard
* CRM integration
* Email automation

---

## 👨‍💻 Author

**Yash Taksale**

Computer Science Engineering Student
Passionate about building intelligent automation systems and scalable web applications.

GitHub:
https://github.com/yashtaksale

---

## ⭐ If you like this project

Give the repository a **star ⭐**
