import uuid

from .models import Wallet


def generate_transaction_record(wallet, transaction_type, transaction_amount, new_wallet=False):
    transaction_id = str(uuid.uuid4())
    current_balance = wallet.current_balance

    if new_wallet:
        wallet_opening_balance = 0
    else:
        wallet_opening_balance = current_balance

    if transaction_type == 'Credit':
        wallet_closing_bal = wallet_opening_balance + transaction_amount
    else:
        wallet_closing_bal = wallet_opening_balance - transaction_amount

    transaction_dict = {
                        "transaction_id": transaction_id,
                        "wallet": wallet,
                        "transaction_type": transaction_type,
                        "transaction_amount": transaction_amount,
                        "wallet_opening_bal": wallet_opening_balance,
                        "wallet_closing_bal": wallet_closing_bal
                        }

    return transaction_dict
