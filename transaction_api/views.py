from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Transaction
from .serializers import TransactionSerializer
from django.utils import timezone

@api_view(['POST'])
def transaction_webhook(request):
    serializer = TransactionSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Webhook received successfully"}, status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def healthcheck(request):
  return Response({"message": "HEALTHY", 'current_time': timezone.now()}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_transaction_by_id(request, transaction_id):
  try:
    transaction = Transaction.objects.get(transaction_id=transaction_id)
    serializer = TransactionSerializer(transaction)
    return Response(serializer.data, status=status.HTTP_200_OK)
  except Transaction.DoesNotExist:
    return Response({"error": "Transaction not found"}, status=status.HTTP_404_NOT_FOUND)