from django.urls import path
from .views.mango_views import Mangos, MangoDetail
from .views.contract_views import Contracts, ContractDetail
from .views.bid_views import Bids, BidDetail
from .views.contract_bid_views import ContractBids, ContractBidDetail
from .views.user_views import SignUp, SignIn, SignOut, ChangePassword


urlpatterns = [
  	# Restful routing
    path('mangos/', Mangos.as_view(), name='mangos'),
    path('mangos/<int:pk>/', MangoDetail.as_view(), name='mango_detail'),
    path('contracts/', Contracts.as_view(), name='contracts'),
    path('contracts/<int:pk>/', ContractDetail.as_view(), name='contract_detail'),
    path('bids/', Bids.as_view(), name='bids'),
    path('bids/<int:pk>/', BidDetail.as_view(), name='bid_detail'),
    # path('contract_bid/', ContractBids.as_view(), name='contract_bid'),
    path('contract_bid/<int:pk>/', ContractBidDetail.as_view(), name='contract_bid_detail'),
    path('sign-up/', SignUp.as_view(), name='sign-up'),
    path('sign-in/', SignIn.as_view(), name='sign-in'),
    path('sign-out/', SignOut.as_view(), name='sign-out'),
    path('change-pw/', ChangePassword.as_view(), name='change-pw'),
]
