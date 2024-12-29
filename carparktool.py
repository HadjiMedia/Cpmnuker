import requests
import json

# Copyright (C) Anasov <me@anasov.ly> - All Rights Reserved
# Unauthorized copying of this file, via any medium is strictly prohibited
# Proprietary and confidential
# Written by Anasov <me@anasov.ly>, 05, May, 2024.

BASE_URL: str = "https://cpmnuker.anasov.ly"

class CPMNuker:

        self.auth_token = None
        
    def login(self, email, password) -> int:
        payload = { "account_email": email, "account_password": password }
        response = requests.post(f"{BASE_URL}/api/account_login", params=params, data=payload)
        response_decoded = json.loads(response.text)
        if response_decoded.get("ok"):
            self.auth_token = response_decoded.get("auth")
        return response_decoded.get("error")

    def register(self, email, password) -> int:
        payload = { "account_email": email, "account_password": password }
        response = requests.post(f"{BASE_URL}/api/account_register", params=params, data=payload)
        response_decoded = json.loads(response.text)
        if response_decoded.get("ok"):
            self.auth_token = response_decoded.get("auth")
        return response_decoded.get("error")

    def delete(self) -> None:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{BASE_URL}/api/account_delete", params=params, data=payload)
        response_decoded = json.loads(response.text)

    def get_player_data(self) -> any:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{BASE_URL}/api/get_data", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded

    def set_player_rank(self) -> bool:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{BASE_URL}/api/set_rank", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")

    def get_key_data(self) -> any:
        response = requests.get(f"{BASE_URL}/api/get_key_data", params=params)
        response_decoded = json.loads(response.text)
        return response_decoded

    def set_player_money(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        response = requests.post(f"{BASE_URL}/api/set_money", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")

    def set_player_coins(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        response = requests.post(f"{BASE_URL}/api/set_coins", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")

    def set_player_name(self, name) -> bool:
        payload = { "account_auth": self.auth_token, "name": name }
        response = requests.post(f"{BASE_URL}/api/set_name", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")

    def set_player_localid(self, id) -> bool:
        payload = { "account_auth": self.auth_token, "id": id }
        response = requests.post(f"{BASE_URL}/api/set_id", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")

    def set_player_plates(self) -> bool:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{BASE_URL}/api/set_plates", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")

    def delete_player_friends(self) -> bool:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{BASE_URL}/api/delete_friends", params=params, data=payload)
        response_decoded = json.loads(response.text)
        return response_decoded.get("ok")
