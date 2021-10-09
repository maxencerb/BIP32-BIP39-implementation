import argparse
from create_seed import create_seed, get_mnemonic, get_hex
from generate_wallet import import_mnemonic, is_seed_valid, get_masters

def log_new_seed():
    seed = create_seed()
    mnemonic = get_mnemonic(seed)
    print('Your seed is: {}'.format(get_hex(seed)))
    print('Your mnemonic is: {}'.format(mnemonic))

def check_mnemonic(mnemonic):
    seed = ''
    try:
        seed = import_mnemonic(mnemonic)
    except ValueError as e:
        print(f'Invalid mnemonic : {e}')
        return False
    if is_seed_valid(seed):
        print('Your seed {} is valid'.format(get_hex(seed)))
    else:
        print('Your mnemonic is invalid')
        return False
    return seed

def get_master_keys(mnemonic):
    private, public, chain_code = get_masters(mnemonic)
    print('Private key: {}'.format(private.hex()))
    print('Public key: {}'.format(public.hex()))
    print('Chain code: {}'.format(chain_code.hex()))

def main():
    parser = argparse.ArgumentParser('Python implementation of a Bitcoin HDWallet')
    parser.add_argument('-i', '--init', action='store_true', help='Initialize a new wallet by returning a securely random bitcoin seed and its mnemonic')
    parser.add_argument('-m', '--mnemonic', metavar='mnemonic', nargs='*', help='Import the 12 words mnemonic')
    parser.add_argument('-cm', '--check-mnemonic', action='store_true', help='Check if a mnemonic is valid')
    parser.add_argument('-mk', '--master-keys', action='store_true',help='Generate a master keys from a mnemonic')
    args = parser.parse_args()

    if args.init:
        log_new_seed()
    elif args.mnemonic:

        mnemonic = ' '.join(args.mnemonic)
        seed = check_mnemonic(mnemonic)

        if seed:

            if args.master_keys:
                get_master_keys(mnemonic)
   
    else:
        print('No mnemonic provided')
        parser.print_help()


if __name__ == '__main__':
    main()