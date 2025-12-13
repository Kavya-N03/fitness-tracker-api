# Fitness Tracker REST API

A **Fitness Tracker REST API** built using **Django Rest Framework** that allows users to set fitness goals, log daily activities and meals, track calorie intake and calories burned, and monitor overall daily progress.

The API is designed to be consumed by a frontend application.

---

**Features**

- **User Authentication**
  - Secure user registration and login using JWT

- **Goal Management**
  - Set personal fitness goals
  - Track progress towards goals over time

- **Activity Tracking**
  - Log daily activities such as walking, running, swimming, yoga, etc.
  - Track calories burned for each activity

- **Nutrition & Meal Tracking**
  - Log meals consumed by the user
  - Track nutritional values including calories, protein, fats, and carbohydrates

- **Daily Progress Tracking**
  - View daily summary of:
    - Calories consumed
    - Calories burned
    - Nutritional intake (protein, fats, carbs)
  - Monitor overall fitness progress by date

- **Secure API**
  - All user data is protected using JWT authentication

---

**Technologies Used**

- **Backend:** Django, Django Rest Framework
- **Authentication:** JWT (JSON Web Tokens)
- **Database:** PostgreSQL (Render) / SQLite (Local)
- **Deployment:** Render

---

**Deployed API**

🔗https://fitness-tracker-api-5ibu.onrender.com/api/

---

** API Endpoints**

- `/register/`
- `/token/`
- `/auth/token/`
- `/goals/`
- `/activities/`
- `/meals/`
- `/daily-progress/`

🔐 Most endpoints require **JWT authentication**.

---

**Run Locally**

```bash
git clone https://github.com/your-username/fitness_tracker_api.git
cd fitness_tracker_api
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
