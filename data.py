import random
import allure
import string


class Register:
        
    @allure.step('Создаем рандомного курьера')    
    def generate_new_random_user():
        def generate_random_string(length):
            letters = string.ascii_lowercase
            random_string = ''.join(random.choice(letters) for i in range(length))
            return random_string

        login_pass = []

        login = generate_random_string(10)
        password = generate_random_string(10)
        first_name = generate_random_string(10)

        return {
            "login": login,
            "password": password,
            "firstName": first_name
        }    
        

class Order:
    @allure.step('Создаем новый заказ')
    def generate_order_data(color = ['BLACK']):
        return {
            "firstName": "Федор",
            "lastName": "Федоров",
            "address": "Дубровка, 38",
            "metroStation": 3,
            "phone": "+7 800 555 35 35",
            "rentTime": 5,
            "deliveryDate": "2024-06-10",
            "comment": "Кто-то заказал самокат на Дубровку",
            "color": color            
        }
    
    @allure.step('Выбираем цвет самоката')    
    def get_scooter_color():
        return [
            ['BLACK'],
            ['GREY'],
            ['BLACK', 'GREY'],
            []
        ]
        