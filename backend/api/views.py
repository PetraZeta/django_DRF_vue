from django.http.response import Http404
from rest_framework import status, permissions

from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import UserSerializer,UserRegisterSerializer, WorkerSerializer
from .models import Worker

# Create your views here.
class UserRegister(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.create(request.data)
            if user:
                return Response({'user': serializer.data})
        return Response(status=status.HTTP_400_BAD_REQUEST)
    
class UserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response({'user': serializer.data}, status=status.HTTP_200_OK)
    
class WorkerListView(APIView):
   # permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = WorkerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        worker = Worker.objects.all()
        serializer = WorkerSerializer(worker, many=True)
        return Response(serializer.data)

class WorkerView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_worker(self, pk):
        try:
            return Worker.objects.get(pk=pk)
        except Worker.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        hero = self.get_worker(pk)
        serializer = WorkerSerializer(hero)
        return Response(serializer.data)

    def put(self, request, pk):
        worker = self.get_worker(pk)
        serializer = WorkerSerializer(worker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        worker = self.get_hero(pk)
        worker.delete()
        return Response("Deleted", status=status.HTTP_200_OK)

