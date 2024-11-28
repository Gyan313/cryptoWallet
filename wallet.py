import os
from web3 import Web3
from dotenv import load_dotenv

# fetch the environment variables.
load_dotenv()

REMOTE_NODE_PROVIDER_API_KEY = os.getenv("INFURA_API_KEY")

# connected to the ethereum network.
w3 = Web3(
    Web3.HTTPProvider(f"https://sepolia.infura.io/v3/{REMOTE_NODE_PROVIDER_API_KEY}")
)

# creating a new eth-account.
# generate the key_pair.
# private_key (local_private_key) ----> You must always use local private keys when working with nodes hosted by someone else, as i am using infura node.

# this will create a new account for me.
_account = w3.eth.account.create()

# note: i only needs to save the private_key as we can get the wallet_address from the key.
wallet_address = _account.address
# as private_key we get is initally in python byte object, so to convert it into hexadecimal number, there is a method provided by web3.py lib, which is to_hex.
private_key = w3.to_hex(_account.key)

print(f"new-eth-account address: {wallet_address}\nprivate_key: {(private_key)}")
