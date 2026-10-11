import sender_stand_request
import data

def get_new_user_token ():
    new_token = sender_stand_request.post_create_user(data.user_body)
    new_token  = new_token.json()["authToken"]
    return new_token

def get_kit_body (name):
    current_kit=data.kits_body.copy()
    current_kit["name"] = name
    return current_kit

def positive_assert(name):
    current_kit= get_kit_body (name)
    auth_token =get_new_user_token()
    response =sender_stand_request.post_new_client_kit(current_kit,auth_token)
    assert response.status_code == 201
    assert response.json().get ("name")==name

def negative_assert(name):
    current_kit= get_kit_body (name)
    auth_token = get_new_user_token()
    response =sender_stand_request.post_new_client_kit(current_kit,auth_token)
    assert response.status_code == 400

def test_create_new_kit_1_letter_in_name_get_successful():
    positive_assert("a")

def test_create_new_kit_511_letter_in_name_get_successful():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_create_new_kit_no_letter_in_name_fails():
    negative_assert("")

def test_create_new_kit_512_letter_in_name_fails():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcDe")

def test_create_new_kit_special_characters_in_name_get_successful():
    positive_assert("&/")

def test_create_new_kit_spaces_in_name_successful():
    positive_assert(" A Aaa")

def test_create_new_kit_numbers_in_name_successful():
    positive_assert("123")

def test_create_new_kit_empty_name_fails ():
    body=data.kits_body.copy()
    body.pop("name")
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(body,auth_token)
    assert response.status_code == 400

def test_create_new_kit_different_parameter_numbers_in_name_fail():
    positive_assert(123)
