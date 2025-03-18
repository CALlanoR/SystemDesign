import boto3
import json

ec2 = boto3.client('ec2')

def lambda_handler(event, context):
    try:
        instance_id = event['instance_id']

        # Validar que instance_id es una cadena
        if not isinstance(instance_id, str):
            raise ValueError("El 'instance_id' debe ser una cadena.")

        # Validar que el instance_id tenga el formato correcto (opcional)
        if not instance_id.startswith("i-"):
            print("Advertencia: el ID de instancia no comienza con 'i-'")

        # Detener la instancia
        response = ec2.stop_instances(InstanceIds=[instance_id])

        # Verificar si la operación fue exitosa
        if response['StoppingInstances'][0]['CurrentState']['Name'] == 'stopping':
            return {
                'statusCode': 200,
                'body': json.dumps({
                    'message': f'Se ha solicitado la detención de la instancia: {instance_id}'
                })
            }
        else:
            return {
                'statusCode': 500,
                'body': json.dumps({
                    'message': f'No se pudo solicitar la detención de la instancia: {instance_id}. Estado actual: {response}'
                })
            }
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': "Error: El evento debe contener el campo 'instance_id'."
            })
        }
    except ValueError as e:
        return {
            'statusCode': 400,
            'body': json.dumps({
                'message': f"Error: {str(e)}"
            })
        }
    except Exception as e:
        print(f"Error inesperado: {e}") # Registrar el error para debugging
        return {
            'statusCode': 500,
            'body': json.dumps({
                'message': f"Error interno del servidor: {str(e)}"
            })
        }