## script to upload  files to azure blob/storage container 

## post executing script blob_files.py, 
<img width="933" alt="image" src="https://github.com/asmitaece88/azure_ml/assets/45303929/bb41d1ce-88f9-4687-9ab7-8bf89f75a4e2">
 
 ## next  create azure cognitive search service 
 create a  free  azure cognitive service index 
 <img width="778" alt="image" src="https://github.com/asmitaece88/azure_ml/assets/45303929/b0abf2c1-e026-48dc-b2e9-f1e61ce1a1e0">

 # we will now  use python sdk  , to index the data stored in blob storage , through the use of script - azure_cognitive_search_index_data.py
 ## note , here index will be created programatically 

 <img width="839" alt="image" src="https://github.com/asmitaece88/azure_ml/assets/45303929/0901a9b8-5a79-412b-bff6-0773ccfa828a">

 ## now checking the index  in azure cognitive service --> indexer --> click on the index , just check whether all the embeddings has been loaded in the vector store 

 <img width="863" alt="image" src="https://github.com/asmitaece88/azure_ml/assets/45303929/87f131d5-79e6-4200-bea1-608c5f15dec8">

 # clicking on refresh  , gives us the actal document count 
 <img width="773" alt="image" src="https://github.com/asmitaece88/azure_ml/assets/45303929/0e58d921-31e0-4f05-a5ec-471f7dce829c">
 
 # we can now use the vector store , to retreive the information from our chatbot , which we will call through application.py
 

 
 


