import argparse
import boto3
import setup_helper

TEMPLATE_LOCATION = "../cfn/device-registration.yaml"

iot = boto3.client('iot')
cf = boto3.client('cloudformation')

parser = argparse.ArgumentParser()
parser.add_argument("device_name")
args = parser.parse_args()
device = args.device_name

secrets = iot.create_keys_and_certificate(setAsActive=True)
cert_arn = secrets['certificateArn']
setup_helper._write_to_file("{}.cert.pem".format(device), secrets['certificatePem'])
setup_helper._write_to_file("{}.public.key".format(device), secrets['keyPair']['PublicKey'])
setup_helper._write_to_file("{}.private.key".format(device), secrets['keyPair']['PrivateKey'])
setup_helper._print_log("Key Pair and Certificates have been generated by AWS IoT and added to current working Directory")

stack_creation = cf.create_stack(
    StackName="pfe-chiller-poc-{}".format(device),
    TemplateBody=setup_helper._parse_template(TEMPLATE_LOCATION),
    Parameters=[
        {
            'ParameterKey': 'DeviceName',
            'ParameterValue': device
        },
        {
            'ParameterKey': 'CertificateArn',
            'ParameterValue': cert_arn
        }
    ],
    Capabilities=['CAPABILITY_NAMED_IAM', 'CAPABILITY_IAM'],
    OnFailure='DO_NOTHING'
)
setup_helper._print_log("CloudFormation stack has been created.")

waiter = cf.get_waiter('stack_create_complete')
waiter.wait(StackName="pfe-chiller-poc-{}".format(device))
setup_helper._print_log("Awaiting CloudFormation Stack")

endpoint_info = iot.describe_endpoint(endpointType='iot:Data-ATS')
print("IoT Endpoint: {}".format(endpoint_info['endpointAddress']))
