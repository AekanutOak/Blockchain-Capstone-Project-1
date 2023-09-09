if (typeof web3 !== 'undefined') {
    
    const loginButton = document.getElementById('connect-metamask');
    // Attach a click event listener to the login button
    loginButton.addEventListener('click', async () => {
      try {
        // Request the user's permission to access their Ethereum accounts
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        
        // User granted permission, you can now access their accounts and perform actions
        const web3 = new Web3(window.ethereum);
        
        // Example: Get the user's Ethereum address
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];
        
        window.location.href = `homepage.html?userAddress=${userAddress}`;
        // You can now use 'userAddress' and perform Ethereum-related actions
        console.log(`Logged in with address: ${userAddress}`);
      } catch (error) {
        console.error('Error logging in with MetaMask:', error);
      }
    });
  } else {
    console.error('MetaMask is not installed.');
  }