from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import mongodb



# Create your views here.
@api_view(['GET'])
def GetInformation(request,district,crop):
    data = mongodb.GetExpertSuggestion(district,crop)
    return Response(data)