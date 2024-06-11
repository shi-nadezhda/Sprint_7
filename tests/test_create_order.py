import allure
import requests
import pytest
import json
from endpoints import Api
from data import Order


class TestOrder:
    @allure.title('Проверка создания заказа с выбором {color} цвета самоката')
    @allure.description('Создаем заказ, выбираем цвет самоката. Получаем track заказа и код 201')     
    @pytest.mark.parametrize('color', Order.get_scooter_color())
    def test_order_colors_scooter_selected_success(self, color):
        headers = {"Content-type": "application/json"}
        payload = json.dumps(Order.generate_order_data(color))
        
        r = requests.post(Api.create_order, data=payload, headers=headers)
        
        assert r.status_code == 201
        assert 'track' in r.json()


    @allure.title('Проверка получения списка заказов')
    @allure.description('Проверяем получение списка заказов. Получаем список заказов orders и код 200') 
    def test_get_list_orders_success(self):

        response = requests.get(Api.create_order)
        
        assert response.status_code == 200
        assert 'orders' in response.json()
