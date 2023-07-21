import requests

# print(requests.get("http://127.0.0.1:8000/").json())
# print(requests.get("http://127.0.0.1:8000/items/1").json())

print("Adding an item:")
print(
    requests.post(
        "http://127.0.0.1:8000/",
        json={"name": "HardDrive", "price": 15,
              "count": 5, "id": 4, "category": 'tools'},
    ).json()
)
print(requests.get("http://127.0.0.1:8000/").json())
print()

print("Update an item:")
print(requests.put("http://127.0.0.1:8000/items/0?count=72").json())
print(requests.get("http://127.0.0.1:8000/").json())
print()

print("Delete an item:")
print(requests.delete("http://127.0.0.1:8000/items/0").json())
print(requests.get("http://127.0.0.1:8000/").json())
