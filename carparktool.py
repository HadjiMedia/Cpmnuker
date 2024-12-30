import requests

__ENDPOINT_URL__: str = "https://cpmnuker.anasov.ly/api"

class CPMNuker:

    def login(self, email, password) -> int:
        payload = { "account_email": email, "account_password": password }
        response = requests.post(f"{__ENDPOINT_URL__}/account_login", params=params, data=payload)
        response_decoded = response.json()
        if response_decoded.get("ok"):
            self.auth_token = response_decoded.get("auth")
        return response_decoded.get("error")

    def register(self, email, password) -> int:
        payload = { "account_email": email, "account_password": password }
        response = requests.post(f"{__ENDPOINT_URL__}/account_register", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("error")

    def delete(self):
        payload = { "account_auth": self.auth_token }
        requests.post(f"{__ENDPOINT_URL__}/account_delete", params=params, data=payload)

    def get_player_data(self) -> any:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{__ENDPOINT_URL__}/get_data", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded

    def set_player_rank(self) -> bool:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{__ENDPOINT_URL__}/set_rank", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def get_key_data(self) -> any:
        response = requests.get(f"{__ENDPOINT_URL__}/get_key_data", params=params)
        response_decoded = response.json()
        return response_decoded

    def set_player_money(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        response = requests.post(f"{__ENDPOINT_URL__}/set_money", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def set_player_coins(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        response = requests.post(f"{__ENDPOINT_URL__}/set_coins", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def set_player_name(self, name) -> bool:
        payload = { "account_auth": self.auth_token, "name": name }
        response = requests.post(f"{__ENDPOINT_URL__}/set_name", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def set_player_localid(self, id) -> bool:
        payload = { "account_auth": self.auth_token, "id": id }
        response = requests.post(f"{__ENDPOINT_URL__}/set_id", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def set_player_plates(self) -> bool:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{__ENDPOINT_URL__}/set_plates", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def get_player_car(self, car_id) -> any:
        payload = { "account_auth": self.auth_token, "car_id": car_id }
        response = requests.post(f"{__ENDPOINT_URL__}/get_car", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def delete_player_friends(self) -> bool:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{__ENDPOINT_URL__}/delete_friends", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_w16(self) -> bool:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_w16", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_horns(self) -> bool:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_horns", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def disable_engine_damage(self) -> bool:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{__ENDPOINT_URL__}/disable_damage", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlimited_fuel(self) -> bool:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{__ENDPOINT_URL__}/unlimited_fuel", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def set_player_wins(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        response = requests.post(f"{__ENDPOINT_URL__}/set_race_wins", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def set_player_loses(self, amount) -> bool:
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        response = requests.post(f"{__ENDPOINT_URL__}/set_race_loses", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_houses(self) -> bool:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_houses", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_smoke(self) -> bool:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_smoke", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_paid_cars(self) -> bool:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_paid_cars", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_all_cars(self) -> bool:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_all_cars", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def unlock_all_cars_siren(self) -> bool:
        payload = { "account_auth": self.auth_token }
        response = requests.post(f"{__ENDPOINT_URL__}/unlock_all_cars_siren", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def account_clone(self, account_email, account_password) -> bool:
        payload = { "account_auth": self.auth_token, "account_email": account_email, "account_password": account_password }
        response = requests.post(f"{__ENDPOINT_URL__}/clone", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")