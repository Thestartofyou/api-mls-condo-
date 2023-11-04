import requests

# Define the API endpoint and parameters
api_url = 'https://example-api.com/land-zoning'
api_key = 'your_api_key'  # Replace with your actual API key
min_condos = 50
max_condos = 60

# Define a function to search for land zoning
def find_zoned_land(api_url, api_key, min_condos, max_condos):
    headers = {
        'Authorization': f'Bearer {api_key}'
    }

    params = {
        'min_condos': min_condos,
        'max_condos': max_condos
    }

    try:
        response = requests.get(api_url, headers=headers, params=params)

        if response.status_code == 200:
            land_data = response.json()
            return land_data
        else:
            print(f"API request failed with status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the API request: {e}")
        return None

# Main function
if __name__ == '__main__':
    zoned_land = find_zoned_land(api_url, api_key, min_condos, max_condos)

    if zoned_land:
        print("Zoned land for 50-60 condos:")
        for land in zoned_land:
            print(f"Land ID: {land['id']}")
            print(f"Location: {land['location']}")
            print(f"Zoning Details: {land['zoning']}")
    else:
        print("No zoned land found for the specified criteria.")

