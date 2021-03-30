from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from .serializers import PageListSerializer, PageDetailSerializer
from .pagination import PageListPagination
from .tasks import increase_page_counters
from .models import Page


class PageListView(ListAPIView):
    queryset = Page.objects.all()
    serializer_class = PageListSerializer
    permission_classes = [AllowAny, ]
    pagination_class = PageListPagination


class PageDetailView(RetrieveAPIView):
    queryset = Page.objects.all()
    permission_classes = [AllowAny, ]
    serializer_class = PageDetailSerializer

    def get_object(self):
        page = super(PageDetailView, self).get_object()
        increase_page_counters.delay(page.id)
        return page
