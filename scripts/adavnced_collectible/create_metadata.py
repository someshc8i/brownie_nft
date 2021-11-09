from brownie import AdvancedCollectible, network
from scripts.helpful_scripts import get_breed
from metadata.sample_metadata import metadata_template
from pathlib import Path
import requests
import json
import os

# breed_to_image_uri = {
#     ''
# }


def main():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_advanced_collectibles = advanced_collectible.tokenCounter()
    print(f"you have created {number_of_advanced_collectibles} collectibles")

    for token_id in range(number_of_advanced_collectibles):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        metadata_file_name = f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        collectible_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print('Already exists')
        else:
            print(f'creating metadata fie {metadata_file_name}')
            collectible_metadata['name'] = breed
            collectible_metadata['desctiption'] = 'Adorable'
            image_path = './img/' + breed.lower().replace('_', '-') + '.png'
            # OPTMIZATION
            # image_uri = None
            # if os.getenv('UPLOAD_IPFS') == 'true':
            #     image_uri = image_uri if image_uri else breed_to_image_uri[breed]
            image_uri = upload_to_ipfs(image_path)
            collectible_metadata['image_uri'] = image_uri
            with open(metadata_file_name, 'w') as file:
                json.dump(collectible_metadata, file)
            upload_to_ipfs(metadata_file_name)


def upload_to_ipfs(filepath):
    with Path(filepath).open('rb') as fp:
        image_binary = fp.read()
        ipfs_url = 'http://127.0.0.1:5001'
        endpoint = '/api/v0/add'
        response = requests.post(
            ipfs_url + endpoint, files={"file": image_binary})
        ipfs_hash = response.json()['Hash']
        filename = filepath.split('/')[-1:][0]
        image_uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        print(image_uri)
        return image_uri
