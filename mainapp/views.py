from django.shortcuts import render
from rest_framework.response import Response
import pandas as pd  
from rest_framework.generics import GenericAPIView  
from .seive import perform_analysis
from rest_framework import status

# Create your views here.  


class GetUserDoc(GenericAPIView):
    def post(self, request, *args, **kwargs):
        file= request.FILES["file"]
        owner= request.data["owner"]
        init_wt= request.data["init_wt"]
        try:
            float(init_wt)
        except Exception as e:
            return Response ({"detail":f"{str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
        response=perform_analysis(file, owner, init_wt)
        if response == False:
            return Response ({"detail":"File is empty or has invalid data types"}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail":response})
