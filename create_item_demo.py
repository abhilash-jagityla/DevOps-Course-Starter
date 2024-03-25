import requests
import dotenv
import os

dotenv.load_dotenv()

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
    "idList" : ("TRELLO_TODO_LIST_ID") ,
    "name" : "Python Created Todo"
}

response = requests.post(reqUrl, params = query_params , verify='wincacerts.pem')

print(response.text)