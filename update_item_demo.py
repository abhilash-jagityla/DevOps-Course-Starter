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

reqUrl = f"https://api.trello.com/1/cards/65d883daedb2ff75755dfff6"

query_params = {
    "key" : os.getenv("TRELLO_API_KEY") ,
    "token" : os.getenv("TRELLO_API_TOKEN") ,
    "idList" : os.getenv("TRELLO_DONE_LIST_ID") ,
}

response = requests.put(reqUrl, params = query_params , verify='wincacerts.pem')

print(response.text)