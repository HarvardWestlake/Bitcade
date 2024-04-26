WalletConnect.js

The WalletConnect.js file is a React component that allows users to connect their Ethereum wallet to the application. When a user clicks a button (not shown in this code), the connectWallet function is called. This function asks the user's Ethereum provider (like MetaMask) for access to their account. If the user grants access, the function fetches the user's Ethereum address and balance. The balance is fetched from a local server running on http://localhost:3001. The component also contains a function to format the Ethereum address for display. The balance is fetched again whenever the wallet address changes.

server.js

The server.js file sets up a server that listens for new blocks on the Ethereum blockchain. When a new block is found, it checks each transaction in that block. If a transaction is sent to a specific address (monitoredAddress), it updates the sender's balance. The server uses Express.js for handling requests and the ethers.js library to interact with the Ethereum blockchain. The server listens on a port defined by the environment variable PORT or defaults to 3001 if PORT is not set.

Currently, the server looks for transactions coming to a pre-defined wallet, but for our application, it should probably be used for other tasks like getting ERC20 balance of a user, etc.

Header.js

The Header.js file defines a React component named Header. This component displays a header bar with three sections: a title on the left ("Blocade"), the user's Ethereum balance in the middle, and a WalletConnect component on the right. The WalletConnect component is used to connect the user's Ethereum wallet to the application. The Header component uses React's useState hook to store the user's balance, and passes a function to set this balance (setBalance) to the WalletConnect component.