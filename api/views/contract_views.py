from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.contract import Contract
from ..serializers import ContractSerializer


# Create your views here.
class Contracts(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = ContractSerializer
    def get(self, request):
        """Index request"""
        # Get all the contracts:
        # contracts = Contract.objects.all()
        # Filter the contracts by owner, so you can only see your owned contracts
        contracts = Contract.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = ContractSerializer(contracts, many=True).data
        return Response({ 'contracts': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['contract']['owner'] = request.user.id
        # Serialize/create contract
        contract = ContractSerializer(data=request.data['contract'])
        # If the contract data is valid according to our serializer...
        if contract.is_valid():
            # Save the created contract & send a response
            contract.save()
            return Response({ 'contract': contract.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(contract.errors, status=status.HTTP_400_BAD_REQUEST)

class ContractDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the contract to show
        contract = get_object_or_404(Contract, pk=pk)
        # Only want to show owned contracts?
        if request.user != contract.owner:
            raise PermissionDenied('Unauthorized, you do not own this contract')

        # Run the data through the serializer so it's formatted
        data = ContractSerializer(contract).data
        return Response({ 'contract': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate contract to delete
        contract = get_object_or_404(Contract, pk=pk)
        # Check the contract's owner against the user making this request
        if request.user != contract.owner:
            raise PermissionDenied('Unauthorized, you do not own this contract')
        # Only delete if the user owns the  contract
        contract.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Contract
        # get_object_or_404 returns a object representation of our Contract
        contract = get_object_or_404(Contract, pk=pk)
        # Check the contract's owner against the user making this request
        if request.user != contract.owner:
            raise PermissionDenied('Unauthorized, you do not own this contract')

        # Ensure the owner field is set to the current user's ID
        request.data['contract']['owner'] = request.user.id
        # Validate updates with serializer
        data = ContractSerializer(contract, data=request.data['contract'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
