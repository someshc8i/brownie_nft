from scripts.helpful_scripts import OPENSEA_URL, get_account
from brownie import SimpleCollectible

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def deploy_and_create():
    account = get_account()
    simple_collectible = SimpleCollectible.deploy({'from': account})
    token_id = simple_collectible.tokenCounter()
    tx = simple_collectible.createCollectible(
        sample_token_uri, {'from': account})
    tx.wait(1)
    print(
        f"Awesome you can view this nft on {OPENSEA_URL.format(simple_collectible.address, token_id)}")
    return simple_collectible


def main():
    deploy_and_create()
