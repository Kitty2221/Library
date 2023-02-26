from django.views.decorators.csrf import csrf_exempt
from api.user_api.serializer import CustomUserSerializer, UserOrdersListSerializer, OrderSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import status, generics
from rest_framework import status
from rest_framework import viewsets
from authentication.models import CustomUser
from order.models import Order


# class UserViewSet(viewsets.ViewSet):
#     def list(self, request):
#         user = CustomUser.objects.all()
#         serializer = CustomUserSerializer(user, many=True)
#         return Response(serializer.data)
#
#     def retreive(self, request, pk=None):
#         id = pk
#         if id is not None:
#             user = CustomUser.objects.get(id=id)
#             serializer = CustomUserSerializer(user)
#             return Response(serializer.data)
#
#     def create(self, request):
#         serializer = CustomUserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'msg': 'Data  created'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self, request, pk):
#         id = pk
#         user = CustomUser.objects.get(pk=id)
#         user.delete()
#         return Response({'msg': 'Data Deleted'})

@csrf_exempt
@api_view(['GET', 'POST'])
def users_list(request):
    if request.method == 'GET':
        data = CustomUser.objects.all()

        serializer = CustomUserSerializer(data, context={'request': request}, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def users_detail(request, pk):
    try:
        user = CustomUser.objects.get(pk=pk)
    except CustomUser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = CustomUserSerializer(user, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'GET':
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)


class UserOrdersListView(generics.ListAPIView):
    serializer_class = UserOrdersListSerializer

    def get(self, request, *args, **kwargs):
        self.queryset = Order.objects.filter(user=kwargs['user_id'])
        return self.list(request, *args, **kwargs)


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class OrderDetailView(generics.RetrieveDestroyAPIView):
    lookup_field = "pk"
    serializer_class = OrderSerializer

    def get_queryset(self):
        if self.kwargs["pk"]:
            return Order.objects.filter(user_id=self.kwargs["user_id"])
        else:
            return Order.objects.all()
