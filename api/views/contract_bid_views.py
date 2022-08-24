from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.contract_bid import ContractBid
from ..serializers import ContractBidSerializer


# Create your views here.
class ContractBids(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = ContractBidSerializer
    def get(self, request):
        """Index request"""
        # Get all the contracts:
        contract_bid = ContractBid.objects.all()
        # Filter the contracts by owner, so you can only see your owned contracts
        # contracts = ContractBid.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = ContractBidSerializer(contract_bid, many=True).data
        return Response({ 'contract_data': data })

class ContractBidDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the contract to show
        contract_bid = get_object_or_404(ContractBid, pk=pk)
        # Only want to show owned contracts?
        # if request.user != contract.owner:
        #     raise PermissionDenied('Unauthorized, you do not own this contract')

        # Run the data through the serializer so it's formatted
        data = ContractBidSerializer(contract_bid).data
        return Response({ 'contract_bid': data })

    