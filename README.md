# 🏦 Bank Customer Churn Prediction

A Deep Learning project that predicts whether a bank customer is likely to churn (leave the bank) or remain with the bank. The model is built using **TensorFlow/Keras** and deployed with **Streamlit** for an interactive user experience.

---

## 📖 Overview

Customer churn prediction is an important business problem in the banking industry. Identifying customers who are likely to leave allows banks to take proactive retention measures.

This project uses customer information such as credit score, geography, age, balance, and salary to predict the probability of customer churn using an Artificial Neural Network (ANN).

---

## 🚀 Features

- Predict customer churn using an ANN model
- Interactive web application built with Streamlit
- Data preprocessing with encoding and feature scaling
- Real-time prediction based on user input
- Clean and easy-to-use interface

---

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Pickle

---

## 📂 Project Structure

```
Bank-Customer-Churn-Prediction/
│
├── app.py                      # Streamlit application
├── experiments.ipynb           # Model training and experimentation
├── prediction.ipynb            # Model prediction notebook
├── model.h5                    # Trained ANN model
├── scaler.pkl                  # StandardScaler
├── label_encode_gender.pkl     # Label Encoder
├── one_hot_encode.pkl          # One-Hot Encoder
├── requirements.txt            # Project dependencies
├── .gitignore
└── README.md
```

---

## 📊 Dataset Features

The model is trained using the following customer attributes:

- Credit Score
- Geography
- Gender
- Age
- Tenure
- Balance
- Number of Products
- Has Credit Card
- Is Active Member
- Estimated Salary

**Target Variable**

- **Exited**
  - `0` → Customer Stays
  - `1` → Customer Churns

---

## 🧠 Model

The prediction model is an **Artificial Neural Network (ANN)** developed using TensorFlow/Keras.

### Data Preprocessing

- Label Encoding (Gender)
- One-Hot Encoding (Geography)
- Standard Scaling

### Model Architecture

- Input Layer
- Hidden Dense Layers (ReLU)
- Output Layer (Sigmoid)

### Loss Function

- Binary Crossentropy

### Optimizer

- Adam

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/3PANKAJ6JANGRA9/Bank-Customer-Churn-Prediction.git
```

### Navigate to the project folder

```bash
cd Bank-Customer-Churn-Prediction
```

### Install the required packages

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will start at:

```
http://localhost:8501
```

---

## 📸 Application

The Streamlit application allows users to:

- Enter customer details
- Process the input data
- Predict the probability of customer churn
- Display the prediction instantly

---

## 🔮 Future Improvements

- Hyperparameter tuning
- Model performance comparison with other algorithms
- Explainable AI (SHAP/LIME)
- Cloud deployment
- User authentication
- Prediction history

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push to your branch.
5. Open a Pull Request.

---

## 📜 License

This project is created for educational and learning purposes.

---

## 👨‍💻 Author

**Pankaj Jangra**

- GitHub: https://github.com/3PANKAJ6JANGRA9
