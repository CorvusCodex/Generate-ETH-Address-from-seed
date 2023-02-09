from eth_keys import keys
from eth_keys.datatypes import SeedPhrase

def generate_address(seed_phrase):
    seed = SeedPhrase(seed_phrase)
    private_key = keys.PrivateKey.derive_from_seed(seed)
    public_key = private_key.public_key
    address = public_key.to_address()
    return address

seed_phrase = "apple quality pie pen crowd welcome album tornado prize angle sword crumble"
address = generate_address(seed_phrase)
print("Address:", address)
