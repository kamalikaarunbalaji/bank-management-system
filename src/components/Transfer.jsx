import { useState } from "react";

function Transfer() {
  const [fromAcc, setFromAcc] = useState(null);
  const [toAcc, setToAcc] = useState(null);
  const [amount, setAmount] = useState(null);

  const transfer = () => {
    fetch("http://127.0.0.1:5000/transfer", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({
        from_acc: fromAcc,
        to_acc: toAcc,
        amount: amount
      })
    })
    .then(res => res.json())
    .then(data => alert(data.message));
  };

  return (
    <div style={{ textAlign: "center", marginTop: "50px" }}>
      <h3>Transfer</h3>
      <input placeholder="From Account" onChange={(e)=>setFromAcc(e.target.value)}style={{ padding: "8px", marginBottom: "10px" }} />
      <input placeholder="To Account" onChange={(e)=>setToAcc(e.target.value)}style={{ padding: "8px", marginBottom: "10px" }} />
      <input placeholder="Amount" onChange={(e)=>setAmount(e.target.value)}style={{ padding: "8px", marginBottom: "10px" }} />
      <button onClick={transfer}style={{ padding: "8px 16px", cursor: "pointer" }}>Transfer</button>
    </div>
  );
}

export default Transfer;