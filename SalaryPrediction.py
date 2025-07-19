import boto3

def lambda_handler(event, context):

    region = 'us-east-1'
    endpoint_name = 'salary-linear'

    # Crear el cliente SageMaker Runtime
    runtime = boto3.client("sagemaker-runtime", region_name=region)

    # Payload: una sola feature (años de experiencia)
    payload = event['body']['years_of_experience']

    # Enviar la solicitud
    response = runtime.invoke_endpoint(
        EndpointName=endpoint_name,
        ContentType='text/csv',  # importante para modelos entrenados con CSV
        Body=payload
    )

    # Leer la respuesta
    salary = response['Body'].read().decode('utf-8')

    return {
        'statusCode': 200,
        'salary_prediction': salary
    }
