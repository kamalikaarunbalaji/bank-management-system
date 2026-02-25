create database bankmanagement;
use bankmanagement;
create table accounts(
acc_no INT PRIMARY KEY,
name VARCHAR(50),
balance DECIMAL(10,2)
);
insert into accounts values (101, 'Ravi', 0),(102, 'Priya', 0),(103, 'preethi', 0),(104, 'keerthi', 0),(105, 'rithu', 0);
select * from accounts;

create table transactions (
trans_id INT AUTO_INCREMENT PRIMARY KEY,
acc_no INT,
trans_type VARCHAR(20),
amount DECIMAL(10,2),
date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY (acc_no) REFERENCES accounts(acc_no)
);

insert into transactions (acc_no, trans_type, amount) values
(101, 'DEPOSIT', 2000);

UPDATE accounts SET balance = balance + 2000 WHERE acc_no = 101;

SELECT balance FROM accounts WHERE acc_no = 101;

insert into transactions (acc_no, trans_type, amount) values
(102, 'DEPOSIT', 3000);

UPDATE accounts SET balance = balance + 3000 WHERE acc_no = 102;

SELECT balance FROM accounts WHERE acc_no = 102;

insert into transactions (acc_no, trans_type, amount) values
(103, 'DEPOSIT', 4000);

UPDATE accounts SET balance = balance + 4000 WHERE acc_no = 103;

SELECT balance FROM accounts WHERE acc_no = 103;

insert into transactions (acc_no, trans_type, amount) values
(104, 'DEPOSIT', 1500);

UPDATE accounts SET balance = balance + 1500 WHERE acc_no = 104;

SELECT balance FROM accounts WHERE acc_no = 104;

insert into transactions (acc_no, trans_type, amount) values
(105, 'DEPOSIT', 4500);

UPDATE accounts SET balance = balance + 4500 WHERE acc_no = 105;

SELECT balance FROM accounts WHERE acc_no = 105;

INSERT INTO transactions (acc_no, trans_type, amount)
VALUES (101, 'WITHDRAW', 500);

UPDATE accounts SET balance = balance - 500 WHERE acc_no = 101;

SELECT * FROM transactions WHERE acc_no = 101;
SELECT * FROM accounts WHERE acc_no = 101;

-- 103 account to 104 account
-- sender withdraw
insert into transactions (acc_no, trans_type, amount)values(103, 'TRANSFER OUT', 2000);
UPDATE accounts SET balance = balance - 2000 WHERE acc_no = 103;
SELECT balance FROM accounts WHERE acc_no = 103;

-- receiver deposit
insert into transactions (acc_no, trans_type, amount)values(104, 'TRANSFER 	IN', 2000);
UPDATE accounts SET balance = balance + 2000 WHERE acc_no = 104;
SELECT balance FROM accounts WHERE acc_no = 104;

SELECT * FROM accounts WHERE acc_no IN (103,104);

