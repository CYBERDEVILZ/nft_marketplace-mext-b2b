# 🖼️ &nbsp;&nbsp;NFT MARKETPLACE&nbsp;&nbsp; 🖼️
POC to implement an **NFT marketplace** in the **MEXT METAVERSE**.

## 📚 SUMMARY
**Non-fungible tokens (NFTs)** are cryptographic assets on a blockchain with unique identification codes and metadata that distinguish them from each other.
NFT Marketplace enables any user having a valid cryptocurrency wallet to engage in buying/selling NFTs. This POC aims at demonstrating the working of a simple NFT Marketplace.

## 🏛️ ARCHITECTURE
### 📝 Smart Contract 
Smart Contract is the backbone of the whole NFT Marketplace. Anything and everything revolves around interacting with the Smart Contract. For those, who doesn't even have the slightest idea about smart contract, it is a self executing piece of code that is deployed on a blockchain.

The Smart Contract for this project is developed using Solidity and deployed on the Polygon blockchain network (to be more precise, on the Mumbai Testnet). Hence, all the transactions that happens should be done over the Polygon network. Polygon has its own cryptocurrency, MATIC, via which we can carry out transactions over the network. Due to very low gas fees and faster transaction rates, Polygon network is preferred in this case. 

### 🎇 Front-End 
The front-end layout is built using plain old HTML and CSS. Web3.js, a library used to interact with Smart Contracts and ethereum nodes, is also utilized to carry out several functionalities like calling contract methods, getting wallet information, and performing transactions.

### 🏭 Back-End
Authentication is made possible by utilizing Google Firebase, which is a BaaS (Backend as a Service) provider. Flask, a microframework for Python, is used to create a web server over which the NFT Marketplace runs.

## ✅ REQUIREMENTS
✔️ Python 3.6+   
✔️ MetaMask Wallet   
✖️ Git (optional)

## 🚀 RUN THE PROJECT
Follow the points mentioned below to run the project in your system. If you are lazy enough to read them, kindly navigate down to find a demo video of setting up and running the project.

### 🧾 Create a MetaMask Wallet account
This project utilizes MetaMask wallet to perform transactions over the Polygon Network. If you don't have a MetaMask Wallet, kindly install the extension from your browser marketplace and create an account in it. It is pretty much easy to create an account in MetaMask. All the instructions are provided the moment you install and activate the extension in your browser.

### ⛓️ Add Polygon Chain to wallet
Since the NFT Marketplace has been implemented on the Polygon Blockchain, we need to add this chain to our wallet and switch to the network. For the purpose of testing out this application, I have deployed the contract on the **Polygon Mumbai TestNet**. This is crucial as you can experiment with the application without using real money for transaction purposes. So, go ahead and add the Polygon Mumbai TestNet to your wallet. If you are unfamiliar, navigate to the bottom part of this README to find demo videos.

### 💲 Add some MATIC to your account
Since transactions that happen over the blockchain requires some gas fees to be paid to the validators (or miners, depending on the consensus used), you must possess some amount of MATIC, which is the cryptocurrency used in Polygon Network.
Since, we are using this project on a Testnet, you can easily get some fake MATIC from the faucet made available [here](https://faucet.polygon.technology/)

#### Cryptocurrency over the TestNet are never real and you cannot exchange them for real money!

### ⏬ Clone the repository
If you are aware of using Git, then you can go ahead and clone this repository to your local desktop. Else, just go ahead and download the zip folder from [here](https://github.com/CYBERDEVILZ/nft_marketplace/archive/refs/heads/main.zip) and extract the contents. Make sure you are now inside the folder where all the files of this repository are visible.

### 🔥 Initialize server
In order to initialize the server, we need to do make some arrangements. Firstly, we must create a virtual environment using Python and secondly, install the dependencies inside it. This will save us from dependency conflicts in the future.

#### ⚙️ Create a virtual environment
While inside the folder where you can see other files of this repository, open your terminal / cmd prompt and issue the following command.
```
python -m venv venv
```

In certain cases, if the above command didn't work, you might want to specify the version number along with python as follows.
```
python3 -m venv venv
```
This will create a new folder named `venv` in the current directory.

Now we need to activate the virtual environment. For that, issue the following command inside your terminal / cmd prompt while being in the same directory as the other files of this repository.

**Windows:**
```
venv\Scripts\activate
```

**Linux / MacOS:** 
```
source venv/bin/activate
```

#### ⚙️ Install dependencies
If you take a look at the contents of the repository, you might find a file named `requirements.txt`. This file contains all the dependencies that needs to be installed on your device for smooth functioning of the Python server. So let's go ahead and install them by issuing the following command inside your terminal / cmd prompt while being in the same directory as the other files of this repository.
```
pip install -r requirements.txt
```

#### 🔥 Start the server
After you have successfully performed the above two steps, it is time to fire up the server. Issue the following command inside your terminal / cmd prompt while being in the same directory as the other files of this repository.
```
python flask-nft.py
```

This will spin up a **server on your localhost at port 5000**. Navigate to http://localhost:5000 to see your project running live!

## 📺 Demo Video
### Create a Metamask Wallet Account
https://user-images.githubusercontent.com/55954313/192086056-b3dae06a-2e3d-4be4-9773-1cb3ac8ca54b.mp4


