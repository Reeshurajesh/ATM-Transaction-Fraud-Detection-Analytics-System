import mysql.connector
import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import messagebox


db_config = {
    "host": "localhost",
    "user": "root",
    "password": "Reesh@123",
    "database": "atm_fraud_db"
}


def get_data():

    conn = mysql.connector.connect(**db_config)

    sqlQuery = '''
        SELECT
            t.transaction_id,
            c.name,
            c.account_number,
            c.city AS customer_city,
            a.atm_location,
            a.city AS atm_city,
            t.transaction_date,
            t.amount,
            t.transaction_type,
            t.status
        FROM transactions t
        INNER JOIN customers c
            ON t.customer_id = c.customer_id
        INNER JOIN atm_machines a
            ON t.atm_id = a.atm_id
    '''

    df = pd.read_sql(sqlQuery, conn)

    conn.close()

    return df


def analyze_transactions():

    try:

        df = get_data()

        df["transaction_date"] = pd.to_datetime(
            df["transaction_date"]
        )

        df["amount"] = df["amount"].astype(float)

        df["risk_score"] = 0

        df["risk_reason"] = ""

        high_value = df["amount"] > 100000

        df.loc[high_value, "risk_score"] += 30

        df.loc[high_value, "risk_reason"] += "High Amount, "

        failed = df["status"] == "Failed"

        df.loc[failed, "risk_score"] += 20

        df.loc[failed, "risk_reason"] += "Failed Transaction, "

        hour = df["transaction_date"].dt.hour

        odd_hour = (hour >= 0) & (hour < 5)

        df.loc[odd_hour, "risk_score"] += 20

        df.loc[odd_hour, "risk_reason"] += "Odd Hour, "

        different_city = (
            df["customer_city"] != df["atm_city"]
        )

        df.loc[different_city, "risk_score"] += 30

        df.loc[
            different_city,
            "risk_reason"
        ] += "Different City, "

        df = df.sort_values(
            ["account_number", "transaction_date"]
        )

        df["time_difference"] = (
            df.groupby("account_number")
            ["transaction_date"]
            .diff()
            .dt.total_seconds()
            / 60
        )

        rapid_transaction = (
            df["time_difference"] <= 10
        )

        df.loc[
            rapid_transaction,
            "risk_score"
        ] += 20

        df.loc[
            rapid_transaction,
            "risk_reason"
        ] += "Rapid Transaction, "

        df["risk_level"] = np.where(
            df["risk_score"] >= 60,
            "HIGH RISK",
            np.where(
                df["risk_score"] >= 30,
                "MEDIUM RISK",
                "NORMAL"
            )
        )


        total_transactions = len(df)

        total_amount = df["amount"].sum()

        average_amount = df["amount"].mean()

        successful_transactions = len(
            df[df["status"] == "Success"]
        )

        failed_transactions = len(
            df[df["status"] == "Failed"]
        )

        amounts = df["amount"].to_numpy()

        mean_amount = np.mean(amounts)

        std_dev = np.std(amounts)

        p90_amount = np.percentile(
            amounts,
            90
        )


        suspicious_df = df[
            df["risk_score"] >= 30
        ]

        high_risk_df = df[
            df["risk_level"] == "HIGH RISK"
        ]

        atm_summary = df.groupby(
            "atm_location"
        ).agg(
            total_transactions=(
                "transaction_id",
                "count"
            ),
            total_amount=(
                "amount",
                "sum"
            ),
            average_amount=(
                "amount",
                "mean"
            )
        ).reset_index()

        city_summary = df.groupby(
            "atm_city"
        ).agg(
            total_transactions=(
                "transaction_id",
                "count"
            ),
            total_amount=(
                "amount",
                "sum"
            )
        ).reset_index()

        risk_summary = df.groupby(
            "risk_level"
        ).agg(
            transaction_count=(
                "transaction_id",
                "count"
            ),
            total_amount=(
                "amount",
                "sum"
            )
        ).reset_index()

        result_text.delete(
            "1.0",
            tk.END
        )


        result_text.insert(
            tk.END,
            "========== ATM TRANSACTION RISK ANALYTICS ==========\n\n"
        )


        result_text.insert(
            tk.END,
            f"Total Transactions : {total_transactions}\n"
        )

        result_text.insert(
            tk.END,
            f"Total Amount       : Rs.{total_amount:,.2f}\n"
        )

        result_text.insert(
            tk.END,
            f"Average Amount     : Rs.{average_amount:,.2f}\n"
        )

        result_text.insert(
            tk.END,
            f"Successful         : {successful_transactions}\n"
        )

        result_text.insert(
            tk.END,
            f"Failed             : {failed_transactions}\n"
        )

        result_text.insert(
            tk.END,
            f"90th Percentile    : Rs.{p90_amount:,.2f}\n"
        )

        result_text.insert(
            tk.END,
            f"Standard Deviation : Rs.{std_dev:,.2f}\n\n"
        )


        result_text.insert(
            tk.END,
            "========== RISK SUMMARY ==========\n\n"
        )

        result_text.insert(
            tk.END,
            f"Suspicious Transactions : {len(suspicious_df)}\n"
        )

        result_text.insert(
            tk.END,
            f"High Risk Transactions  : {len(high_risk_df)}\n\n"
        )


        result_text.insert(
            tk.END,
            "========== SUSPICIOUS TRANSACTIONS ==========\n\n"
        )


        if len(suspicious_df) > 0:

            result_text.insert(
                tk.END,
                suspicious_df[
                    [
                        "transaction_id",
                        "name",
                        "amount",
                        "transaction_date",
                        "atm_city",
                        "risk_score",
                        "risk_level",
                        "risk_reason"
                    ]
                ].to_string(index=False)
            )

        else:

            result_text.insert(
                tk.END,
                "No suspicious transactions found."
            )


        result_text.insert(
            tk.END,
            "\n\n"
        )


        result_text.insert(
            tk.END,
            "========== HIGH RISK TRANSACTIONS ==========\n\n"
        )


        if len(high_risk_df) > 0:

            result_text.insert(
                tk.END,
                high_risk_df[
                    [
                        "transaction_id",
                        "name",
                        "amount",
                        "transaction_date",
                        "risk_score",
                        "risk_level",
                        "risk_reason"
                    ]
                ].to_string(index=False)
            )

        else:

            result_text.insert(
                tk.END,
                "No high risk transactions found."
            )


        result_text.insert(
            tk.END,
            "\n\n"
        )


        result_text.insert(
            tk.END,
            "========== ATM WISE ANALYSIS ==========\n\n"
        )

        result_text.insert(
            tk.END,
            atm_summary.to_string(index=False)
        )


        result_text.insert(
            tk.END,
            "\n\n"
        )


        result_text.insert(
            tk.END,
            "========== CITY WISE ANALYSIS ==========\n\n"
        )

        result_text.insert(
            tk.END,
            city_summary.to_string(index=False)
        )


        result_text.insert(
            tk.END,
            "\n\n"
        )


        result_text.insert(
            tk.END,
            "========== RISK LEVEL ANALYSIS ==========\n\n"
        )

        result_text.insert(
            tk.END,
            risk_summary.to_string(index=False)
        )


        status_label.config(
            text="Risk Analysis Completed Successfully!"
        )


    except Exception as e:

        messagebox.showerror(
            "Error",
            str(e)
        )

        status_label.config(
            text="Error occurred!"
        )


def clear_result():

    result_text.delete(
        "1.0",
        tk.END
    )

    status_label.config(
        text="Ready"
    )


window = tk.Tk()


window.title(
    "ATM Transaction Fraud Detection & Risk Analysis"
)


window.geometry(
    "1400x900"
)


title = tk.Label(
    window,
    text="ATM Transaction Fraud Detection & Risk Analysis",
    font=("Arial", 20, "bold")
)


title.pack(
    pady=20
)


subtitle = tk.Label(
    window,
    text="MySQL + Python + Pandas + NumPy + Fraud Rules + Risk Score + Tkinter Dashboard",
    font=("Arial", 11)
)


subtitle.pack()


analyze_button = tk.Button(
    window,
    text="Analyze Transactions",
    font=("Arial", 12, "bold"),
    command=analyze_transactions
)


analyze_button.pack(
    pady=15
)


clear_button = tk.Button(
    window,
    text="Clear",
    font=("Arial", 11),
    command=clear_result
)


clear_button.pack()


result_text = tk.Text(
    window,
    width=180,
    height=40,
    font=("Courier New", 10)
)


result_text.pack(
    pady=15
)


status_label = tk.Label(
    window,
    text="Ready",
    font=("Arial", 11)
)


status_label.pack()


window.mainloop()




       
             
