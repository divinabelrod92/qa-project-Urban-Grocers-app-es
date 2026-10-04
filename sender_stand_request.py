import configuration
import requests
import data

def post_create_user(body):
   return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                 json= body,
                 headers=data.headers)

response = post_create_user(data.user_body)

print(response.status_code)
print(response.json())

token =  response.json()["authToken"]

def post_new_client_kit (kits_body,auth_token):
    headers = data.headers.copy()
    headers ["Authorization"] = auth_token

    return requests.post(configuration.URL_SERVICE + configuration.KITS_PATH,
                         json=kits_body,
                         headers=headers)

kit_response = post_new_client_kit (data.kits_body,token)

print(kit_response.status_code)
print(kit_response.json())
