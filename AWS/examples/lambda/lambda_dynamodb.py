import boto3
import json

def lambda_handler(event, context):
    """
    Inserta un elemento en una tabla de DynamoDB.

    Args:
        event (dict): El evento de Lambda, que debe contener un diccionario
                      con los atributos a insertar en la tabla DynamoDB.
        context (object): El objeto de contexto de Lambda.

    Returns:
        dict: Un diccionario con el resultado de la operación.
    """

    # 1. Configura el cliente de DynamoDB
    dynamodb = boto3.resource('dynamodb')
    table_name = 'your-dynamodb-table-name'  # Reemplaza con el nombre de tu tabla
    table = dynamodb.Table(table_name)

    try:
        # 2. Obtiene los atributos del evento
        item = event  # Asume que el evento en sí mismo es el item a insertar

        # 3. Valida que el item sea un diccionario
        if not isinstance(item, dict):
            raise ValueError("El evento debe ser un diccionario.")

        # 4. Realiza la inserción
        response = table.put_item(Item=item)

        # 5. Retorna el resultado
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': f'Elemento insertado correctamente en la tabla {table_name}',
                'response': response
            })
        }

    except ValueError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': f"Error de validación: {str(e)}"
            })
        }
    except Exception as e:
        print(f"Error inesperado: {e}")  # Log para depuración
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': f"Error interno del servidor: {str(e)}"
            })
        }