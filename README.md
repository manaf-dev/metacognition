# Metacognition Application


### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/manaf-dev/metacognition.git
   cd metacognition
   ```

2. **Create virtual environment and install requirements:**
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Run the migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```


4. **Create superuser:**
   ```bash
   python manage.py createsuperuser
   ```
   -Create with a username and password of your choice

4. **Run the application:**
   ```bash
   python manage.py runserver
   ```



5. **Access the application:**
   - Open brower at: `http://localhost:8000`
   - Login with superuser username and password you created above
