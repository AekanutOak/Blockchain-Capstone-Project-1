from solcx import compile_standard, install_solc
from web3 import Web3
from random import choice

import json
import os

dirname = os.path.dirname(__file__)
install_solc("0.8.19")

network_address = os.path.join(dirname, '../config/blockchain_network')

with open(network_address,"r") as f:
    network_address = f.read()

w3 = Web3(Web3.HTTPProvider(network_address))

contract_path = os.path.join(dirname, 'product.sol')

with open(contract_path,"r") as f:
    product_contract = f.read()

    complied_Product_contract = compile_standard(
        {
            "language": "Solidity",
            "sources": {"Product.sol": {"content": product_contract}},
            "settings": {
                "outputSelection": {
                    "*": {"*": ["abi", "metadata", "evm.bytecode", "evm.sourceMap"]}
                }
            },
        },
        solc_version="0.8.19",
    )

bytecode_Product = complied_Product_contract["contracts"]["Product.sol"]["Product"][ "evm"]["bytecode"]["object"]
abi_Product = complied_Product_contract["contracts"]["Product.sol"]["Product"]["abi"]

with open(os.path.join(dirname,"complied_Product_contract.json"), "w") as file:
    json.dump(complied_Product_contract, file)

with open(os.path.join(dirname,"abi_Product.json"), "w") as file:
    json.dump(abi_Product, file)

deploy_address = choice(w3.eth.accounts)

Product = w3.eth.contract(abi=abi_Product, bytecode=bytecode_Product)
transaction_Product = Product.constructor().transact({"from": deploy_address})
contract_address_Product = w3.eth.wait_for_transaction_receipt(transaction_Product)

with open(os.path.join(dirname,"contract_address_Product"), "w") as file:
    file.write(contract_address_Product.contractAddress)