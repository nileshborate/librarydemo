from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class RegisterUser(APIView):
    def post(self,request):
        serializer = UserSerializer(data = request.data)

        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors,'message':'Invalid input'})
        serializer.save()

        user = User.objects.get(username=serializer.data['username'])
        token_obj , _ = Token.objects.get_or_create(user=user)
        return Response({'status':200,'payload':serializer.data,'token':str(token_obj),'message':'User added Successfully'})
    
class MemberAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        if request.GET.get('id'):
            member_objs = Member.objects.get(id=request.GET.get('id'))
            serializer = MemberSerializer(member_objs)
        else:
            member_objs = Member.objects.all()
            serializer = MemberSerializer(member_objs,many=True)
        return Response({'status':200,'payload':serializer.data})
    

    def post(self,request):
        serializer = MemberSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403,'errors':serializer.errors,'message':'Invalid input'})
        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':'Member added Successfully'})
    
    #to update whole data
    def put(self,request):
        pass
    
    #to update the partial data
    def patch(self,request):
        try:
            member_obj = Member.objects.get(id=request.data['id'])
            #partial = FAlse for PUT method
            serializer = MemberSerializer(member_obj,data=request.data,partial=True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'errors':serializer.errors,'message':'Invalid input'})
            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':'Member updated Successfully'})
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'Invalid Id'})
    
    def delete(self,request):
        try:
            id = request.GET.get('id')
            member_objs = Member.objects.get(id=id)
            member_objs.delete()
            return Response({'status':200,'message':'deleted'})
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'Invalid id'})
    

class BookAPI(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        if request.GET.get('id'):
            Book_objs = Book.objects.get(id=request.GET.get('id'))
            serializer = BookSerializer(Book_objs)
        else:
            Book_objs = Book.objects.all()
            serializer = BookSerializer(Book_objs,many=True)
        return Response({'status':200,'payload':serializer.data})
    

    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403,'errors':serializer.errors,'message':'Invalid input'})
        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':'Book added Successfully'})
    
    #to update whole data
    def put(self,request):
        pass
    
    #to update the partial data
    def patch(self,request):
        try:
            Book_obj = Book.objects.get(id=request.data['id'])
            #partial = FAlse for PUT method
            serializer = BookSerializer(Book_obj,data=request.data,partial=True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'errors':serializer.errors,'message':'Invalid input'})
            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':'Book updated Successfully'})
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'Invalid Id'})
    
    def delete(self,request):
        try:
            id = request.GET.get('id')
            Book_objs = Book.objects.get(id=id)
            Book_objs.delete()
            return Response({'status':200,'message':'deleted'})
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'Invalid id'})

class LoanAPI(APIView):

    def get(self,request):
        if request.GET.get('id'):
            Loan_objs = Loan.objects.get(id=request.GET.get('id'))
            serializer = LoanSerializer(Loan_objs)
        else:
            Loan_objs = Loan.objects.all()
            serializer = LoanSerializer(Loan_objs,many=True)
        return Response({'status':200,'payload':serializer.data})
    

    def post(self,request):
        serializer = LoanSerializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403,'errors':serializer.errors,'message':'Invalid input'})
        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':'Loan added Successfully'})
    
    #to update whole data
    def put(self,request):
        pass
    
    #to update the partial data
    def patch(self,request):
        try:
            Loan_obj = Loan.objects.get(id=request.data['id'])
            #partial = FAlse for PUT method
            serializer = LoanSerializer(Loan_obj,data=request.data,partial=True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'errors':serializer.errors,'message':'Invalid input'})
            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':'Loan updated Successfully'})
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'Invalid Id'})
    
    def delete(self,request):
        try:
            id = request.GET.get('id')
            Loan_objs = Loan.objects.get(id=id)
            Loan_objs.delete()
            return Response({'status':200,'message':'deleted'})
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'Invalid id'})
