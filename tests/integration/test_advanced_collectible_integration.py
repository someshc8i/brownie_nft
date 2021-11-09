from scripts.helpful_scripts import LOCAL_BLOCKCHAIN_ENVIRONMENTS, get_account, get_contract
from brownie import network
import pytest
import time
from scripts.adavnced_collectible.deploy import deploy_and_create


def test_can_create_advanced_collectible_integration():
    if network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        pytest.skip()
    advanced_collectible, tx = deploy_and_create()
    time.sleep(60)
    assert advanced_collectible.tokenCounter() == 1
