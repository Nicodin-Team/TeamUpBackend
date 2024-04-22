from rest_framework.pagination import PageNumberPagination

class MediumPage(PageNumberPagination):
    page_size = 2