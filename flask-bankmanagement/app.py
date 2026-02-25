from flask import Flask,request,jsonify
from flask_cors import CORS 
import mysql.connector

app = Flask(__name__)
CORS(app)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Kamali2003arun@",
    database="bankmanagement"
)

@app.route("/createaccount", methods=["POST"])
def create_account():
    data = request.get_json()

    acc_no = data.get("acc_no")
    name = data.get("name")
 
    cursor = db.cursor()

    sql = "INSERT INTO accounts (acc_no, name, balance) VALUES (%s, %s, 0)"
    cursor.execute(sql, (
    data.get('acc_no'),
    data.get('name')
    ))
 
    db.commit()
    cursor.close()
  
    return jsonify({"message": "Account Created Successfully"})


@app.route("/deposit", methods=["POST"])
def deposit():
    data = request.get_json()

    acc_no = data.get("acc_no")
    amount = data.get("amount")

    cursor = db.cursor()

    sql = "INSERT INTO transactions (acc_no, trans_type, amount) VALUES (%s, 'DEPOSIT', %s)"

    cursor.execute(sql,(
        data.get('acc_no'),
        data.get('amount')
    ))

    cursor.execute(
        "UPDATE accounts SET balance = balance + %s WHERE acc_no = %s",
        (amount, acc_no)
    )

    db.commit()
    cursor.close()

    return jsonify({"message": "Deposit Successful"})


@app.route("/withdraw", methods=["POST"])
def withdraw():
    data = request.get_json()

    acc_no = data.get("acc_no")
    amount = data.get("amount")

    cursor = db.cursor()

    cursor.execute("SELECT balance FROM accounts WHERE acc_no = %s", (acc_no,))
    balance= cursor.fetchone()[0]

    cursor.execute(
        "INSERT INTO transactions (acc_no, trans_type, amount) VALUES (%s, 'WITHDRAW', %s)",
        (acc_no, amount)
    )

    cursor.execute(
        "UPDATE accounts SET balance = balance - %s WHERE acc_no = %s",
        (amount, acc_no)
    )

    db.commit()
    cursor.close()

    return jsonify({"message": "Withdraw Successful"})


@app.route("/transfer", methods=["POST"])
def transfer():
    data = request.get_json()

    from_acc = data.get("from_acc")
    to_acc = data.get("to_acc")
    amount = data.get("amount")

    cursor = db.cursor()

    cursor.execute("SELECT balance FROM accounts WHERE acc_no = %s", (from_acc,))
    balance = cursor.fetchone()[0]
 
    # Sender 
    cursor.execute(
        "INSERT INTO transactions (acc_no, trans_type, amount) VALUES (%s, 'TRANSFER_OUT', %s)",
        (from_acc, amount)
    )

    cursor.execute(
        "UPDATE accounts SET balance = balance - %s WHERE acc_no = %s",
        (amount, from_acc)
    )

    # Receiver
    cursor.execute(
        "INSERT INTO transactions (acc_no, trans_type, amount) VALUES (%s, 'TRANSFER_IN', %s)",
        (to_acc, amount)
    )

    cursor.execute(
        "UPDATE accounts SET balance = balance + %s WHERE acc_no = %s",
        (amount, to_acc)
    )

    db.commit()
    cursor.close()

    return jsonify({"message": "Transfer Successful"})


@app.route("/balance/<int:acc_no>", methods=["GET"])
def check_balance(acc_no):
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT balance FROM accounts WHERE acc_no = %s",
        (acc_no,)
    )

    balance = cursor.fetchone()
    cursor.close()

    return jsonify(balance)

# recent transaction

@app.route("/recenttransactions/<int:acc_no>", methods=["GET"])
def getrecent_transactions(acc_no):
    cursor = db.cursor(dictionary=True)

    cursor.execute(
        "SELECT trans_id, trans_type, amount, date FROM transactions WHERE acc_no = %s ORDER BY trans_id DESC",
        (acc_no,)
    )

    gettransactions = cursor.fetchall()
    cursor.close()

    return jsonify(gettransactions)

if __name__ == "__main__":
    app.run(debug=True)