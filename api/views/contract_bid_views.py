from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.contract_bid import ContractBid
from ..serializers import ContractBidSerializer
from ..serializers import SpecialContractBidSerializer


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

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['owner'] = request.user.id
        # Serialize/create contract_bid
        contract_bid = SpecialContractBidSerializer(data=request.data)
        # If the contract_bid data is valid according to our serializer...
        if contract_bid.is_valid():
            # Save the created contract_bid & send a response
            contract_bid.save()
            return Response({ 'contract_bid': contract_bid.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(contract_bid.errors, status=status.HTTP_400_BAD_REQUEST)    

class ContractBidDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the contract_bid to show
        contract_bid = get_object_or_404(ContractBid, pk=pk)
        # Only want to show owned contracts?
        # if request.user != contract_bid.owner:
        #     raise PermissionDenied('Unauthorized, you do not own this contract_bid')

        # Run the data through the serializer so it's formatted
        data = ContractBidSerializer(contract_bid).data
        return Response({ 'contract_bid': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate contract_bid to delete
        contract_bid = get_object_or_404(ContractBid, pk=pk)
        # Check the contract_bid's owner against the user making this request
        if request.user != contract_bid.owner:
            raise PermissionDenied('Unauthorized, you do not own this contract_bid')
        # Only delete if the user owns the contract_bid
        contract_bid.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Contract
        # get_object_or_404 returns a object representation of our Contract
        contract_bid = get_object_or_404(ContractBid, pk=pk)
        # Check the contract_bid's owner against the user making this request
        # if request.user != contract_bid.owner:
        #     raise PermissionDenied('Unauthorized, you do not own this contract_bid')

        # Ensure the owner field is set to the current user's ID
        request.data['owner'] = request.user.id
        # Validate updates with serializer
        data = SpecialContractBidSerializer(contract_bid, data=request.data, partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
    