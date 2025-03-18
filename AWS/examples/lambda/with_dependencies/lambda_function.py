# lambda_function.py
import json
import requests  # Ejemplo de una dependencia

def request_site():
    response = requests.get("https://www.example.com")
    response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
    data = response.text
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Successfully fetched data from example.com',
            'data_length': len(data)
        })
    }

def lambda_handler(event, context):
    try:
        return request_site()
    except requests.exceptions.RequestException as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': f'Error fetching data: {str(e)}'
            })
        }
    
if __name__ == "__main__":
    event = {}
    result = lambda_handler(event, None)
    print(result)