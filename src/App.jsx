import Checkbalance from "./components/Checkbalance";
import Deposit from "./components/Deposit";
import Transfer from "./components/Transfer";
import Withdraw from "./components/Withdraw";

function App() {
  return (
    <div style={{textAlign: "center"}}>
      <h1>Bank Management</h1>
      <Checkbalance />
      <Deposit />
      <Transfer />
      <Withdraw />
    </div>
  );
}

export default App;