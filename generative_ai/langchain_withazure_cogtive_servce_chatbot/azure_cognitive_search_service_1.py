'''
https://techcommunity.microsoft.com/t5/azure-ai-services-blog/azure-cognitive-search-and-langchain-a-seamless-integration-for/ba-p/3901448

https://www.youtube.com/watch?v=WAedZvSDZAI

pip install azure-identity
pip install azure-search-documents==11.4.0b6
pip install azure-search --pre --upgrade
pip install azure-core --pre --upgrade
## common issues :
whenever faced resource not found from azuresearch , trychangig the version in openapi , changing from 2023-05-15 to 
2022-12-01 resolved the issue . 
'''

import os 

from  langchain.embeddings.openai import OpenAIEmbeddings
import openai
import os
from langchain.vectorstores import AzureSearch
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import AzureBlobStorageContainerLoader
# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('corpus')
# from dotenv import load_dotenv

# load_dotenv()
#Configure the OpenAI settings to use Azure OpenAI or OpenAI:
# here we will configure open ai settings 


OPENAI_API_BASE="https://asmita-openai.openai.azure.com/"
OPENAI_API_KEY=""## azure open ai key frm portal.azure.com
OPENAI_API_VERSION="2022-12-01" ##
AZURE_COGNITIVE_SEARCH_SERVICE_NAME="" ## azure cognitive service  service name 
AZURE_COGNITIVE_SEARCH_API_KEY=""## azure cognitive service  service name   from key and endpoints --> primary admin key 
AZURE_COGNITIVE_SEARCH_INDEX_NAME ="langchain-vector-demo-asmita1"
AZURE_CONN_STRING="" ## portal.azure.com-->storage account-->access keys -->connection string


### initialzie azure open ai 
openai.api_type = "azure"
openai.api_base = OPENAI_API_BASE
openai.api_version = OPENAI_API_VERSION
openai.api_key = OPENAI_API_KEY

engine: str ="text-embedding-ada-002" ## deployment model , better name and deployment name should be constant , 

# Configure vector store settings
# Set up the vector store settings using the Azure Cognitive Search endpoint and admin key. You can retrieve those in the Azure portal:

vector_store_address: str =  AZURE_COGNITIVE_SEARCH_SERVICE_NAME
vector_store_password: str = AZURE_COGNITIVE_SEARCH_API_KEY

 

# Create embeddings and vector store instances
# Create instances of the OpenAIEmbeddings and AzureSearch classes:


embeddings = OpenAIEmbeddings(deployment_id="text-embedding-ada-002", chunk_size=1,
                                                openai_api_base=OPENAI_API_BASE, openai_api_key=OPENAI_API_KEY,
                                                openai_api_version=OPENAI_API_VERSION
                                                )
index_name: str = "langchain-vector-demo-asmita-2"

print(f"printing embedding function query :{embeddings.embed_query}")

## connect to azure cognutive service 
vector_store = AzureSearch(
    azure_search_endpoint=AZURE_COGNITIVE_SEARCH_SERVICE_NAME,
    azure_search_key=AZURE_COGNITIVE_SEARCH_API_KEY,
    index_name=AZURE_COGNITIVE_SEARCH_INDEX_NAME,
    embedding_function=embeddings.embed_query)

container_name ="testcontainer" ## container name in azure blob 
blob_name = "asmitargstroag" ## bloblor storage account 



loader = AzureBlobStorageContainerLoader(
    conn_str=AZURE_CONN_STRING,
    container=container_name,
)

documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=150, chunk_overlap=20)
docs = text_splitter.split_documents(documents)
vector_store.add_documents(documents=docs)

print("Data loaded into vectorstore successfully")
