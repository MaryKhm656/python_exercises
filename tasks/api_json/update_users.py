import json
import requests
from users import load_users

users = load_users()
    
names = list(set(user['name'] for user in users))
        
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)
update_users = []

if response.status_code == 200:
    users_data = response.json()
    for name in names:
        for user in users_data:
            if name in user['name']:
                update_users.append({
                    "name": user['name'],
                    "email": user['email'],
                    "phone": user['phone']
                })
                break
                
    with open("report2.json", "w", encoding="utf-8") as a:
        json.dump(update_users, a, indent=4, ensure_ascii=False)
        print("Данные успешно обновлены!")
else:
    print("Error:", response.status_code)
                
