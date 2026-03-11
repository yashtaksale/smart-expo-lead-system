<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="60"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/django/django-plain.svg" width="60"/>
</p>

<h1 align="center">🚀 Smart Expo Lead Capture System</h1>

<p align="center">
Visitor Management & Lead Automation Platform for Exhibitions and Tech Events
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Django](https://img.shields.io/badge/Django-Web%20Framework-green?style=for-the-badge\&logo=django)
![Selenium](https://img.shields.io/badge/Selenium-Automation-orange?style=for-the-badge\&logo=selenium)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Active-brightgreen?style=for-the-badge)

</p>

---

# 🌟 Overview

**Smart Expo Lead Capture System** is a Django-based platform designed for exhibitions, business expos, and technology events to efficiently capture visitor leads and automate follow-ups.

The system allows visitors to register through a simple form, automatically calculates **lead scores**, captures visitor photos via QR-based camera access, sends **automated WhatsApp follow-ups**, and provides an **admin analytics dashboard** for managing leads.

This system helps businesses **convert exhibition visitors into potential clients efficiently**.

---

# ✨ Key Features

* 📋 Visitor Registration System
* 👥 Group Visitor Registration
* 🔥 Intelligent Lead Scoring (Hot / Warm / Cold)
* 📷 QR-Based Camera Capture
* 📱 Automated WhatsApp Messaging
* 📊 Admin Analytics Dashboard
* 📺 Real-Time TV Welcome Display
* 📤 Excel Export of Visitor Data
* 🔐 Secure Admin Login Panel

---

# 🎬 Project Demo

<p align="center">
<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcHBkNHF1M3JqZ3Q0MTRmM3M1MnhkYWRkdmR3ZXpsMWl3YW5xczI5dyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/coxQHKASG60HrHtvkt/giphy.gif" width="700">
</p>

Experience the **Smart Expo Lead Capture System** in action — from visitor registration to automated lead management.

---

# 📸 Project Screenshots

### 📝 Visitor Signup Page

<p align="center">
<img width="900" src="https://github.com/user-attachments/assets/704816c7-82b7-4cc9-86c1-738ed93f7af4">
</p>

### 📷 Thank You Page

<p align="center">
<img width="500" src="https://github.com/user-attachments/assets/fe7570ce-26d5-4ccf-a364-95a4a2b2555c">
</p>

### 📊 Admin Dashboard

<p align="center">
<img width="900" src="https://github.com/user-attachments/assets/f7e925f5-b311-43e3-89e2-ec7e1c47c08b">
</p>

### 📺 TV Welcome Display

<p align="center">
<img width="900" src="https://github.com/user-attachments/assets/f1afd989-40d5-4d11-ba29-a7f1d58fe0d0">
</p>

---

# 🧠 System Architecture

```
                Visitor
                   │
                   ▼
            QR Code Scan
                   │
                   ▼
            Signup Form (Django)
                   │
                   ▼
            Visitor Database (SQLite)
                   │
       ┌───────────┼────────────┐
       ▼           ▼            ▼
 Lead Scoring   Photo Capture   WhatsApp Automation
   Engine          System           (Selenium)
       │           │                │
       ▼           ▼                ▼
  Hot / Warm / Cold      Visitor Image Storage
                   │
                   ▼
             Admin Dashboard
                   │
         ┌─────────┼───────────┐
         ▼         ▼           ▼
     Analytics   Lead Data   Excel Export
```

---

# 🔄 Visitor Workflow

```
Visitor Arrives at Stall
        │
        ▼
Scans QR Code
        │
        ▼
Fills Registration Form
        │
        ▼
Lead Score Calculated
        │
        ▼
Visitor Photo Captured
        │
        ▼
Welcome Display on TV
        │
        ▼
Automated WhatsApp Follow-up
        │
        ▼
Admin Dashboard Analytics
```

---

# 🧰 Tech Stack

| Layer         | Technology              |
| ------------- | ----------------------- |
| Backend       | Django                  |
| Programming   | Python                  |
| Frontend      | HTML, CSS, JavaScript   |
| Automation    | Selenium                |
| Database      | SQLite                  |
| Data Export   | OpenPyXL                |
| QR Generation | Python QRCode           |
| Messaging     | WhatsApp Web Automation |

---

# ⚙ Installation

Clone the repository

```
git clone https://github.com/yashtaksale/smart-expo-lead-system.git
```

Navigate to the project folder

```
cd smart-expo-lead-system
```

Create virtual environment

```
python -m venv venv
```

Activate environment (Windows)

```
venv\Scripts\activate
```

Install dependencies

```
pip install django selenium openpyxl qrcode pillow
```

Run migrations

```
python manage.py migrate
```

Start the server

```
python manage.py runserver
```

---

# 💼 Real World Use Cases

This system can be used in:

* Technology exhibitions
* Startup demo events
* Business networking expos
* College project exhibitions
* Product launch events

Companies can easily capture visitor information and automatically follow up with potential leads.

---

# 📈 Future Improvements

* AI-based lead scoring
* Cloud deployment (AWS / Render)
* Twilio WhatsApp integration
* Visitor analytics dashboard
* CRM integration
* Email automation

---

# 👨‍💻 Author

**Yash Taksale**

Computer Science Engineering Student
Passionate about building intelligent automation systems and scalable web applications.

GitHub
https://github.com/yashtaksale

---

⭐ If you like this project, consider giving it a **star on GitHub**.

---
