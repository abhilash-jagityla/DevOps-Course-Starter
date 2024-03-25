import requests
import dotenv
import os

dotenv.load_dotenv()

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

response = requests.get(reqUrl, params = query_params , verify='wincacerts.pem')

response_list = response.json()

for trello_list in response_list:
    for trello_card in trello_list['cards'] :
       print(trello_card['name'])
       

print(response.status_code)