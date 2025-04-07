import json

def load_users():
    with open("users.json", "r", encoding="utf-8") as file:
        return json.load(file)
    
def likes_of_users(users):
    likes_users = {}
    for user in users:
        total = sum(post['likes'] for post in user['posts'])
        likes_users[user['name']] = total
    return likes_users

if __name__ == "__main__":
    users = load_users()
    
    print("Общее количество пользователей:", len(users))
    
    print("\nПользователь с максимальным количеством лайков:")
    likes_users = likes_of_users(users)
    max_likes = max(likes_users.values())
    for user, likes in likes_users.items():
        if likes == max_likes:
            print(f"{user}: {likes}")
    
        