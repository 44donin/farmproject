
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import mongodb



# Create your views here.
@api_view(['GET'])
def GetInformation(request,district,crop):
    data = mongodb.GetExpertSuggestion(district,crop)
    return Response(data)

@api_view(['POST'])
def GetData(request):
    if(request.method == 'POST'):
        data = mongodb.GetExpertSuggestion(district=request.data['District'],crop=request.data['Crop'],language=request.data['LanguageCode'])
        return Response(data)