from rest_framework import status
from rest_framework.response import Response

def response(data,status):
    Response({"data":data}, status=status)