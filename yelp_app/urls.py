from .views import SearchView, CafeList
from django.urls import path


urlpatterns = [
    path('', SearchView.as_view(), name='search'),
    path('cafe_result/', CafeList.as_view(), name='cafe_list')
]
