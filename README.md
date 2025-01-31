# FAQFlow: Django Multilingual FAQ API

## 🚀 Overview
This is a Django-based FAQ management system with **multilingual support**, **WYSIWYG editor integration**, **REST API**, and **Redis caching** for improved performance.

### **Key Features**
✅ **Multilingual Support** (English, Hindi, Bengali)  
✅ **WYSIWYG Editor** (CKEditor for rich text formatting)  
✅ **Fast API with Caching** (Redis for quick translations)  
✅ **Dockerized** (Easily run using Docker & Compose)  
✅ **Admin Panel** (Manage FAQs via Django Admin)  
✅ **Unit Testing & Linting** (pytest, flake8)  

---

## 📌 **Installation Steps**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/footcricket05/FAQFlow.git
cd faq_project
```

### **2️⃣ Create Virtual Environment**
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Apply Database Migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5️⃣ Create Superuser (For Admin Panel)**
```bash
python manage.py createsuperuser
```

### **6️⃣ Start Redis Server (For Caching)**
```bash
redis-server --daemonize yes  # Mac/Linux
# Windows users need Redis installed separately
```

### **7️⃣ Run the Development Server**
```bash
python manage.py runserver
```

### **8️⃣ Open in Browser**
- **API Endpoint:** http://127.0.0.1:8000/api/faqs/
- **Admin Panel:** http://127.0.0.1:8000/admin/

---

## 📌 **API Usage Examples**

### **1️⃣ Get FAQs (Default Language: English)**
```bash
curl http://127.0.0.1:8000/api/faqs/
```

### **2️⃣ Get FAQs in Hindi**
```bash
curl http://127.0.0.1:8000/api/faqs/?lang=hi
```

### **3️⃣ Get FAQs in Bengali**
```bash
curl http://127.0.0.1:8000/api/faqs/?lang=bn
```

### **4️⃣ Create a New FAQ**
```bash
curl -X POST http://127.0.0.1:8000/api/faqs/ -H "Content-Type: application/json" -d '{
  "question": "What is Docker?",
  "answer": "Docker is a containerization platform."
}'
```

---

## 📌 **Docker Setup** (Recommended)

### **1️⃣ Build and Run the Docker Containers**
```bash
docker-compose up --build
```

### **2️⃣ Stop the Containers**
```bash
docker-compose stop
```

### **3️⃣ Check Running Containers**
```bash
docker ps
```

---

## 📌 **Contribution Guidelines**
We welcome contributions! Please follow these steps:

1. **Fork the repository** and clone it locally.
2. **Create a new branch** for your feature:
   ```bash
   git checkout -b feature-new-api-endpoint
   ```
3. **Commit your changes** with meaningful messages:
   ```bash
   git commit -m "feat: Add support for French translations"
   ```
4. **Run tests before pushing**:
   ```bash
   pytest
   ```
5. **Push your branch** and create a Pull Request:
   ```bash
   git push origin feature-new-api-endpoint
   ```

---

## 📌 **Deployment Guide**

### **🚀 Deploying to Heroku**
1. **Login to Heroku CLI:**
   ```bash
   heroku login
   ```
2. **Create a Heroku App:**
   ```bash
   heroku create faq-api
   ```
3. **Deploy Code to Heroku:**
   ```bash
   git push heroku main
   ```
4. **Run Migrations on Heroku:**
   ```bash
   heroku run python manage.py migrate
   ```
5. **Open the App:**
   ```bash
   heroku open
   ```

### **🚀 Deploying to AWS (EC2 Instance)**
1. **SSH into EC2:**
   ```bash
   ssh -i your-key.pem ubuntu@your-ec2-ip
   ```
2. **Install Docker on EC2:**
   ```bash
   sudo apt update && sudo apt install docker docker-compose
   ```
3. **Clone the Repository:**
   ```bash
   git clone <your-repo-url>
   cd faq_project
   ```
4. **Run the Application in Docker:**
   ```bash
   docker-compose up --build -d
   ```
5. **Access API via:**
   ```bash
   http://your-ec2-ip:8000/api/faqs/
   ```

---

## 📌 **Testing & Linting**

### **1️⃣ Run Unit Tests**
```bash
pytest
```

### **2️⃣ Check for Code Style Issues**
```bash
flake8 faqs
```

---

## 📌 **License**
This project is licensed under the MIT License.

