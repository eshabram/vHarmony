import requests
import random

class Car():
    def __init__(self, url='', type='', make='', color='', condition=''):
        self.url = url
        self.type = type
        self.make = make
        self.color = color
        self.condition = condition
    
    def set_url(self, url):
        self.url = url

    def get_url(self):
        return self.url
    
    def set_type(self, type):
        self.type = type

    def get_type(self):
        return self.type
    
    def get_make(self):
        return self.make
    
    def get_color(self):
        return self.color
    
    def set_condition(self, condition):
        self.condition = condition

    def get_condition(self):
        return self.condition


def query():
    api_key = '40942229-12632621050d81131aeb8535b'
    fail_image = 'https://i.redd.it/this-guy-from-strange-addiction-who-is-in-love-with-his-car-v0-g1hxcgdio7i81.jpg?width=2340&format=pjpg&auto=webp&s=73551fc5611686f3aa6b71c83d10de77e2057a67'

    car_makes = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Volkswagen', 'BMW', 'Mercedes-Benz', 'Audi', 'Nissan', 'Hyundai']
    color_list = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'white', 'black']
    car_types = ['car', 'truck', 'van', 'SUV']
    conditions = ['new', 'used', 'old']

    make_random = random.choice(car_makes)
    color_random = random.choice(color_list)
    type_random = random.choice(car_types)
    condition_random = random.choice(conditions)

    car_image = Car(type=type_random, make=make_random, color=color_random, condition=condition_random)

    url = f'https://pixabay.com/api/?key={api_key}&q={color_random} {make_random} {type_random} {condition_random}'


    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        if 'hits' in data and data['hits']:
            image = random.choice(data['hits'])
            car_image.set_url(image['largeImageURL'])
            return True, car_image
        else:
            return False, car_image
    else:
        print('API request error!')
        car_image.set_url(fail_image)
        return False, car_image


if __name__ == "__main__":
    result = query()
    print(result)