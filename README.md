# 🎫 Ticket Classification System

## 🚀 Overview

This project is a Machine Learning based system that classifies customer support tickets and assigns a priority level.
It helps support teams respond faster and smarter.

---

## 🧠 Features

* 📂 Predicts Ticket Category
* ⚡ Assigns Priority (High / Medium / Low)
* 🎯 Uses Machine Learning model (TF-IDF + LinearSVC)
* 💡 Smart rule-based priority mapping
* 🌐 Simple and interactive UI using Streamlit

---

## 🛠️ Tech Stack

* 🐍 Python
* 🤖 Scikit-learn
* 📊 Pandas, NumPy
* 🎨 Streamlit

---

## 📁 Project Structure

```
FUTURE_ML_02/
│── app.py
│── ticket_model.pkl
│── requirements.txt
│── README.md
│── .gitignore
```

---

## ▶️ How to Run

1️⃣ Clone the repository

```
git clone https://github.com/your-username/FUTURE_ML_02.git
```

2️⃣ Go to project folder

```
cd FUTURE_ML_02
```

3️⃣ Create virtual environment

```
python -m venv venv
```

4️⃣ Activate environment

```
venv\Scripts\activate
```

5️⃣ Install dependencies

```
pip install -r requirements.txt
```

6️⃣ Run the app

```
streamlit run app.py
```

---

## 💡 How It Works

* User enters a ticket description
* Model predicts the category
* System assigns priority using rules
* Output is shown instantly in UI

---

## 📊 Example

Input:

```
I am unable to login to my system and it shows access denied
```

Output:

```
Category: Access  
Priority: High
```

---

## 🎯 Goal

To build a smart ticket classification system that improves response time and efficiency of support teams.

---

## ❤️ Author

Made with ❤️ by Lalit Mohan
