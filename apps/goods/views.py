from rest_framework import mixins, viewsets
from rest_framework .pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend

from apps.goods.serializer import MyLookupTypeSerializer, MyLookupValueSerializer
from apps.goods.models import MyLookupType, MyLookupValue
# from apps.goods.filters import GoodsFilter


class GoodsPagination(PageNumberPagination):
    page_size = 2
    # 可以通过前端动态指定page_size
    page_size_query_param = 'page_size'
    page_query_param = 'p'
    max_page_size = 100


class MyLookupListViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    List all goods
    """
    queryset = MyLookupValue.objects.all()
    serializer_class = MyLookupValueSerializer
    pagination_class = GoodsPagination

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
