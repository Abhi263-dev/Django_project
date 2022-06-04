from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RecordSerializer
from .models import Record

class RecordViews(APIView):
    def post(self, request):
        serializer = RecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "record created"}, status=status.HTTP_200_OK)
        else:
            return Response({"errors": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

 
class RecordgetViews(APIView): 
    def get(self, request):
       
        items = Record.objects.all()
        serializer = RecordSerializer(items, many=True)
        return Response({"data": serializer.data}, status=status.HTTP_200_OK)
