from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.decorators import api_view,APIView
from knox.auth import AuthToken
from accounts.models import LeadModel
from .serailizers import LeadSerializer
from rest_framework import viewsets
from rest_framework import permissions

class LeadViewset(viewsets.ModelViewSet):
    serializer_class = LeadSerializer
    permission_classes = [
        permissions.IsAuthenticated
    ]

    def get_queryset(self):
        return self.request.user.leads.all()
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)




# @api_view(['POST'])
# def login_api(request):
#     serializer=AuthTokenSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     user=serializer.validated_data['user']
#     _,token=AuthToken.objects.create(user)
#     return Response({
#             'user_info':{
#                 'id':user.id,
#                 'username':user.username,
#                 'email':user.email
#             },
#             'token':token,
#             }
#             )


# @api_view(['GET'])
# def get_user_data(request):
#     user=request.user
#     print(user)
#     if user.is_authenticated:
#         return Response({
#              'user_info':{
#                 'id':user.id,
#                 'username':user.username,
#                 'email':user.email
#             }
#         }

#         )
#     return Response({"error":"not authenticated"},status=400)
    
