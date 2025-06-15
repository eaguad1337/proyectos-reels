from faker import Faker
import requests
import time

fake = Faker()

count = 0
while True:
    try:
        r = requests.post(
            "https://62b2905120cad3685c8fb43a.mockapi.io/users",
            json={
                "name": fake.name(),
                "email": fake.email(),
                "username": fake.user_name(),
            },
        )
        time.sleep(1)
        count += 1
        print(f"Registros creados: {count}", end="\r")
    except Exception as e:
        print(e)
        break