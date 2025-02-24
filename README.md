# Basic Book Appoinment API

## 🚗 Overview
This project is a **Book Appoinment API** built with **Django Rest Framework (DRF)**


## 📌 Features

### 🏷 User API
- Add Doctors,Nurse,Appoinment using Django Rest Framework's.

#### API Endpoints:
- `DoctorCreate` 
- `NurseCreate` 
- `AppoinmentCreate` 
- `AtendanceCreate` 
- `AttednanceReport` 
- `TodayAppoinment` 



## 🚀 Getting Started

### 📌 Installation
1. Clone the repository:
   ```bash
   https://github.com/PriyankaTaug/BookAppoinment.git
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migration
   python manage.py migrate
   ```
4. Run the development server:
   ```bash
   python manage.py runserver
   ```