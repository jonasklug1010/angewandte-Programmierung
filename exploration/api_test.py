import requests

URL = "http://127.0.0.1:8000/"

def test_get_root():
    response = requests.get(URL)
    if response.status_code == 200:
        print("GET / - SUCCESS")
    else:
        print("GET / - FAILED")

def test_post_creation():
    payload = {
        "title": "title",
        "content": "content",
        "category": "category",
        "tags": ["test", "note"]
    }
    response = requests.post(URL + "notes", json=payload)
    if response.status_code == 201:
        print("POST /notes - SUCCESS")
    else:
        print("POST /notes - FAILED")



        
if __name__ == "__main__":
    test_get_root()
    