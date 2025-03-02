# 🌱 Crop Recommendation System
🚜 A machine learning-powered web application designed to help farmers determine the best crop to grow based on soil and weather conditions.

## 📌 Project Overview
The **Crop Recommendation System** uses machine learning to predict the most suitable crop for cultivation based on key soil and environmental factors, including:

- Nitrogen (N), Phosphorus (P), Potassium (K) levels in soil
- Temperature (°C)
- Humidity (%)
- Soil pH
- Rainfall (mm)

The model is trained using AWS SageMaker and deployed with a user-friendly interface built using **Streamlit** for the frontend and **Flask** for the backend. The system leverages **AWS EC2** for deployment and **AWS S3** for storage.

## ⚙️ Tech Stack
- **Frontend**: Streamlit
- **Machine Learning**: AWS SageMaker
- **Storage**: AWS S3
- **Deployment**: AWS EC2
- **Version Control**: Git, GitHub

## 🚀 Features
✅ Enter soil and weather conditions  
✅ Get AI-powered crop recommendations  
✅ Easy-to-use web interface  
✅ Hosted on AWS Free Tier services for cost-effective deployment

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/Crop-Recommendation-System.git
cd Crop-Recommendation-System
```
### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
### 3️⃣ Run the Web App
```bash
streamlit run app.py
```

## 📂 Project Structure
```bash
Crop-Recommendation-System/
│── app.py                        # Streamlit frontend
│── crop-recommendation-model.ipynb # Jupyter notebook for training the model
│── Crop_recommendation.csv        # Dataset for training the model
│── model.pkl                     # Saved machine learning model
│── minmaxscaler.pkl              # MinMaxScaler for feature scaling
│── standscaler.pkl               # StandardScaler for feature scaling
│── requirements.txt              # Python dependencies
└── README.md                     # Project Documentation


```
## 🎯 How It Works
#### 1️⃣ Enter the soil and weather parameters in the web interface.
#### 2️⃣ Click "Predict Crop".
#### 3️⃣ The model processes the input and returns the best crop recommendation based on the provided data.

## Application Overview
![Screenshot 2025-03-02 225411](https://github.com/user-attachments/assets/c3f28cf6-47fd-465c-9fec-f1de9d36d6fd)

## 📌 Future Enhancements
##### 🔹 Support for real-time weather API integration
##### 🔹 Adding more crops & region-specific recommendations
##### 🔹 Improving accuracy with deep learning models

