from yelpapi import YelpAPI
import googleplaces


def get_yelp_instance(yelp_key):
    yelp_instance = YelpAPI(yelp_key)
    kwargs = {
        'term': 'Vegan Cafe',
        'location': 'San Francisco',
        'limit': 50,
        'offset': 50
    }
    yelp_instance = yelp_instance.search_query(**kwargs)
    return yelp_instance


def get_google_instance(google_key):
    google_instance = googleplaces.GooglePlaces(google_key)
    return google_instance
