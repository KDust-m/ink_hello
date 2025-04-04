import time
import random
from web3 import Web3

# === 사용자 설정 ===
rpc_url = "https://rpc-gel.inkonchain.com"  # 정확한 RPC URL로 교체 필요
private_key = "your private key"  # 개인 키
contract_address = "0xc867DC30BF41FA4ddee2d94d0ab82836102B32D3"

# Web3 연결
web3 = Web3(Web3.HTTPProvider(rpc_url))
account = web3.eth.account.from_key(private_key)
from_address = account.address

# ABI (hello() 함수만 포함된 최소 ABI)
contract_abi = [
    {
        "inputs": [],
        "name": "hello",
        "outputs": [],
        "stateMutability": "nonpayable",
        "type": "function"
    }
]

# 컨트랙트 인스턴스 생성
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

# === 무한 루프 반복 실행 ===
while True:
    try:
        # nonce
        nonce = web3.eth.get_transaction_count(from_address)

        # 트랜잭션 생성
        transaction = contract.functions.hello().build_transaction({
            'chainId': web3.eth.chain_id,
            'gas': 25000,
            'gasPrice': web3.to_wei('0.01', 'gwei'),
            'nonce': nonce
        })

        # 트랜잭션 서명
        signed_txn = web3.eth.account.sign_transaction(transaction, private_key)

        # 전송 (속성명 수정)
        tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)

        print(f"📨 트랜잭션 해시: {web3.to_hex(tx_hash)}")
    except Exception as e:
        print(f"⚠️ 에러 발생: {e}")

    # 5~30초 사이 무작위 대기
    delay = random.randint(5, 30)
    print(f"⏱️ 다음 실행까지 대기: {delay}초")
    time.sleep(delay)