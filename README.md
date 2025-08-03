#  Heart Disease Predictive App

A machine learning-based desktop application that analyzes patient health data to predict the risk of heart disease. Built with a logistic regression model and wrapped in a user-friendly PyQt5 GUI, this tool helps medical professionals and users explore real-time risk evaluations using interpretable ML.

 **2nd Place Winner** @ Virginia TSA Hackathon  
 Powered by Kaggle Datasets, Scikit-learn, and Matplotlib

---

##  Features

-  **Logistic Regression Model**  
  Trained on real-world heart disease data from Kaggle with 20+ medical features.
  
-  **Real-Time Risk Prediction**  
  Users can enter their health metrics and instantly receive a predicted risk level.
  
-  **Interactive Desktop UI**  
  PyQt5 GUI designed for smooth data entry and immediate model output display.
  
-  **Visualization Support**  
  Matplotlib and NumPy used for visual feedback and basic interpretability tools.

---

## 🛠 Tech Stack

| Category     | Tools & Libraries                        |
|--------------|-------------------------------------------|
| Language     | Python                                    |
| ML/Stats     | Scikit-learn, NumPy, Pandas               |
| Visualization| Matplotlib                                |
| GUI          | PyQt5                                     |
| Dataset      | [Kaggle: Heart Disease UCI](https://www.kaggle.com/datasets/ronitf/heart-disease-uci) |

---

##  Sample Input Parameters

- Age, Sex
- Chest Pain Type (cp)
- Resting Blood Pressure (trestbps)
- Cholesterol (chol)
- Fasting Blood Sugar (fbs)
- Resting ECG (restecg)
- Max Heart Rate (thalach)
- Exercise-Induced Angina (exang)
- ST Depression (oldpeak)
- Slope, CA, Thal, etc.

---



###  Requirements

- Python 3.8+
- pip / conda
- Recommended: virtual environment

###  Installation

```bash
git clone https://github.com/your-username/heart-disease-predictor.git
cd heart-disease-predictor
pip install -r requirements.txt
