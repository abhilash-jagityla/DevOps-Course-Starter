import requests
import os

from todo_app.item import Item

def add_item(title):
    import ssl
    context = ssl.create_default_context()
    der_certs = context.get_ca_certs(binary_form=True)
    pem_certs = [ssl.DER_cert_to_PEM_cert(der) for der in der_certs]
    with open('wincacerts.pem', 'w') as outfile:
        for pem in pem_certs:
            outfile.write(pem + '\n')

    reqUrl = "https://api.trello.com/1/cards"

    query_params = {
        "key" : os.getenv("TRELLO_API_KEY") ,
        "token" : os.getenv("TRELLO_API_TOKEN") ,
        "idList" : os.getenv("TRELLO_TODO_LIST_ID") ,
        "name" : title
    }

    response = requests.post(reqUrl, params=query_params, verify='wincacerts.pem')

    print(response.text)

def get_items():
    board_id = os.getenv("TRELLO_BOARD_ID")

    import ssl
    context = ssl.create_default_context()
    der_certs = context.get_ca_certs(binary_form=True)
    pem_certs = [ssl.DER_cert_to_PEM_cert(der) for der in der_certs]
    with open('wincacerts.pem', 'w') as outfile:
        for pem in pem_certs:
            outfile.write(pem + '\n')

    reqUrl = f"https://api.trello.com/1/boards/{board_id}/lists"

    query_params = {
        "key" : os.getenv("TRELLO_API_KEY") ,
        "token" : os.getenv("TRELLO_API_TOKEN") ,
        "cards" : "open"
    }

    response = requests.get(reqUrl, params=query_params, verify='wincacerts.pem')

    response.raise_for_status()

    response_list = response.json()

    items = []

    for trello_list in response_list:
        for trello_card in trello_list['cards']:
            item = Item.from_trello_card(trello_card,trello_list)
            items.append(item)         
                     
    return items

def move_item_to_done(item_id) :
    
    reqUrl = f"https://api.trello.com/1/cards/{item_id}"

    query_params = {
        "key" : os.getenv("TRELLO_API_KEY") ,
        "token" : os.getenv("TRELLO_API_TOKEN") ,
        "idList" : os.getenv("TRELLO_DONE_LIST_ID") ,
    }
    response = requests.put(reqUrl, params = query_params , verify='wincacerts.pem')

    response.raise_for_status()
     
    