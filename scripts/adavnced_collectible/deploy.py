from scripts.helpful_scripts import OPENSEA_URL, fund_with_link, get_account, get_contract
from brownie import AdvancedCollectible, config, network


def deploy_and_create():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract('vrf_coordinator'),
        get_contract('link_token'),
        config['networks'][network.show_active()]['keyhash'],
        config['networks'][network.show_active()]['fee'],
        {'from': account})
    fund_with_link(advanced_collectible.address)
    tx = advanced_collectible.createCollectible({'from': account})
    tx.wait(1)
    print('new token created')
    return advanced_collectible, tx


def main():
    deploy_and_create()
