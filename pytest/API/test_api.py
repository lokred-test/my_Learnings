import requests

ENDPOINT="https://todo.pixegami.io"

def test_can_call_endpoint():
    response=requests.get(ENDPOINT)
    assert response.status_code==200
def test_can_create_task():
    payload={
  "content": "my test content",
  "user_id": "test_user",
  "task_id": "test_task_id",
  "is_done": False,
    }
    response=requests.put(ENDPOINT + "/create-task", json=payload)
    assert response.status_code==200
    data=response.json
    print(data)

    task_id=data["task"]["task_id"]
    get_task_response=requests.get(ENDPOINT+f"/get-task/{task_id}")
    assert get_task_response.status_code==200
    get_task_data=get_task_response.json
    assert get_task_response["content"]==payload["content"]
    assert get_task_response["user_id"]==payload["user_id"]



