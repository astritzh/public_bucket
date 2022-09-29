"""
    Script used to query Cardano staking address rewards

    Uses blockfrost python skd
"""
import sys
from pycardano import *
from pathlib import Path
from blockfrost import BlockFrostApi, ApiError, ApiUrls

if len(sys.argv) != 2:
    print("Usage: {0} staking_address".format(sys.argv[0]))
    sys.exit(0)

network = Network.TESTNET

bf_key = Path('blockfrost.key').read_text().rstrip()

api = BlockFrostApi(project_id=bf_key, base_url=ApiUrls.testnet.value)

account_rewards = api.account_rewards(
        stake_address=sys.argv[1],
        count=20,
        gather_pages=True, # will collect all pages
)
print(f"###### Staking rewards for {address}")
for r in account_rewards:
    print(r)
