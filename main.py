import asyncio
import uvloop
import sys
import os
from web3 import Web3
from dotenv import load_dotenv
from paloma_sdk.client.lcd import AsyncLCDClient
from paloma_sdk.key.mnemonic import MnemonicKey

NODE = "https://bsc-dataseed.binance.org"
CHAIN_TYPE = "evm"
CHAIN_REFERENCE_ID = "bnb-main"
GRAIN = "0xb895f485F4575BC9f6C1b371cAa18F755D85C498"
TOKEN = sys.argv[1]
JOB_ID = "uniswap_pool_create"
load_dotenv()
PALOMA_MNEMONIC = os.environ["PALOMA_MNEMONIC"]


async def main():
    w3: Web3 = Web3(Web3.HTTPProvider(NODE))
    factory_address = "0xcA143Ce32Fe78f1f7019d7d551a6402fC5350c73"
    abi = [{
        "constant": False,
        "inputs": [
            {
                "internalType": "address",
                "name": "tokenA",
                "type": "address"
            },
            {
                "internalType": "address",
                "name": "tokenB",
                "type": "address"
            }
        ],
        "name": "createPair",
        "outputs": [
            {
                "internalType": "address",
                "name": "pair",
                "type": "address"
            }
        ],
        "payable": False,
        "stateMutability": "nonpayable",
        "type": "function"
    }]
    factory_contract = w3.eth.contract(address=factory_address, abi=abi)
    payload = factory_contract.encodeABI(
        "createPair", [GRAIN, TOKEN]
        )[2:]

    paloma = AsyncLCDClient(
        url="https://lcd.testnet.palomaswap.com/",
        chain_id="paloma-testnet-15"
    )
    acc = MnemonicKey(mnemonic=PALOMA_MNEMONIC)
    wallet = paloma.wallet(acc)
    job_id = "uniswap_pool_create"

    result = await paloma.job_scheduler.execute_job(
        wallet, job_id, payload)
    print(result)

    await paloma.session.close()


uvloop.install()
asyncio.run(main())
