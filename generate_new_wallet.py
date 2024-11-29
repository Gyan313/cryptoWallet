# to generate wallet -----> to create a new private key.
# cause, with private_key i can get public_key.
# and with public_key i can get wallet_address.

# Private Key
"""
1. A private key is just a random unguessable, or cryptographically safe, 256-bit integer number

2.A valid private key is > 0 and < max private key value (a number above the elliptic curve order FFFFFFFF FFFFFFFF FFFFFFFF FFFFFFFE BAAEDCE6 AF48A03B BFD25E8C D0364141)

3. Private keys do not have checksums.
"""

from web3 import Web3
from dotenv import set_key
from datetime import datetime

# create a new eth account, along with private_key and address for the account.
_account = Web3().eth.account.create()

# storing the private key in .env file with current datetime value
key_env_name = f"PRIVATE_KEY_{datetime.now().strftime("%m_%d_%Y__%H_%M_%S")}"

# Web3().eth.account.create(): generate private_key ( byte type ).
# But, we need hex type string for blockchain.
value_to_store = Web3().to_hex(_account.key)

# set the private key in the environment variable.
set_key(dotenv_path=".env", key_to_set=key_env_name, value_to_set=value_to_store)


# generate all the keys with a mneumonic phrase, we are creating a HD_wallet.
