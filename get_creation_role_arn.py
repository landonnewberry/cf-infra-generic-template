import json

with open('stack_info.json', 'r') as f:
    data = json.load(f)

    stack = data['Stacks'][0]

    creation_role_arn = [ 
        o['OutputValue'] for o in stack['Outputs'] 
            if o['ExportName'] == 'CreationRoleArn' 
    ][0]

    print(creation_role_arn)