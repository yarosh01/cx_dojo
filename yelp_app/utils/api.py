from yelpapi import YelpAPI


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
