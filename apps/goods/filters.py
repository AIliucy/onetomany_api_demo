# import django_filters
# from apps.goods.models import Goods
#
#
# class GoodsFilter(django_filters.FilterSet):
#     # 指定区间过滤
#     min_price = django_filters.NumberFilter(field_name="shop_price",
#                                             lookup_expr='gte')
#     max_price = django_filters.NumberFilter(field_name="shop_price",
#                                             lookup_expr='lte')
#     # 模糊过滤
#     name = django_filters.CharFilter(field_name="name", lookup_expr='icontains')
#
#     class Meta:
#         model = Goods
#         fields = ['min_price', 'max_price', 'name']
