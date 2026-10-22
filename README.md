# ATM Transaction Fraud Detection & Analytics System

## 📌 Project Overview

The **ATM Transaction Fraud Detection & Analytics System** is a Python-based desktop application that analyzes ATM transactions and identifies potentially suspicious activities using rule-based fraud detection techniques.

The system retrieves transaction data from a MySQL database, processes it using Pandas and NumPy, calculates risk scores based on predefined fraud indicators, and displays transaction analytics through a Tkinter graphical user interface.

This project helps identify high-risk transactions and provides useful insights into ATM-wise, city-wise, and risk-level transaction patterns.

## 🎯 Project Objectives

- Analyze ATM transaction data stored in MySQL.
- Identify suspicious transactions using predefined fraud detection rules.
- Calculate risk scores and classify transactions by risk level.
- Generate transaction summaries and statistical insights.
- Display fraud analysis results through a desktop dashboard.

## 🛠️ Technologies Used

- **Python** – Application development and fraud detection logic
- **MySQL** – Transaction database management
- **Pandas** – Data processing, filtering, grouping, and analysis
- **NumPy** – Statistical calculations and risk classification
- **Tkinter** – Graphical user interface (GUI)

## ✨ Key Features

- **MySQL Data Integration:** Retrieves transaction, customer, and ATM information using SQL joins.
- **Rule-Based Fraud Detection:** Identifies suspicious transactions using predefined conditions.
- **Risk Score Calculation:** Assigns scores based on transaction amount, status, time, location, and transaction frequency.
- **Risk Classification:** Classifies transactions as Normal, Medium Risk, or High Risk.
- **Transaction Statistics:** Calculates total transactions, total amount, average amount, successful transactions, and failed transactions.
- **Statistical Analysis:** Calculates the 90th percentile and standard deviation of transaction amounts.
- **ATM-Wise Analysis:** Summarizes transaction counts and amounts for each ATM location.
- **City-Wise Analysis:** Analyzes transaction counts and amounts by ATM city.
- **Risk Summary:** Displays transaction counts and total amounts for each risk level.
- **Interactive GUI:** Provides Analyze Transactions and Clear buttons through Tkinter.

## 🔍 Fraud Detection Rules

The system assigns risk scores based on the following conditions:

| Fraud Indicator | Risk Score |
|---|---:|
| Transaction amount greater than ₹1,00,000 | +30 |
| Failed transaction | +20 |
| Transaction between 12:00 AM and 4:59 AM | +20 |
| Customer city differs from ATM city | +30 |
| Another transaction within 10 minutes for the same account | +20 |

### Risk Classification

| Risk Score | Risk Level |
|---|---|
| 0–29 | Normal |
| 30–59 | Medium Risk |
| 60 and above | High Risk |

**Note:** These are predefined, rule-based risk indicators for project demonstration. The results flag potentially suspicious transactions and do not independently confirm actual fraud.

## 📊 Analytics and Reports

The application displays:

- Total transactions and transaction amount
- Average transaction amount
- Successful and failed transaction counts
- 90th percentile and standard deviation
- Suspicious transaction details and risk reasons
- High-risk transaction details
- ATM-wise transaction analysis
- City-wise transaction analysis
- Risk-level transaction summary

## 🗄️ Database Requirements

Create a MySQL database named `atm_fraud_db`.

The application expects the following tables:

- `customers` – Customer details, account numbers, and cities
- `atm_machines` – ATM locations and cities
- `transactions` – Transaction details, amounts, dates, types, and statuses

The tables must contain the columns referenced in the Python SQL query, with appropriate primary keys and foreign keys.

## ⚙️ Installation and Setup

### 1. Install Python

Install Python on your computer if it is not already installed.

### 2. Install Required Libraries

Open Command Prompt or the terminal and run:

```bash
pip install mysql-connector-python pandas numpy
```

Tkinter is included with most standard Windows Python installations.

### 3. Configure MySQL

- Start your MySQL server.
- Create the `atm_fraud_db` database.
- Create and populate the required tables: `customers`, `atm_machines`, and `transactions`.

### 4. Configure Database Credentials

Update the `db_config` dictionary in the Python program with your own MySQL username and password.

**Important:** Never upload your actual database password or other sensitive credentials to a public repository.

### 5. Run the Application

Save the Python program as `atm_fraud_detection.py` or use your chosen Python filename.

Open the terminal in the project folder and run:

```bash
python atm_fraud_detection.py
```

### 6. Analyze Transactions

- Click **Analyze Transactions** to retrieve and analyze the data.
- Review suspicious transactions, risk scores, and analytical summaries.
- Click **Clear** to clear the displayed results.

## 💻 Source Code

[View Python Source Code](PASTE_YOUR_GITHUB_SOURCE_CODE_LINK_HERE)

## 📸 Output Screenshots

Project output screenshots will be added here.

<!-- Add your uploaded screenshot links below after uploading them to GitHub. -->

## 🚀 Future Enhancements

- Integrate machine learning models for fraud prediction.
- Add interactive charts and data visualizations.
- Export analytical reports to CSV or Excel.
- Introduce date-based filtering and transaction search.
- Add secure configuration for database credentials.

## 🎓 Learning Outcomes

Through this project, I gained practical experience in:

- Python programming and exception handling
- MySQL database connectivity and SQL joins
- Data manipulation using Pandas
- Statistical analysis using NumPy
- Rule-based fraud detection and risk scoring
- GUI development using Tkinter
- Transaction analytics and report generation

## 👩‍💻 Author

**Reeshma Devi R**

Data Analytics Learner | Python | SQL | Pandas | NumPy.
