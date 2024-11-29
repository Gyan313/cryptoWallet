# Crypto Wallet

## What are different types of crypto wallet ?
1. [creating a very basic crypto-wallet from scratch](<https://www.askpython.com/resources/build-crypto-wallet-python#:~:text=Once%20you've%20generated%20the,Signature%20Algorithm)%20library%20in%20Python.>)
    - Mainly 2 types of crypto wallet: 
        - Hot wallet --- connected to internet (vulnerable)
        - cold wallet ---- not connected to internet, like a piece of paper (QR) or hardware device.

## what do you mean by crypto wallet ?
* at the most basic level :
    - stores --->  digital assets ( Wallets don't "store" cryptocurrency; they store the keys that allow access to funds recorded on the blockchain )
    - allow ----> send, receive, and monitor your funds.
* three fundamental components of a wallet: 
    - private key ( give access to funds & sign tranx ) ( 256 bits number == 32 bytes)
    - public key ( generated from private key )
    - address ( generated usign public key )
* "Creating a new Ethereum account" means generating a unique, new wallet address on the Ethereum blockchain, which is essentially a string of characters that acts like your "digital mailbox" where you can receive and send Ether (ETH) cryptocurrency; this address is automatically generated when you set up a new Ethereum wallet on a platform like MetaMask, and is used to identify your account on the network.


## how can i create a crypto cli wallet ?
### Create cli wallet for ethereum first
---

1. need the python library web3.py to interact with ethereum blockchain network.

---------

2. setup an eth node ----->
    - not with google cloud for now, as it requires me to put in the payment details.
    - Recommended Path for You: ( chatgpt )
        - Start with Infura to quickly build and test your CLI wallet. 
        - Once you are comfortable with blockchain basics, experiment with Ganache to simulate blockchain locally for testing.
        - Later, explore full-node clients like Geth for more advanced projects.
    - So, for now using **infura.io**.

----------

3. Create wallet using python.
    * What are the basic function of a crypto-wallet ?

        - Private Key Generation 
            - private_key ----> from a cryptographic algorithm.
            - public_key -----> one-way cryptographic function ----> func(private_key)
            - wallet_address ----> public_key hashed to get the produce a wallet address. Short, human-readable.

            - You must always use local_private_keys ( saved locally on my machine ) when working with nodes hosted by someone else, as i am using infura node.

            - Why we only need private key? 
                - cause, with private_key we can generate a public_key
                - then, with public_key you can generate a wallet_address easily.
        
        - mnemonic phrase
            - generate private_key using mnemonic phrase.
            - user needs to save this phrase, somewhere safe, cause it will generate the private_keys.
            



## Blockchain related libraries I used in this project.
1. [eth_keys](https://github.com/ethereum/eth-keys)
2. [web3.py](https://web3py.readthedocs.io/en/stable/) -----> contains the *eth_keys* library.
3. [hdwallet](https://hdwallet.readthedocs.io/en/v3.0.1/toctree.html)

