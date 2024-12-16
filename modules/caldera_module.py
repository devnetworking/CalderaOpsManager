import requests
import yaml

class CalderaAPI:
    def __init__(self, config_path):
        """Initializes the CalderaAPI with configuration from a YAML file."""
        with open(config_path, 'r') as file:
            config = yaml.safe_load(file)
        
        self.api_url = config['API_URL']
        self.headers = {
            'Content-Type': 'application/json',
            'Cookie': f"API_SESSION={config['API_SESSION']}"
        }

    def get_abilities(self):
        """Fetches the list of abilities from the Caldera API."""
        try:
            response = requests.get(f"{self.api_url}abilities", headers=self.headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()  # Return parsed JSON data
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch abilities: {e}")
    
    def get_operations(self):
        """Fetches the list of operations from the Caldera API."""
        try:
            response = requests.get(f"{self.api_url}operations", headers=self.headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()  # Return parsed JSON data
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch operations: {e}")
    
    def get_adversaries(self):
        """Fetches the list of adversaries from the Caldera API."""
        try:
            response = requests.get(f"{self.api_url}adversaries", headers=self.headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()  # Return parsed JSON data
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch adversaries: {e}")
    
    def create_operation(self, name, adversary_id):
        """Creates a new operation in the Caldera API."""
        payload = {
            "name": name,
            "adversary_id": adversary_id
        }
        try:
            response = requests.post(f"{self.api_url}operations", headers=self.headers, json=payload)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()  # Return parsed JSON data
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to create operation: {e}")
    
    def delete_operation(self, operation_id):
        """Deletes an operation from the Caldera API."""
        try:
            response = requests.delete(f"{self.api_url}operations/{operation_id}", headers=self.headers)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()  # Return parsed JSON data
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to delete operation: {e}")
    
    def update_operation(self, operation_id, update_data):
        """Updates an existing operation in the Caldera API."""
        try:
            response = requests.patch(f"{self.api_url}operations/{operation_id}", headers=self.headers, json=update_data)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.json()  # Return parsed JSON data
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to update operation: {e}")

