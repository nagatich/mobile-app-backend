import requests
import json

from bs4 import BeautifulSoup

def bytes_to_json(bytes_data):
    json_data = bytes_data.decode('utf8').replace("'", '"')
    return json.loads(json_data)

def only_numbers(string):
    return int(''.join(i for i in string if i.isdigit()))

class Drom:
    URL = 'https://baza.drom.ru/backend/search-autoparts/'
    LIST_CONTROL_URL = f'{URL}list-control/v3.0/'
    REFERENCE_URL = f'{URL}reference/v1.0/'
    TYPESET_CAR_POSTFIX = '?typeSet=car'

    def get_car_list(self):
        cars = requests.get(f'{self.LIST_CONTROL_URL}{self.TYPESET_CAR_POSTFIX}')
        data = bytes_to_json(cars.content)
        return data

    def get_car_models(self, car_name):
        """
            car_name (str): mercedes-benz.
        """
        models = requests.get(f'{self.LIST_CONTROL_URL}{car_name}/{self.TYPESET_CAR_POSTFIX}')
        data = bytes_to_json(models.content)
        return data

    def get_model_generations(self, model_name):
        """
            model_name (str): mercedes-benz c-class.
        """
        payload = {
            'model': model_name,
        }
        generations = requests.get(f'{self.REFERENCE_URL}generations', params=payload)
        data = bytes_to_json(generations.content)
        return data

    def get_generation_modifications(self, model_name, generation):
        """
            model_name (str): mercedes-benz c-class.
            generation (int): 2.
        """
        payload = {
            'model': model_name,
            'generations': generation,
        }
        modifications = requests.get(f'{self.REFERENCE_URL}modifications', params=payload)
        data = bytes_to_json(modifications.content)
        return data

    @staticmethod
    def get_query_html(model, generation, query, engine_fuel = None, engine_volume = None, city = 15291):
        """
            model (str): mercedes-benz c-class.
            generation (int): 2.
            query (str): магнитола.
            engine_fuel (str): gasoline.
            engine_volume (int): 1800.
            city (int): 15291.
        """
        payload = {
            'ajax': 1,
            'async': 1,
            'status': 'actual',
            'pageSize': 10000,
            'autoPartsFuel': engine_fuel,
            'autoPartsGeneration': generation,
            'autoPartsVolume': engine_volume,
            'city': city,
            'model': model,
            'query': query,
        }
        query = requests.get(f'https://baza.drom.ru/sell_spare_parts/', params=payload)
        data = json.loads(query.text)
        return data

    @staticmethod
    def get_min_max_avg_price(data):
        """
            data (result of get_query_html): includes html, itemsCount
        """
        html = data.get('feed')
        soup = BeautifulSoup(html, 'html.parser')
        prices = soup.find_all(class_="price-per-quantity__price")
        price_list = [only_numbers(p.text) for p in prices]
        data = {
            'minimum': 0,
            'maximum': 0,
            'average': 0,
        }
        if len(price_list):
            data['minimum'] = min(price_list)
            data['maximum'] = max(price_list)
            data['average'] = int(sum(price_list) / len(price_list))
        return data
