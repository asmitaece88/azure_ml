'''
reference links :https://python.langchain.com/docs/integrations/vectorstores/azuresearch
https://www.youtube.com/watch?v=hkSnPhhjm1Y&list=PLrLEqwuz-mRIdlmvhddd7nGiNh8exqsBG&index=36

python packages needed for  cognitve search index sdk 
pip install azure-search-documents==11.4.0b8
pip install azure-identity

# dataset used : https://www.kaggle.com/discussions/general/414512

## this python script will  
1)execute indexing , 
aftre running  this , we  wil find the index  created will have that many number of records as present in csv file
'''
from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
import pandas as pd 
import re 
import json 
import openai
import os 

## define our azure cognitive search  settings 
service_name = 'ai-search-service925'## cognitive seach service name from portal.azure.com
index_name = 'asmitadataindex'
admin_key =''##portal.azure.com-->azure cognitive search servuce -> key 
endpoint =f"https://{service_name}.search.windows.net/"
credential =AzureKeyCredential(admin_key )

#load the csv data into a python dataframe 
file_path = 'linkedln_build_ai_apps_semantic_kernel_langchain/azure_use_cases_pocs/data/customer_support_tickets_1.csv'
df=pd.read_csv(file_path)# encoding='utf-8'
print(df)

##initialize the client 
search_client =SearchClient(endpoint=endpoint,index_name=index_name,credential=credential)

## upload the data to the cognitive service

data =[]

for _,row in df.iterrows():
        data.append({
                "@search.action":"upload",
                "TicketID":str(row["Ticket ID"]),
                "TicketType":row["Ticket Type"],
                "TicketSubject":row["Ticket Subject"],
                "TicketDescription":row["Ticket Description"],
                "TicketStatus":row["Ticket Status"],
                "TicketPriority":row["Ticket Priority"],
                "TicketChannel":row["Ticket Channel"]
        })

result =search_client.upload_documents  (data )     
print(f"Upload status result :{result} ")










