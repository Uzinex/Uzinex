from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Transaction
from .serializers import TransactionSerializer


class TransactionViewSet(viewsets.ModelViewSet):
    """Stub transaction endpoints for holding and releasing funds."""
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all().select_related('contract')
    permission_classes = [permissions.IsAuthenticated]

    @action(detail=True, methods=['post'])
    def hold(self, request, pk=None):
        transaction = self.get_object()
        transaction.status = 'held'
        transaction.save(update_fields=['status'])
        return Response({'status': 'held'})

    @action(detail=True, methods=['post'])
    def release(self, request, pk=None):
        transaction = self.get_object()
        transaction.status = 'released'
        transaction.save(update_fields=['status'])
        return Response({'status': 'released'})
