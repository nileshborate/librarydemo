
from django.urls import path
from . views import *
urlpatterns = [
    path('member/',MemberAPI.as_view() ),
    path('book/',BookAPI.as_view() ),
    path('loan/',LoanAPI.as_view() ),
    path('register/',RegisterUser.as_view() ),
]