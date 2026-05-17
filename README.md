<div align="center">

# 🧠 Customer Churn Prediction
### ⚡ Deep Learning · ANN · Machine Learning ⚡

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![Keras](https://img.shields.io/badge/Keras-Deep%20Learning-D00000?style=for-the-badge&logo=keras&logoColor=white)](https://keras.io)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

> 🔍 *Predict which customers are likely to leave — before they do.*  
> Built with an **Artificial Neural Network (ANN)** for high-accuracy churn classification.

</div>

---

## 📌 Table of Contents

- [📖 Overview](#-overview)
- [✨ Features](#-features)
- [🗂️ Project Directory](#️-project-directory)
- [⚙️ Installation](#️-installation)
- [🚀 Usage](#-usage)
- [🏗️ Model Architecture](#️-model-architecture)
- [📊 Results](#-results)
- [🛠️ Tech Stack](#️-tech-stack)
- [📚 References](#-references)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)

---

## 📖 Overview

**Customer Churn Prediction** is an end-to-end deep learning project that identifies customers who are likely to discontinue a service. Using an **Artificial Neural Network (ANN)**, the model learns from historical customer behavior, demographics, and account information to output a churn probability.

This solution empowers businesses to take **proactive retention actions**, reducing revenue loss and improving customer lifetime value.

---

## ✨ Features

- 🧹 **Data Preprocessing** — Label encoding, one-hot encoding, feature scaling
- 🏋️ **ANN Model Training** — Multi-layer neural network with dropout regularization
- 📈 **Performance Evaluation** — Accuracy, confusion matrix, classification report
- 💾 **Model Persistence** — Save & load trained model using `.h5` / `.pkl`
- 🌐 **Prediction Interface** — Single customer prediction support
- 📊 **Visualization** — Training loss & accuracy curves

---

## 🗂️ Project Directory

```
customer-churn-prediction/
│
├── Churn_Modelling.csv               # Raw dataset (Bank customer data)
│
├── experiments.ipynb                 # feature enginerring & encoding & model building and training
│
├── prediction.ipynb                  # run the test cases with the input data and predict the output
│
├── model.h5                          # Saved Keras ANN model
│
├── Label_encoder_gender.pkl          # Label encoder for Gender
├── one_hot_encoder_geo.pkl           # One-hot encoder for Geography
├── scaler.pkl                        # StandardScaler object
│
├── 📁 logs/
│   └── training_logs/               # TensorBoard logs (optional)
│
├── 📄 app.py                        # Streamlit / Flask app (optional)
├── 📄 requirements.txt              # Python dependencies
├── 📄 README.md                     # Project documentation
```

---

## ⚙️ Installation

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/customer-churn-prediction.git
cd customer-churn-prediction

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the streamlit interface
streamlit run app.py
```

**`requirements.txt` includes:**
```
tensorflow>=2.10
scikit-learn>=1.2
pandas>=1.5
numpy>=1.23
matplotlib>=3.6
seaborn>=0.12
streamlit>=1.20       # optional, for app
```

---

## 🚀 Usage

### 🔮 Predict for a Single Customer
```python
result = predict_churn(
    CreditScore=600,
    Geography="France",
    Gender="Male",
    Age=40,
    Tenure=3,
    Balance=60000,
    NumOfProducts=2,
    HasCrCard=1,
    IsActiveMember=1,
    EstimatedSalary=50000
)

print(f"Churn Probability: {result['probability']:.2f}")
print(f"Prediction: {'🚨 Will Churn' if result['churn'] else '✅ Will Stay'}")
```

---

## 🏗️ Model Architecture

```
Input Layer      → 11 features
     ↓
Dense Layer 1    → 64 neurons  | Activation: ReLU | Dropout: 0.3
     ↓
Dense Layer 2    → 32 neurons  | Activation: ReLU | Dropout: 0.3
     ↓
Output Layer     → 1 neuron    | Activation: Sigmoid
     ↓
Optimizer: Adam  | Loss: Binary Crossentropy | Metric: Accuracy
```

**Training Config:**
| Parameter     | Value        |
|---------------|--------------|
| Epochs        | 100          |
| Batch Size    | 32           |
| Validation    | 20% Split    |
| Early Stop    | Patience = 10|

---

## 📊 Results

| Metric        | Score  |
|---------------|--------|
| ✅ Accuracy   | ~86%   |
| 🎯 Precision  | ~83%   |
| 📥 Recall     | ~79%   |
| 📐 F1-Score   | ~81%   |
| 📉 AUC-ROC    | ~88%   |

> 📌 *Results may vary slightly depending on random seed and dataset split.*

---

## 🛠️ Tech Stack

| Tool              | Purpose                          |
|-------------------|----------------------------------|
| 🐍 Python         | Core programming language        |
| 🔶 TensorFlow/Keras | ANN model building & training  |
| 🔬 Scikit-Learn   | Preprocessing & evaluation       |
| 🐼 Pandas & NumPy | Data manipulation                |
| 📊 Matplotlib/Seaborn | Data visualization           |
| 💻 Jupyter Notebook | Experimentation & EDA          |
| 🌐 Streamlit      | Web interface (optional)         |

---

## 📚 References

1. 📘 **Goodfellow, I., Bengio, Y., & Courville, A.** (2016). *Deep Learning*. MIT Press.  
   🔗 [https://www.deeplearningbook.org](https://www.deeplearningbook.org)

2. 📗 **TensorFlow Documentation** — Keras Sequential API  
   🔗 [https://www.tensorflow.org/api_docs/python/tf/keras](https://www.tensorflow.org/api_docs/python/tf/keras)

3. 📙 **Scikit-Learn Documentation** — Preprocessing & Metrics  
   🔗 [https://scikit-learn.org/stable/modules/classes.html](https://scikit-learn.org/stable/modules/classes.html)

4. 📕 **Dataset** — Bank Customer Churn Modelling (Kaggle)  
   🔗 [https://www.kaggle.com/datasets/shantanudhakadd/bank-customer-churn-prediction](https://www.kaggle.com/datasets/shantanudhakadd/bank-customer-churn-prediction)

5. 📔 **Chollet, F.** (2021). *Deep Learning with Python* (2nd ed.). Manning Publications.  
   🔗 [https://www.manning.com/books/deep-learning-with-python-second-edition](https://www.manning.com/books/deep-learning-with-python-second-edition)

6. 📓 **Analytics Vidhya** — Customer Churn Prediction using ANN  
   🔗 [https://www.analyticsvidhya.com/blog/2021/10/implementing-artificial-neural-network-for-customer-churn-prediction/](https://www.analyticsvidhya.com/blog/2021/10/implementing-artificial-neural-network-for-customer-churn-prediction/)

---

<div align="center">

Made with ❤️ by **Ashitosh Shirsath**  

</div>