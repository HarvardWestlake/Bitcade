const express = require('express');
const { ethers } = require('ethers');

const app = express();

const cors = require('cors');
app.use(cors());

const port = process.env.PORT || 3001;

// Define the wallet address to monitor
const monitoredAddress = '0x8cf6ed9080f3f3f30a6eed14872c82e3cb645a00';

// Set up an ethers.js provider
const provider = new ethers.JsonRpcProvider('https://sepolia.infura.io/v3/ef2d474717a74b92b850a4f3167a5650');

// Function to update the sender's balance in Firebase
async function updateSenderBalance(senderAddress, amount) {
    const walletRef = db.collection('wallets').doc(senderAddress);
    const walletDoc = await walletRef.get();
    let newBalance = ethers.formatEther(amount);
    console.log(senderAddress + " deposited " + newBalance + " ETH")

    if (walletDoc.exists) {
        const currentBalance = walletDoc.data().balance;
        newBalance = ethers.formatEther(ethers.parseEther(currentBalance) + amount);
    }
    console.log(senderAddress + " has " + newBalance + " ETH in balance")

    await walletRef.set({
        balance: newBalance,
    }, { merge: true });
}

// Function to check each transaction in a block
async function checkTransactions(blockNumber) {
    const block = await provider.getBlock(blockNumber);
    for (const txHash of block.transactions) {
      const tx = await provider.getTransaction(txHash);
      if (tx && tx.to && tx.to.toLowerCase() === monitoredAddress.toLowerCase()) {
        await updateSenderBalance(tx.from, tx.value);
      }
    }
  }
  

// Function to listen for new blocks and check transactions
function watchTransactions() {
  provider.on('block', async (blockNumber) => {
    console.log(blockNumber)
    await checkTransactions(blockNumber);
  });
}

// Start watching transactions
watchTransactions();

app.listen(port, () => {
  console.log(`Server is running on port ${port}`);
});

