import xadmin

from apps.goods.models import MyLookupType, MyLookupValue


class MyLookupTypeAdmin(object):
    list_display = ["id", "lookup_type", "enable_flag", "language", "creation_date"]
    search_fields = ["lookup_type", "enable_flag", "language", "creation_date"]
    list_filter = ["lookup_type", "enable_flag", "language", "creation_date"]
    list_editable = ["lookup_type", "enable_flag", "language", "creation_date"]


class MyLookupValueAdmin(object):
    list_display = ["id", "lookup_type_id", "lookup_code", "language", "display_sequence"]
    search_fields = ["lookup_type_id", "lookup_code", "language", "display_sequence"]
    list_filter = ["lookup_type_id", "lookup_code", "language", "display_sequence"]
    list_editable = ["lookup_type_id", "lookup_code", "language", "display_sequence"]


xadmin.site.register(MyLookupType, MyLookupTypeAdmin)
xadmin.site.register(MyLookupValue, MyLookupValueAdmin)
