# -*- coding: utf-8 -*-
import unittest
import requests
import json
import csv

field_names= ['title', 'price', 'available_quantity', 'sold_quantity', 'permalink']


def get_request_to_dict():
    try:
        query = {'1':'chromecast', 'limit':'50'}
        response = requests.get('https://api.mercadolibre.com/sites/MLA/search?q=chromecast&limit=50#json', params=query, timeout=5)
        json_data = json.loads(response.text)
        response.raise_for_status()
        #for i in json_data["results"]:
        #    print(i["title"],i["price"],i["available_quantity"],i["sold_quantity"],i["permalink"])
        return json_data["results"]
        # Code here will only run if the request is successful
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)


def main():
    MyDict = get_request_to_dict()

    with open('mycsvfile.csv', 'w') as csvfile:
        for i in MyDict:
            #print(i["title"],i["price"],i["available_quantity"],i["sold_quantity"],i["permalink"])
            w = csv.DictWriter(csvfile, i.keys())
            #w.writeheader()
            w.writerow(i)

if __name__ == '__main__':
    """unittest.main()"""
    main()
