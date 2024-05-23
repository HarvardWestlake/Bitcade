import { ethers } from 'ethers';

// Connect Wallet Button
document.getElementById('connectWalletBtn').addEventListener('click', async () => {
    console.log("test")
    if (window.ethereum) {
        try {
            await window.ethereum.request({ method: 'eth_requestAccounts' });
            updateWalletBalance();
        } catch (error) {
            console.error(error);
        }
    } else {
        console.error('MetaMask or another Ethereum wallet extension not detected.');
    }
});

// Start Betting Session Button
document.getElementById('startSessionBtn').addEventListener('click', async () => {
    try {
        await contract.startBettingSession();
        alert('Betting session started successfully!');
    } catch (error) {
        console.error(error);
    }
});

// Play Game Button
document.getElementById('playGameBtn').addEventListener('click', async () => {
    const number = document.getElementById('numberSlider').value;
    try {
        const result = await contract.playGame(number);
        if (result) {
            alert('Congratulations! You won.');
        } else {
            alert('Sorry! You lost.');
        }
    } catch (error) {
        console.error(error);
    }
});

// Cash Out Button
document.getElementById('cashOutBtn').addEventListener('click', async () => {
    try {
        await contract.cashOut();
        alert('Cash out successful!');
    } catch (error) {
        console.error(error);
    }
});

// Function to update wallet balance
async function updateWalletBalance() {
    const accounts = await ethereum.request({ method: 'eth_accounts' });
    const balance = await ethereum.request({ method: 'eth_getBalance', params: [accounts[0]] });
    document.getElementById('walletBalance').innerText = `Your ETH Balance: ${ethers.utils.formatEther(balance)} ETH`;
}

// Sample contract instance (replace with your actual contract)
const contract = new ethers.Contract('YOUR_CONTRACT_ADDRESS', contractABI, ethereum);
