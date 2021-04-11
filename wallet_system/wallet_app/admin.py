from django.contrib import admin
from .models import Wallet, Transactions


class WalletAdmin(admin.ModelAdmin):
    list_display = ('wallet_id', 'current_balance')


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('transaction_id', 'wallet', 'transaction_type', 'transaction_amount',)


admin.site.register(Wallet, WalletAdmin)
admin.site.register(Transactions, TransactionAdmin)
