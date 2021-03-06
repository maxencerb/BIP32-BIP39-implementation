# BIP 32 and BIP 39 implementation

First install dependencies from `requirements.txt` file.

```bash
pip install -r requirements.txt
```

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

## Get the private key with derivation path

```bash
python3 wallet.py -m flat entry century busy organ lock second scorpion forum enrich involve economy -gk m/1/2/3/4/5
```

The option `-gk` or `--get-keys` let you specify the derivation path. The result will be :

```bash
Your seed 0x588974958f99c706f09e095ba961d8a31 is valid
Derivation path: m/1/2/3/4/5
Private key: b019e4c827809b737a0f03efae5c1e24b2cbf7bd684215e04f01e69d7fa5a54c
Public key: a87bf7678305b40c17a70294e1d9da3225107831aa28c402a6b149c929b7355287bac80d20afc61868dcd012a1bb88f47d48b14d8d6dfa6a948f5b69ef8746f4
Chain code: ab8e3b5e402754c401c5b0d3a27b0ecc6a93d5aae8dfb313df7b9847af9c3892
```
