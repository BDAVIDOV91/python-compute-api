from app.auth import generate_token

user = "test_user"
token = generate_token(user)
print(f"Generated JWT token for user '{user}': {token}")