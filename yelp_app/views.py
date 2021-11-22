from django.http import Http404
from django.shortcuts import render, redirect
from django.views.generic import View, ListView
from .utils.api import get_yelp_instance
from django.conf import settings
from .models import Cafe
from django.db import DatabaseError
import logging
logger = logging.getLogger(__name__)


class SearchView(View):
    template_name = 'search.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        term = request.POST.get('term') if request.POST.get('term') else None
        if term and term.lower() == 'vegan cafe':

            yelp_response = get_yelp_instance(settings.YELP_API_KEY)

            for business in yelp_response.get('businesses'):
                cafe_result = dict(name=business.get('name'), phone=business.get('phone'), categories=(','.join(item['title'] for item in business.get('categories'))),
                                   tags=(','.join(item['title'] for item in business.get('categories'))),
                                   address=business.get('location').get('address1'), city=business.get('location').get('city'),
                                   zip_code=business.get('location').get('zip_code'),
                                   latitude=business.get('coordinates').get('latitude'),
                                   longitude=business.get('coordinates').get('longitude'), rating=business.get('rating'))
                Cafe.objects.update_or_create(**cafe_result)

            return redirect('cafe_list')

        return render(request, self.template_name)


class CafeList(ListView):
    model = Cafe
    template_name = 'list.html'
    paginate_by = 10

    def get_queryset(self):
        try:
            query = Cafe.objects.all()
        except DatabaseError as e:
            logger.error(e)
            raise Http404
        return query
