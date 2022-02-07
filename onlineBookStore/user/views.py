import logging

from book.models import Book
from book.filters import BookFilter
from django.shortcuts import get_object_or_404
from book.serializers import BookSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from onlineBookStore.pagination import CustomPagination, PaginationHandlerMixin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from django.db.models import Count

logger = logging.getLogger(__name__)


class BookViewSet(viewsets.ViewSet, PaginationHandlerMixin):
    """
    This class contain book crud operation implementation with help of viewset.
    """
    queryset = Book.objects.all()
    serializer = BookSerializer
    filter_backends = (OrderingFilter, DjangoFilterBackend)
    pagination_class = CustomPagination
    filter_class = BookFilter

    def filter_queryset(self, queryset):
        filter_backends = (DjangoFilterBackend,)
        for backend in list(filter_backends):
            queryset = backend().filter_queryset(
                self.request, queryset, view=self
            )
        return queryset

    # get all books in sorted order with timestamp.
    def get_queryset(self):
        return Book.objects.get_queryset().order_by('timestamp')

    def list(self, request):
        filtered_data = self.filter_queryset(self.get_queryset())
        results = self.paginate_queryset(filtered_data)
        serializer = BookSerializer(results, many=True)
        q = Book.objects.annotate(Count('author'))
        logger.info('aggregation example : ', q[0].author__count)
        response = {
            'success': True,
            'data': serializer.data,
            'message': "fetch image list",
        }
        return Response(response, status=status.HTTP_200_OK)

    def create(self, request):
        if request.data is not None:
            logger.info(f'Input Data: {request.data}.')
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                print(f"Validated Data name: {request.data.get('name')}.")
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        queryset = Book.objects.all()
        if pk is not None:
            book = get_object_or_404(queryset, pk=pk)
            serializer = BookSerializer(book)
            response = {
                'success': True,
                'data': serializer.data,
                'message': "fetch image list"}
            return Response(response, status=status.HTTP_200_OK)

    def update(self, request, pk=None, *args, **kwargs):
        logger.info(f'Input Data: {request.data}.')
        if pk is not None:
            queryset = Book.objects.all()
            book = get_object_or_404(queryset, pk=pk)
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                logger.info(f'Validated Data name: {book.name}.')
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Book.objects.all()
        if pk is not None:
            book = get_object_or_404(queryset, pk=pk)
            logger.info(f'Book: {book.name}.')
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
