import logging

from order.models import Order
from book.filters import BookFilter
from django.shortcuts import get_object_or_404
from order.serializers import OrderSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from onlineBookStore.pagination import CustomPagination, PaginationHandlerMixin
from django_filters.rest_framework import DjangoFilterBackend

logger = logging.getLogger(__name__)

class OrderViewSet(viewsets.ViewSet, PaginationHandlerMixin):
    """
    This class contain order crud operation implementation with help of viewset.
    """
    queryset = Order.objects.all()
    serializer = OrderSerializer
    filter_backends = (DjangoFilterBackend,)
    pagination_class = CustomPagination
    filterset_fields = (
        'user', 'book',
        'date', 'status',)

    def filter_queryset(self, queryset):
        filter_backends = (DjangoFilterBackend, )
        for backend in list(filter_backends):
            queryset = backend().filter_queryset(
                self.request, queryset, view=self
            )
        return queryset

    # get all books in sorted order with created date.
    def get_queryset(self):
        return Order.objects.get_queryset().order_by('created')

    def list(self, request):
        filtered_data = self.filter_queryset(self.get_queryset())
        results = self.paginate_queryset(filtered_data)
        serializer = OrderSerializer(results, many=True)
        response = {
            'success': True,
            'data': serializer.data,
            'message': "fetch order list",
        }
        return Response(response, status=status.HTTP_200_OK)

    def create(self, request):
        if request.data is not None:
            logger.info(f'Input Data: {request.data}.')
            serializer = OrderSerializer(data=request.data)
            if serializer.is_valid():
                print(f"Validated Data name: {request.data.get('name')}.")
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        queryset = Order.objects.all()
        if pk is not None:
            book = get_object_or_404(queryset, pk=pk)
            serializer = OrderSerializer(book)
            response = {
            'success': True,
            'data': serializer.data,
            'message': "fetch order list",
            }
            return Response(response, status=status.HTTP_200_OK)

    def update(self, request, pk=None, *args, **kwargs):
        logger.info(f'Input Data: {request.data}.')
        if pk is not None:
          queryset = Order.objects.all()
          order = get_object_or_404(queryset, pk=pk)
          serializer = OrderSerializer(order, data=request.data)
          if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
          return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Order.objects.all()
        if pk is not None:
          order = get_object_or_404(queryset, pk=pk)
          logger.info(f'Order: {order.name}.')
          order.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)
