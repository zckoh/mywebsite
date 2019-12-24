from django.conf import settings
from django.shortcuts import render
from whattoeat.models import Restaurant
from projects.models import Project
import logging
import googlemaps
import time
logger = logging.getLogger(__name__)

def get_restaurants(loc):
    gmaps = googlemaps.Client(key=settings.GOOGLEMAPS_API_KEY)
    next_page_token = ""
    restaurants_available = []

    for j in range(0,3):
        nearby_search = gmaps.places_nearby(location=loc,
                                        rank_by="distance",
                                        language="en",
                                        keyword="restaurant",
                                        open_now=True,
                                        page_token=next_page_token)

        results = nearby_search["results"]

        for result in results:
            restaurants_available.append(result.get("name"))

        if nearby_search.get("next_page_token"):
            next_page_token = nearby_search.get("next_page_token")
            time.sleep(1)
        else:
            break

    return restaurants_available

# Create your views here.
def whattoeat_index(request):
    projects = Project.objects.all()

    # retrieve search result from google maps python API
    location = (52.1942232,0.1373915)
    restaurants_avail = get_restaurants(location)

    logger.info(restaurants_avail)
    context = {
        'restaurants' : restaurants_avail,
        'projects' : projects,
    }
    return render(request, 'whattoeat/whattoeat_index.html', context)

def whattoeat_eatout(request):
    # todo
    return render(request, 'whattoeat/whattoeat_index.html', context)

def whattoeat_cook(request):    
    # todo
    return render(request, 'whattoeat/whattoeat_index.html', context)