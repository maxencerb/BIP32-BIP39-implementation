# BIP 32 and BIP 39 implementation

First install dependencies from `requirements.txt` file.

## Create a valid mnemonic

```bash
python3 wallet.py -i
# or
python3 wallet.py --init
```

it is going to return a valid mnemonic with its 132 bits seed :

```bash
Your seed is: 0x588974958f99c706f09e095ba961d8a31
Your mnemonic is: flat entry century busy organ lock second scorpion forum enrich involve economy
```

## Check the mnemonic validity

```bash
python3 wallet.py -m flat entry century busy organ lock second scorpion forum enrich involve economy
# or
python3 wallet.py --mnemonic flat entry century busy organ lock second scorpion forum enrich involve economy
```

It will return our 132 bits seed if it is a valid seed:

```bash
Your seed 0x588974958f99c706f09e095ba961d8a31 is valid
```

If the mnemonic is invalid, it is going to return with an error.

## Get the master private / public key and chain code

```bash
python3 wallet.py -m flat entry century busy organ lock second scorpion forum enrich involve economy --master-keys
```

It will return the keys :

```bash
Your seed 0x588974958f99c706f09e095ba961d8a31 is valid
Private key: 3e8d145e3fee76b4d2d26aa95bbebd4269fdff218631cfc170af3bee1d2976bd
Public key: fe0b339e0b8d0d58cb9a91c3bb467f729895b0875d1884b29c970cdffd889e1b9ff2773c0457d15b97d887a6dd38b2cfe4044e4d3686ae03fda06015dec6f8b4
Chain code: 2fec02e9462718b592f763eb2b8b9b390c51dfbe001506cf2ee642e888939e3d
```
