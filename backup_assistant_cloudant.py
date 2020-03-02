#
# main() será executado ao clicar em "Run This Action".
# 
# @author     Gilvan Junior
# @contact    https://www.linkedin.com/in/gilvanjunior/
#

import sys
import json
from watson_developer_cloud import AssistantV1
from cloudant.client import Cloudant
from cloudant.error import CloudantException
from cloudant.result import Result, ResultByKey

def main(dict):
    
    serviceUsername = dict['CLOUDANT_ACCOUNT']
    servicePassword = dict['CLOUDANT_PASSWORD']
    serviceURL = dict['CLOUDANT_URL']
    
    # Use the IBM Cloudant library to create an IBM Cloudant client.
    client = Cloudant(serviceUsername, servicePassword, url=serviceURL)
    
    # Connect to the server
    client.connect()
    
    databaseName = dict['CLOUDANT_DBNAME']
    
    # Create an instance of the database.
    myDatabaseDemo = client.create_database(databaseName)
    
    # Check that the database now exists.
    if myDatabaseDemo.exists():
        print("'{0}' successfully created.\n".format(databaseName))
        
    service = AssistantV1(
        iam_apikey=dict['IAM_APIKEY'],
        version=dict['WDC_VERSION'],
        url=dict['WDC_URL']
    )
    
    response=service.get_workspace(
        workspace_id=dict['WDC_WORKSPACEID'],
        export='true'
    ).get_result()
        
    newDocument = myDatabaseDemo.create_document(response)

    return { 'status': 200, 'message': 'Backup realizado com sucesso!' }
