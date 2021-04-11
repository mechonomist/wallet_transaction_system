import urllib
from django.db import transaction
from django.http import Http404
from rest_framework import status as st
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Wallet
from .serializers import WalletSerializer, TransactionsSerializer
from .utils import generate_transaction_record


class WalletView(APIView):

    minimum_wallet_balance = 100

    def get_object(self, wallet_id):
        try:
            return Wallet.objects.get(pk=wallet_id)
        except Wallet.DoesNotExist:
            raise Http404()

    def get(self, request, *args, **kwargs):
        if 'email' in request.query_params:
            email = request.query_params["email"]
            wallet = self.get_object(email)
            current_balance = wallet.current_balance
            return Response({'email': email, "current_balance": current_balance}, status=st.HTTP_200_OK)
        else:
            return Response({'msg': 'Provide valid email to retrieve details'}, status=st.HTTP_405_METHOD_NOT_ALLOWED)

    def post(self, request, *args, **kwargs):
        wallet_serializer = WalletSerializer(data=request.data)
        if wallet_serializer.is_valid():
            email = wallet_serializer.validated_data.get('wallet_id')
            initial_deposit = wallet_serializer.validated_data.get('current_balance')
            if initial_deposit >= self.minimum_wallet_balance:
                wallet = wallet_serializer.save()
                transaction_record = generate_transaction_record(wallet, 'Credit', initial_deposit, True)
                transaction_serializer = TransactionsSerializer(data=transaction_record)
                if transaction_serializer.is_valid():
                    transaction_serializer.save()
                else:
                    return Response(transaction_serializer.errors, status=st.HTTP_400_BAD_REQUEST)
                msg = f'A new wallet account with email {email} has been created'
                status = st.HTTP_201_CREATED
            else:
                msg = 'Deposited amount below minimum balance requirements'
                status = st.HTTP_400_BAD_REQUEST
        else:
            msg = wallet_serializer.errors['wallet_id'][0]
            status = st.HTTP_400_BAD_REQUEST
        return Response({"message": msg}, status)

    def put(self, request, *args, **kwargs):
        email_id = request.data['email']
        transaction_type = request.data['transaction_type']
        transaction_amount = request.data['transaction_amount']

        with transaction.atomic():
            wallet = self.get_object(email_id)
            if transaction_type in ['Credit', 'Debit']:
                if transaction_type == 'Debit' and wallet.current_balance - transaction_amount < self.minimum_wallet_balance:
                    msg = 'Available wallet balance does not support transaction'
                    status = st.HTTP_400_BAD_REQUEST
                else:
                    try:
                        transaction_record = generate_transaction_record(wallet, transaction_type, transaction_amount)
                        transaction_serializer = TransactionsSerializer(data=transaction_record)
                        if transaction_serializer.is_valid():
                            transaction_serializer.save()
                            wallet.current_balance = transaction_record['wallet_closing_bal']
                            wallet.save()
                        else:
                            return Response(transaction_serializer.errors, status=st.HTTP_400_BAD_REQUEST)

                        if transaction_type == 'Credit':
                            msg = f'Amount Credited, current available balance is {wallet.current_balance}'
                        else:
                            msg = f'Amount Debited, current available balance is {wallet.current_balance}'
                        status = st.HTTP_200_OK
                    except Exception:
                        msg = f'Unknown error has occurred'
                        status = st.HTTP_500_INTERNAL_SERVER_ERROR

            else:
                msg = f'Transaction type:{transaction_type} is not valid'
                status = st.HTTP_400_BAD_REQUEST

        return Response({"message": msg}, status)
