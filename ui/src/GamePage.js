import { WalletProvider } from "./components/WalletContext"; // Import the provider
import ExampleGameComponent from "./games/ExampleGameComponent"; // Import the game component

function App() {
  return (
    <WalletProvider>
      {" "}
      {/* Wrap the entire application with WalletProvider */}
      <div className="App">
        <Header />
        <div className="content">
          <div className="main-panel" style={{ flex: "70%" }}>
            {/* Main content goes here */ "contentcontent"}
          </div>
        </div>
      </div>
    </WalletProvider>
  );
}

export default App;
