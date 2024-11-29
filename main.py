import os
from web3 import Web3
from dotenv import load_dotenv
from eth_account import Account

# fetch the environment variables.
load_dotenv()

REMOTE_NODE_PROVIDER_API_KEY = os.getenv("INFURA_API_KEY")

# connected to the ethereum network.
w3 = Web3(
    Web3.HTTPProvider(f"https://sepolia.infura.io/v3/{REMOTE_NODE_PROVIDER_API_KEY}")
)
