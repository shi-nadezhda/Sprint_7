class Api:
    base_api_url = 'https://qa-scooter.praktikum-services.ru/api/v1'
    create_courier = base_api_url + '/courier' # создать курьера
    login_courier = base_api_url + '/courier/login' # логин курьера
    create_order = base_api_url + '/orders' # создать заказ
