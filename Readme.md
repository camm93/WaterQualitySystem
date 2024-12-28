# 🚀 End-to-End Machine Learning MLOps Project
**Building, Deploying, and Managing a Machine Learning Pipeline with CI/CD, Docker, and Cloud**  


## 🎯 **Project Overview**  
This project demonstrates the implementation of a complete Machine Learning Operations (MLOps) pipeline by building and deploying a classifier to predict water quality as **drinkable** or **not drinkable** based on various water properties (e.g., pH, Turbidity, Chloramines).  

During the model selection phase, **Logistic Regression** and **K-Nearest Neighbors (KNN)** models were trained and evaluated alongside a **Decision Tree Classifier**, with the Decision Tree ultimately selected for deployment based on its performance and interpretability.  

This project integrates **Exploratory Data Analysis**, **model training**, **model selection and hyperparameter tuning**, **deployment**, **containerization**, **CI/CD automation**, and **cloud deployment**, simulating a real-world production environment.



## 🛠️ **Tools and Technologies Used**  
| **Category**               | **Tools**                               |
|----------------------------|-----------------------------------------|
| **Programming**            | Python (numpy, pandas, scikit-learn)    |
| **Model Training**         | LogisticRegressionClassifier, KNN, **DecisionTreeClassifier** (scikit-learn)   |
| **Data Preprocessing**     | Pipelines (Imputation, Scaling)         |
| **API Development**        | FastAPI                                |
| **Containerization**       | Docker, DockerHub                      |
| **CI/CD**                  | GitHub Actions                         |
| **Cloud Deployment**       | Render                                 |
| **Version Control**        | Git, GitHub                            |
| **Security**               | GitHub Secrets, DockerHub Access Tokens|



## 📝 **Project Workflow**  

### 🔹 **1️⃣ Data Preprocessing**
- Imported dataset, handled missing values using **mean imputation**.  
- Built a **data preprocessing pipeline** to automate feature scaling and transformation.  

### 🔹 **2️⃣ Model Training**
- Trained a **Decision Tree Classifier** for binary classification.  
- Fine-tuned hyperparameters (`max_depth`, `min_samples_split`) using grid search.  
- Saved the trained model as a serialized file (`.pkl`) using `joblib`.  

### 🔹 **3️⃣ API Development**
- Built a **FastAPI application** to serve the trained model.  
- Exposed a `/predict` endpoint for predictions.  
- API accepts JSON input, preprocesses the data, and returns predictions in real-time.  

### 🔹 **4️⃣ Dockerization**
- Packaged the application into a **Docker container** for easy deployment.  
- Created a `Dockerfile` to ensure the app runs consistently across environments.  
- Pushed the container image to **DockerHub** for reuse and deployment.  

### 🔹 **5️⃣ CI/CD Pipeline**
- Configured **GitHub Actions** to automate:  
  - Building the Docker image.  
  - Pushing the image to DockerHub.  
  - Triggering redeployment on Render.  

### 🔹 **6️⃣ Cloud Deployment**
- Deployed the containerized application to **Render**, a cloud hosting platform.  
- Configured environment variables for security (e.g., DockerHub credentials).  
- Monitored application logs for debugging and performance insights.  



## 📊 **Key Features**
- **End-to-End MLOps Workflow**: Covers every step from data preprocessing to model deployment.  
- **Cloud Deployment**: Real-world deployment using **Render**.  
- **Reproducibility**: Automated CI/CD ensures consistent builds and deployments.  
- **Scalability**: Dockerized application enables horizontal scaling and portability.  
- **Security**: Managed sensitive credentials with GitHub Secrets and DockerHub tokens.  



## 🛠️ **How to Run the Project Locally**  

### 🔹 **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/camm93/WaterQualitySystem.git

cd WaterQualitySystem
```

### 🔹 **2️⃣ Build and Run the Docker Container**
```bash
docker build -t WaterQualitySystem .

docker run -d -p 8000:8000 WaterQualitySystem
```

### 🔹 **3️⃣ Test the API**
Use **Postman** or `curl` to test the `/predict` endpoint.

Example `curl` command:

```bash
curl -X POST http://localhost:8000/predict \
-H "Content-Type: application/json" \
-d '{
  "pH": 7.13,
  "Dureza": 173.69,
  "Sólidos": 19309.57,
  "Cloraminas": 6.53,
  "Sulfatos": 372.54,
  "Conductividad": 295.39,
  "Carbono_orgánico": 7.27,
  "Trihalometanos": 88.79,
  "Turbidez": 3.40
}'
```

Expected Response:

```json
{
    "prediction": "NO",
    "probability": [
        0.9414033798677441,
        0.058596620132255695
    ]
}
```


## 🛠️ Folder Structure

```
.
├── app.py                  # FastAPI application
├── model.pkl               # Serialized Decision Tree model
├── Dockerfile              # Docker container configuration
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
└── .github/workflows       # CI/CD configuration
    └── deploy.yml          # GitHub Actions workflow
```
---

## 📈 To Recap
- **Model Deployment**: Transitioning from Jupyter notebooks to a production-ready API.
- **Docker**: Containerizing applications for consistent deployments.
- **CI/CD**: Automating builds, tests, and deployments using GitHub Actions.
- **Cloud Hosting**: Deploying machine learning APIs to cloud platforms.
- **Security**: Managing secrets and sensitive credentials for DockerHub and Render.
---

## 🚀 Potential Improvements
1. Add model monitoring (e.g., API latency, prediction drift) using Prometheus + Grafana.
2. Incorporate MLflow for experiment tracking and model versioning.
3. Deploy the app to AWS (EC2, Lambda) or GCP for real-world scalability.
4. Add unit tests for API endpoints using pytest.
5. Enhance the CI/CD pipeline with rollback mechanisms and more extensive test coverage.

---

## 💬 Contact
For questions or collaboration opportunities, feel free to reach out:

- **Email**: crismur_93hotmail.com
- **LinkedIn**: [Cristian Murillo](https://www.linkedin.com/in/cristianmurillom/)
