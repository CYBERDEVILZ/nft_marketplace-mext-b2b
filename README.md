# NFT MARKETPLACE
POC to implement an **NFT marketplace** in the **MEXT METAVERSE**.

## SUMMARY
**Non-fungible tokens (NFTs)** are cryptographic assets on a blockchain with unique identification codes and metadata that distinguish them from each other.
NFT Marketplace enables any user having a valid cryptocurrency wallet to engage in buying/selling NFTs. This POC aims at demonstrating the working of a simple NFT Marketplace.

## ARCHITECTURE
### Smart Contract
Smart Contract is the backbone of the whole NFT Marketplace. Anything and everything revolves around interacting with the Smart Contract. For those, who doesn't even have the slightest idea about smart contract, it is a self executing piece of code that is deployed on a blockchain.

The Smart Contract for this project is developed using Solidity and deployed on the Polygon blockchain network (to be more precise, on the Mumbai Testnet). Hence, all the transactions that happens should be done over the Polygon network. Polygon has its own cryptocurrency, MATIC, via which we can carry out transactions over the network. Due to very low gas fees and faster transaction rates, Polygon network is preferred in this case. 

### Front-End
The front-end layout is built using plain old HTML and CSS. Web3.js, a library used to interact with Smart Contracts and ethereum nodes, is also utilized to carry out several functionalities like calling contract methods, getting wallet information, and performing transactions.

### Back-End
Authentication is made possible by utilizing Google Firebase, which is a BaaS (Backend as a Service) provider. Flask, a microframework for Python, is used to create a web server over which the NFT Marketplace runs.

## REQUIREMENTS
- Python 3.6+
- MetaMask Wallet
- Git (optional)

## RUN THE PROJECT
Follow the points mentioned below to run the project in your system. If you are lazy enough to read them, kindly navigate down to find a video demo of running the project.

### Create a MetaMask Wallet account
This project utilizes MetaMask wallet to perform transactions over the Polygon Network. If you don't have a MetaMask Wallet, kindly install the extension from your browser marketplace and create an account in it. It is pretty much easy to create an account in MetaMask. All the instructions are provided the moment you install and activate the extension in your browser.

### Add some MATIC to your account
Since transactions that happen over the blockchain requires some gas fees to be paid to the validators (or miners, depending on the consensus used), you must possess some amount of MATIC, which is the cryptocurrency used in Polygon Network.
Since, we are using this project on a Testnet, you can easily get some fake MATIC from the faucet made available here.. [Polygon Faucet](https://faucet.polygon.technology/)

Cryptocurrency over the TestNet are never real and you cannot exchange them for real money!

### Clone the repository
If you are aware of using Git, then you can go ahead and clone this repository to your local desktop. Else, just go ahead and download the zip folder from here and extract the contents. 
