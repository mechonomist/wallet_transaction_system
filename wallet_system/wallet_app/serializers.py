from rest_framework import serializers
from .models import Wallet, Transactions
from rest_framework.validators import UniqueValidator


class TransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = '__all__'


class WalletSerializer(serializers.ModelSerializer):
    transactions_by_user = TransactionsSerializer(read_only=True, many=True)
    wallet_id = serializers.EmailField(validators=[UniqueValidator(queryset=Wallet.objects.all())])

    class Meta:
        model = Wallet
        fields = '__all__'
