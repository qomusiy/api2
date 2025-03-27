from django.shortcuts import render
from rest_framework import generics
from .serializer import MetroBekatSerializer
from .models import MetroBekat
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

def index(r):
    return render(r, template_name='index.html', context={'metro':MetroBekat.objects.all()})


class MetroBekatView(APIView):
    def get(self, r):
        metro = MetroBekat.objects.all()
        serializer = MetroBekatSerializer(metro, many=True)
        response = {
            'data':serializer.data,
            'status': status.HTTP_200_OK,
            'message': 'Metro List'
        }
        return Response(response)

class MetroCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = MetroBekatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            rpns = {
                'data': serializer.data,
                'status': status.HTTP_201_CREATED,
                "message": 'Bekat Created'
            }
            return Response(rpns)
        else:
            rpns = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
                "message": 'Invalid Data'
            }
            return Response(rpns)

class MetroUpdateView(APIView):
    def put(self, request, pk, *args, **kwargs):
        book = MetroBekat.objects.get(pk=pk)
        serializer = MetroBekatSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            rpns = {
                'data': serializer.data,
                'status': status.HTTP_200_OK,
                "message": 'Book Updated'
            }
            
        else:
            rpns = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
                "message": 'Invalid Data'
            }
        return Response(rpns)
    
    def patch(self, request, pk, *args, **kwargs):
        book = MetroBekat.objects.get(pk=pk)
        serializer = MetroBekatSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            rpns = {
                'data': serializer.data,
                'status': status.HTTP_200_OK,
                "message": 'Book Updated'
            }
            
        else:
            rpns = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
                "message": 'Invalid Data'
            }
        return Response(rpns)

class MetroBekatDetailView(APIView):
    def get(self, r, pk):
        try:
            metro = MetroBekat.objects.get(pk=pk)
            serializer = MetroBekatSerializer(metro, many=True)
            rspns = {
                'data':serializer.data,
                'status': status.HTTP_200_OK,
                'message': 'Metro List'
            }
        except Exception as e:
            rspns = {
                'data': str(e),
                'status': status.HTTP_404_NOT_FOUND,
                'message': 'Not Found'
            }
        finally:
            return Response(rspns)

class MetroBekatDeleteView(APIView):
    def delete(self, r, pk):
        metro = MetroBekat.objects.get(pk=pk)
        metro.delete()
        rspns = {
                'data': None,
                'status': status.HTTP_204_NOT_CONTENT,
                'message': 'Ochirildi'
            }
        return Response(rspns)
        

### vazifani 1-qismi
### viewset crud kodi, ishlatilganda url qismidagi kommentga etibor qrating

# class MetroViewSet(viewsets.ModelViewSet):
#     queryset = MetroBekat.objects.all()
#     serializer_class = MetroBekatSerializer
#     lookup_field = 'pk'














# class MetroList(generics.ListAPIView):
#     queryset = MetroBekat.objects.all()
#     serializer_class = MetroBekatSerializer

# class MetroCreate(generics.CreateAPIView):
#     queryset = MetroBekat.objects.all()
#     serializer_class = MetroBekatSerializer

# class MetroDelete(generics.DestroyAPIView):
#     queryset = MetroBekat.objects.all()
#     serializer_class = MetroBekatSerializer
#     lookup_field = 'pk'

# class MetroUpdate(generics.UpdateAPIView):
#     queryset = MetroBekat.objects.all()
#     serializer_class = MetroBekatSerializer
#     lookup_field = 'pk'

# class MetroListCreate(generics.ListCreateAPIView):
#     queryset = MetroBekat.objects.all()
#     serializer_class = MetroBekatSerializer

# class MetroRetrieveDestroy(generics.RetrieveDestroyAPIView):
#     queryset = MetroBekat.objects.all()
#     serializer_class = MetroBekatSerializer
#     lookup_field = 'pk'

    
