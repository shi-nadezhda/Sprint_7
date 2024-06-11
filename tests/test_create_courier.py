import allure
import requests
import json
from endpoints import Api
from data import Register


class TestCreateCourier:
    courier = json.dumps(Register.generate_new_random_user())
                               
    @allure.title('Успешная проверка создания курьера')
    @allure.description('Создаем курьера, заполняя все обязательные поля. Получаем ответ "true" и код 201')                 
    def test_create_courier_success(self):
        headers = {"Content-type": "application/json"}

        r = requests.post(Api.create_courier, data=self.courier, headers=headers)
         
        assert r.status_code == 201
        assert r.json()['ok'] == True
        
        
    @allure.title('Проверка создания двух одинаковых курьеров')
    @allure.description('Создаем курьера с существующим логином. Получаем сообщение об ошибке "Этот логин уже используется. Попробуйте другой." и код 409')         
    def test_create_courier_double(self):
        headers = {"Content-type": "application/json"}
        
        r = requests.post(Api.create_courier, data=self.courier, headers=headers)
         
        assert r.status_code == 409
        assert r.json()['message'] == "Этот логин уже используется. Попробуйте другой."
           
    
    @allure.title('Проверка получения ошибки при отсутствии одного из полей')
    @allure.description('Создаем курьера, оставляя одно обязательное поле не заполненным. Получаем сообщение об ошибке "Недостаточно данных для создания учетной записи" и код 400')     
    def test_create_courier_less_requaed_field(self):
        payload = { 
            'password': '1111', 
            'firstName': 'doma'
        }  
        headers = {"Content-type": "application/json"}
        payload_string = json.dumps(payload)
         
        r = requests.post(Api.create_courier, data=payload_string, headers=headers)
         
        assert r.status_code == 400
        assert r.json()['message'] == "Недостаточно данных для создания учетной записи"
