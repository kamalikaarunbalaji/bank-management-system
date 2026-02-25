import { useState } from "react";

function Checkbalance() {

  const [accNo, setAccNo] = useState(null);
  const [balance, setBalance] = useState(null);

  const getBalance = () => {
    fetch("http://localhost:5000/balance/" + accNo)
      .then(res => res.json())
      .then(data => setBalance(data.balance));
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h2>Check Balance</h2>

      <input
        placeholder="Enter Account No"
        onChange={(e) => setAccNo(e.target.value)}style={{ padding: "8px", marginBottom: "10px" }}
      />

      <button onClick={getBalance}style={{ padding: "8px 16px", cursor: "pointer" }}>check</button>
      
      <h3>Balance: {balance}</h3>
    </div>
  );
}

export default Checkbalance;