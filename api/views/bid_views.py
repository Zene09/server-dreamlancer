from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework import generics, status
from django.shortcuts import get_object_or_404

from ..models.bid import Bid
from ..serializers import BidSerializer


# Create your views here.
class Bids(generics.ListCreateAPIView):
    permission_classes=(IsAuthenticated,)
    serializer_class = BidSerializer
    def get(self, request):
        """Index request"""
        # Get all the bids:
        bids = Bid.objects.all()
        # Filter the bids by owner, so you can only see your owned bids
        # bids = Bid.objects.filter(owner=request.user.id)
        # Run the data through the serializer
        data = BidSerializer(bids, many=True).data
        return Response({ 'bids': data })

    def post(self, request):
        """Create request"""
        # Add user to request data object
        request.data['bid']['owner'] = request.user.id
        # Serialize/create bid
        bid = BidSerializer(data=request.data['bid'])
        # If the bid data is valid according to our serializer...
        if bid.is_valid():
            # Save the created bid & send a response
            bid.save()
            return Response({ 'bid': bid.data }, status=status.HTTP_201_CREATED)
        # If the data is not valid, return a response with the errors
        return Response(bid.errors, status=status.HTTP_400_BAD_REQUEST)

class BidDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request, pk):
        """Show request"""
        # Locate the bid to show
        bid = get_object_or_404(Bid, pk=pk)
        # Only want to show owned bids?
        if request.user != bid.owner:
            raise PermissionDenied('Unauthorized, you do not own this bid')

        # Run the data through the serializer so it's formatted
        data = BidSerializer(bid).data
        return Response({ 'bid': data })

    def delete(self, request, pk):
        """Delete request"""
        # Locate bid to delete
        bid = get_object_or_404(Bid, pk=pk)
        # Check the bid's owner against the user making this request
        if request.user != bid.owner:
            raise PermissionDenied('Unauthorized, you do not own this bid')
        # Only delete if the user owns the  bid
        bid.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def partial_update(self, request, pk):
        """Update Request"""
        # Locate Bid
        # get_object_or_404 returns a object representation of our Bid
        bid = get_object_or_404(Bid, pk=pk)
        # Check the bid's owner against the user making this request
        if request.user != bid.owner:
            raise PermissionDenied('Unauthorized, you do not own this bid')

        # Ensure the owner field is set to the current user's ID
        request.data['bid']['owner'] = request.user.id
        # Validate updates with serializer
        data = BidSerializer(bid, data=request.data['bid'], partial=True)
        if data.is_valid():
            # Save & send a 204 no content
            data.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        # If the data is not valid, return a response with the errors
        return Response(data.errors, status=status.HTTP_400_BAD_REQUEST)
