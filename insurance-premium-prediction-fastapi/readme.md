# 🏥 Insurance Premium Prediction API

A FastAPI-based machine learning API that predicts insurance premium categories based on user health and demographic data.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115-green)
![Pydantic](https://img.shields.io/badge/Pydantic-2.11-red)
![Docker](https://img.shields.io/badge/Docker-Ready-blue)
![AWS](https://img.shields.io/badge/AWS-EC2-orange)

## 📋 Features

- **ML-Powered Predictions**: Predicts insurance premium categories (Low, Medium, High)
- **Confidence Scores**: Returns prediction confidence and class probabilities
- **Input Validation**: Pydantic-based data validation
- **Health Check Endpoint**: For container orchestration and monitoring
- **Streamlit Frontend**: Interactive UI for testing predictions
- **Docker Ready**: Containerized for easy deployment

---

## 🚀 Quick Start

### Option 1: Pull from Docker Hub (Recommended)

```bash
docker pull farhanrhine/insurance-premium-api
docker run -p 8000:8000 farhanrhine/insurance-premium-api
```

### Option 2: Build Locally

```bash
git clone https://github.com/farhanrhine/FastAPI.git
cd FastAPI/insurance-premium-prediction-fastapi
docker build -t insurance-premium-api .
docker run -p 8000:8000 insurance-premium-api
```

### Option 3: Run Without Docker

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```

---

## 🌐 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home - Welcome message |
| `/health` | GET | Health check for monitoring |
| `/predict` | POST | Predict insurance premium category |
| `/docs` | GET | Swagger UI documentation |

### Example Request

```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "age": 25,
    "weight": 65.0,
    "height": 1.75,
    "income_lpa": 12.0,
    "smoker": false,
    "city": "Mumbai",
    "occupation": "private_job"
  }'
```

### Example Response

```json
{
  "response": {
    "predicted_category": "Medium",
    "confidence": 0.7823,
    "class_probabilities": {
      "Low": 0.12,
      "Medium": 0.78,
      "High": 0.10
    }
  }
}
```

---

## 🎨 Frontend (Streamlit)

Run the interactive frontend locally:

```bash
# Make sure FastAPI backend is running first
streamlit run frontend.py
```

### Configure API URL in `frontend.py`:

```python
# For local testing
API_URL = "http://localhost:8000/predict"

# For deployed API (replace with your EC2 IP)
# API_URL = "http://<YOUR-EC2-IP>:8000/predict"
```

---

## ☁️ AWS EC2 Deployment

### Step 1: Create EC2 Instance

1. Go to AWS Console → EC2 → Launch Instance
2. Choose **Ubuntu Server 22.04 LTS**
3. Select instance type (t2.micro for free tier)
4. Configure Security Group (see Step 6)
5. Launch and download key pair (.pem file)

### Step 2: Connect to EC2

```bash
chmod 400 your-key.pem
ssh -i "your-key.pem" ubuntu@<YOUR-EC2-PUBLIC-IP>
```

### Step 3: Install Docker on EC2

```bash
sudo apt-get update
sudo apt-get install -y docker.io
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $USER
exit
```

### Step 4: Reconnect to EC2

```bash
ssh -i "your-key.pem" ubuntu@<YOUR-EC2-PUBLIC-IP>
```

### Step 5: Pull and Run Docker Image

```bash
docker pull farhanrhine/insurance-premium-api:latest
docker run -d -p 8000:8000 farhanrhine/insurance-premium-api
```

> 💡 Use `-d` flag to run in detached mode (background)

### Step 6: Configure Security Group

1. Go to EC2 → Security Groups
2. Select your instance's security group
3. Edit Inbound Rules → Add Rule:
   - **Type**: Custom TCP
   - **Port Range**: 8000
   - **Source**: 0.0.0.0/0 (or your IP for security)
4. Save rules

### Step 7: Test the Deployed API

```bash
# Health check
curl http://<YOUR-EC2-PUBLIC-IP>:8000/health

# Swagger UI
http://<YOUR-EC2-PUBLIC-IP>:8000/docs
```

---

## 🔧 Running Frontend with Deployed API

Update `frontend.py` to use your EC2 endpoint:

```python
# Comment out localhost
# API_URL = "http://localhost:8000/predict"

# Use your EC2 public IP
API_URL = "http://<YOUR-EC2-PUBLIC-IP>:8000/predict"
```

Then run:
```bash
streamlit run frontend.py
```

---

## 📁 Project Structure

```
insurance-premium-prediction-fastapi/
├── app.py                  # FastAPI main application
├── frontend.py             # Streamlit frontend
├── Dockerfile              # Docker configuration
├── requirements.txt        # Python dependencies
├── README.md               # This file
├── config/
│   └── city_tier.py        # City tier configuration
├── model/
│   ├── model.pkl           # Trained ML model
│   └── predict.py          # Prediction logic
└── schema/
    ├── user_input.py       # Input validation schema
    └── prediction_response.py  # Response schema
```

---

## 📊 Input Parameters

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `age` | int | Age (1-119) | 35 |
| `weight` | float | Weight in kg | 75.0 |
| `height` | float | Height in meters (0.5-2.5) | 1.75 |
| `income_lpa` | float | Annual income in LPA | 12.0 |
| `smoker` | bool | Smoking status | false |
| `city` | string | City name | "Mumbai" |
| `occupation` | string | Job type | "private_job" |

### Valid Occupations
- `retired`
- `freelancer`
- `student`
- `government_job`
- `business_owner`
- `unemployed`
- `private_job`

---

## 🐳 Docker Commands Reference

```bash
# Pull image
docker pull farhanrhine/insurance-premium-api

# Run container
docker run -p 8000:8000 farhanrhine/insurance-premium-api

# Run in background
docker run -d -p 8000:8000 farhanrhine/insurance-premium-api

# View running containers
docker ps

# Stop container
docker stop <container-id>

# View logs
docker logs <container-id>
```

---

## 👨‍💻 Author

**Farhan**
- GitHub: [@farhanrhine](https://github.com/farhanrhine)
- Docker Hub: [farhanrhine/insurance-premium-api](https://hub.docker.com/r/farhanrhine/insurance-premium-api)

---
