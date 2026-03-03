# 🌿 ShadowRoot-Agro: Core Engine
**By ShadowRoot07**

A high-performance Agrometeorological Monitoring System. This is the **Backend Core**, a RESTful API built with Django 6.0 and Django Rest Framework, designed to process real-time environmental data and provide advanced analytics for precision agriculture.

---

## 🌎 Live Ecosystem
- **Production API:** [https://core-clima-backend.onrender.com/api/](https://core-clima-backend.onrender.com/api/)
- **Frontend Client:** [https://agro-monitor-frontend.vercel.app/](https://agro-monitor-frontend.vercel.app/)

---

## 🚀 Key Features
- **Real-time Synchronization:** Seamless integration with OpenWeatherMap API for live field data.
- **Advanced Analytics:** Backend logic for calculating agricultural metrics like **VPD (Vapor Pressure Deficit)**.
- **Historical Data Engine:** Efficient tracking of temperature, humidity, and pressure trends.
- **Geographic Management:** Multi-location support for different gardens or farms.
- **Reliable Infrastructure:** Database persistence using **PostgreSQL (Neon.tech)** and deployment on **Render**.

## 🛠️ Tech Stack
- **Framework:** Django 6.0 & Django Rest Framework (DRF).
- **Database:** PostgreSQL (Production) / SQLite (Local testing).
- **Environment:** Developed entirely on **Android via Termux** using **Neovim**.
- **DevOps:** CI/CD ready with custom shell scripts for automated testing and deployment.

## 🧪 Testing & Quality
The core engine includes a suite of automated tests to ensure data integrity:
```bash
# Run backend tests
python manage.py test
```

## ⚙️ Installation (Termux / Linux)

1. Clone the repository:
```bash
git clone https://github.com/ShadowRoot07/core_agro.git
```

2. Environment Setup:
```bash
python -m venv venv && source venv/bin/activate
```

3. Dependencies:
```bash
pip install -r requirements.txt
```

4. Configuration:
Create a .env file with the following variables:

+ DEBUG=True
+ SECRET_KEY=your_secret
+ DATABASE_URL=your_postgres_url
+ CLIMA_API_KEY=your_openweathermap_key
+ Database Initialization:
python manage.py migrate
+ Launch Engine:
python manage.py runserver

### Developer Note: This project demonstrates the power of mobile-first development, proving that professional-grade full-stack systems can be built, tested, and deployed entirely from a smartphone. 📱🚀
