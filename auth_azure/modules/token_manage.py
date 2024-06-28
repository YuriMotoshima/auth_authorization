class TokenStorage:
    def __init__(self):
        self.token_store = {}

    def save_token(self, user_id: str, token: str):
        self.token_store[user_id] = token

    def get_token(self, user_id: str):
        return self.token_store.get(user_id)

    def delete_token(self, user_id: str):
        if user_id in self.token_store:
            del self.token_store[user_id]

    def get_user_id_by_token(self, token: str):
        for user_id, stored_token in self.token_store.items():
            if stored_token == token:
                return user_id
        return None
