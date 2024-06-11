import allure
import requests
import json
from endpoints import Api
from data import Register


class TestLoginCourier:
    courier = Register.generate_new_random_user()
    @allure.title('Проверка авторизации курьера')
    @allure.description('Авторизуемся под курьером, заполняя все обязательные поля. Получаем id курьера и код 200') 
    def test_authorization_courier_success(self):
        headers = {"Content-type": "application/json"}
        payload = json.dumps(self.courier)
        
        requests.post(Api.create_courier, data=payload, headers=headers)
        r = requests.post(Api.login_courier, data=payload, headers=headers)
        
        assert r.status_code == 200
        assert 'id' in r.json()
        
        
    @allure.title('Проверка авторизации курьера при неправильном логине или пароле')
    @allure.description('Авторизуемся под курьером, заполняя поле несуществующим логином/паролем. Получаем сообщение об ошибке "Учетная запись не найдена" и код 404')         
    def test_login_with_invalid_field_login_failed(self):           
        payload = json.dumps({
            **self.courier,
            'login': 'kazak'
        })
        headers = {"Content-type": "application/json"}
        
        r = requests.post(Api.login_courier, data=payload, headers=headers)
        
        assert r.status_code == 404
        assert r.json()['message'] == "Учетная запись не найдена"
        

    @allure.title('Проверка авторизации курьера при незаполненном поле')
    @allure.description('Авторизуемся под курьером, не заполняя обязательное поле. Получаем сообщение об ошибке "Недостаточно данных для входа" и код 400')    
    def test_one_of_fields_less_error_response(self):
        payload = json.dumps({
            **self.courier,
            'login': ''
        })
        headers = {"Content-type": "application/json"}
        
        r = requests.post(Api.login_courier, data=payload, headers=headers)
        
        assert r.status_code == 400
        assert r.json()['message'] == "Недостаточно данных для входа"
