import requests
import os

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

    response = requests.post(reqUrl, params = query_params , verify='wincacerts.pem')

    print(response.text)