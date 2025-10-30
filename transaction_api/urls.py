from django.urls import path
from .views import transaction_webhook, healthcheck, get_transaction_by_id

urlpatterns = [
    path('healthcheck/', healthcheck, name='healthcheck'),
    path('transactions/', transaction_webhook, name='transaction_webhook'),
    path('transactions/<str:transaction_id>/', get_transaction_by_id, name='get_transaction_by_id'),
]
