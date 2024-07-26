import requests
import json

response = requests.get("https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow")
print(response.json())
for data in response.json()['items']:
    if data["answer_count"]==1:
        # print(data['title'])
        # print(data['link'])
        print(data["score"])
        print()

#****JSON to Python***********
py_data=json.dumps(response.json(), indent=4)
print(py_data)
#****python to JSON***********
json_data=json.loads(py_data)
print(py_data)

#*****POST call************
base_url="https://gorest.in"
auth_token="Bearer MFwwDQYJKoZIhvcNAQEBBQADSwAwSAJBAJRmzcpTevQqkWn6dJuX/N/Hxl7YxbOwy8+73ijqYSQEN+WGxrruAKtZtliWC86+ewQ0msW1W8psOFL/b00zWqsCAwEAAQ_SQBojqMrKEkBaS6l9O46Ko8Wzfy1dvyf8N6ko139B5i24ngV+/XOm1kOQ3pGyvw9lGx915GeuNGkkEjhnlsWBg"
def post_request():
    url = base_url + "/public/v2/users"
    headers={"Authorization": auth_token}
    data={
        "name":"lokesh",
        "email":"lokeswar@email.com",
        "gender":"male",
        "status":"active",
    }
    response=requests.post(url, json=data, headers=headers)
    assert response.status_code==201
    assert response.json()["name"]=="lokesh"

    user_id=response.json()["id"]
    return user_id

#****PUT request***********
def put_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    headers={"Authorization": auth_token}
    data={
        "name":"lokesh Reddy",
        "email":"lokeswar@email.com",
        "gender":"male",
        "status":"in-active",
    }
    response=requests.post(url, json=data, headers=headers)
    assert response.status_code==200
    assert response.json()["name"]=="lokesh reddy"


#****DELETE request***********
def delete_request(user_id):
    url = base_url + f"/public/v2/users/{user_id}"
    headers={"Authorization": auth_token}
    response=requests.delete(url, json=data, headers=headers)    
    assert response.status_code==200


