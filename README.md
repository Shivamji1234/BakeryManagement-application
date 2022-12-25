# Bakery Management
This project is based on the bakery management model. BakeryAdmin can do crud operation like add item, delete item, edit item and can also see the order history. Customer can register and login, see item name and price and place order accordingly.

## Features

* Inventory Management
* Register and Login
* Get a list of available products
* Place an Order and get the bill
* See order history

## Path for Customer 

* Register: `http://127.0.0.1:8000/Customer/register/`

* Login: `http://127.0.0.1:8000/Customer/login/`

* All items view API: `http://127.0.0.1:8000/Customer/view-items/`

* View all orders API: `http://127.0.0.1:8000/Customer/view-orders/`

* Order specific items API: `http://127.0.0.1:8000/Customer/order/`


## For admin directly go to admin panel 
From there item and ingredients can be added.

## To access item view API, View all orders API and Order specific items API, first we have to authorize the registered token in Postman authorization OAuth 2.0.

* Only registered customer can access all of the above mentioned API.

# For Order API
```
{
    "item_id": 1,
    "quantity": 2
}
```

* Register
```
{
    "username": "shivam",
    "password": "123",
    "age": 23,
    "number": 8081411956,
    "address": "xyz"
}
```

* Login
```
{
    "username": "shivam",
    "password": "123"
}
```

