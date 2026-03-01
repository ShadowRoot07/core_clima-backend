# AgroMonitor 🌦️🌱
**By ShadowRoot07**

A professional Agrometeorological Monitoring System built with Django (Backend) and React (Frontend). This system tracks weather patterns for gardens and farms using real-time data and historical trends.

## 🚀 Features
- **Real-time Weather:** Integration with OpenWeatherMap API.
- **Smart Caching:** Local memory cache to optimize API usage.
- **Location Tracking:** Manage multiple points of interest (Gardens/Farms).
- **Historical Analysis:** Track temperature, humidity, and pressure over time.

## 🛠️ Tech Stack
- **Backend:** Django 6.0, Django Rest Framework (DRF).
- **Frontend:** React (Coming Soon).
- **Environment:** Termux (Android) using Python 3.12.
- **Database:** SQLite (Development) / PostgreSQL (Production).

## ⚙️ Installation (Development)
1. Clone the repository.
2. Create a virtual environment: `python -m venv venv`.
3. Activate it: `source venv/bin/activate`.
4. Install dependencies: `pip install -r requirements.txt`.
5. Create a `.env` file with your `CLIMA_API_KEY`.
6. Run migrations: `python manage.py migrate`.

---
*Note: This project is currently under active development.*

