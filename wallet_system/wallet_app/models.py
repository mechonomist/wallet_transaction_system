from django.db import models

class Wallet(models.Model):
    wallet_id = models.CharField(primary_key=True, max_length=128)  # email_id of the user
    current_balance = models.FloatField()

    def __str__(self):
        return self.wallet_id


class Transactions(models.Model):
    transaction_id = models.CharField(primary_key=True, max_length=64)

    wallet = models.ForeignKey(Wallet, on_delete=models.CASCADE, related_name='transactions_of_user')
    transaction_type = models.CharField(max_length=8, choices=[('Debit', 'Debit'), ('Credit', 'Credit')])
    transaction_amount = models.FloatField()
    wallet_opening_bal = models.FloatField()
    wallet_closing_bal = models.FloatField()


