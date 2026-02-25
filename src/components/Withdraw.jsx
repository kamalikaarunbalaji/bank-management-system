import { useState } from "react";

function Withdraw() {
  const [accNo, setAccNo] = useState(null);
  const [amount, setAmount] = useState(null);

  const withdraw = () => {
    fetch("http://127.0.0.1:5000/withdraw", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({ acc_no: accNo, amount: amount })
    })
    .then(res => res.json())
    .then(data => alert(data.message));
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h3>Withdraw</h3>
      <input placeholder="Account No" onChange={(e)=>setAccNo(e.target.value)}style={{ padding: "8px", marginBottom: "10px" }} />
      <input placeholder="Amount" onChange={(e)=>setAmount(e.target.value)}style={{ padding: "8px", marginBottom: "10px" }} />
      <button onClick={withdraw}style={{ padding: "8px 16px", cursor: "pointer" }}>Withdraw</button>
    </div>
  );
}

export default Withdraw;