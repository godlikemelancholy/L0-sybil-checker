from loguru import logger


with open('core/wallets.txt', 'r', encoding='utf-8') as file:
    wallets = [line.strip() for line in file]


with open('core/sybil_wallets.txt', 'r', encoding='utf-8') as file:
    sybil_wallets = [line.strip() for line in file]


with open('core/result.txt', 'w', encoding='utf-8') as result:
    for wallet in wallets:
        if wallet.lower() in sybil_wallets:
            logger.success(f"Found new wallet - {wallet}")
            result.write(wallet + '\n')


