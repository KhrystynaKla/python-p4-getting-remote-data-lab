import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        try:
            response = requests.get(self.url)
            return response.content
        except requests.exceptions.RequestException as e:
            print(f"Error during GET request: {e}")
            return None

    def load_json(self):
        try:
            return json.loads(self.get_response_body())
        except requests.exceptions.RequestException as e:
            print(f"Error during GET request: {e}")
            return None


        












    # def get_response_body(self):
    #     try:
    #         response = requests.get(self.url)
    #         response.raise_for_status()  # Raise an exception for bad responses
    #         return response.text
    #     except requests.exceptions.RequestException as e:
    #         print(f"Error during GET request: {e}")
    #         return None

    # def load_json(self):
    #     response_body = self.get_response_body()
        
    #     if response_body:
    #         try:
    #             json_data = response_body.json()
    #             return json_data
    #         except ValueError as e:
    #             print(f"Error loading JSON: {e}")
    #             return None
    #     else:
    #         return None