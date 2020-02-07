import boto3

cf = boto3.client('cloudformation')

#Helper Functions
def _write_to_file(file_name, content):
    try:
        secret_file = open(file_name, 'w')
        secret_file.write(content)
        secret_file.close()
    except Exception as e:
        raise e
    return

def _parse_template(template):
    with open(template) as template_fileobj:
        template_data = template_fileobj.read()
    cf.validate_template(TemplateBody=template_data)
    return template_data

def _print_log(message):
    print("Device Registration Service: {}".format(message))
