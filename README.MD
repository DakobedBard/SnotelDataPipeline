# Snotel data pipeline
This repository contains a data pipeline as well as a front end (Angular) as well as a backend (Django REST) to query and
plot the data.  

This pipeline scrapes data streamflow from the USDA as well as trip reports from the WTA (Washginton Trails Assosication) and uses 
    - Use psycopg2 to insert data into a postgresDB
    - Using Kafka Connect & the Debezium postgres connector the trip reports are put into a Kafka topic and then streamed into 
    Elastic Search using Confluent's ElasticSearch sink
This project also a full stack web application includes a Django REST project located within the djangosnotel folder, as well as an Angular frontend  
application in the angularsnotel folder.  

### Run the pipeline

##### Run the kafka stack
docker-compose up --build
##### Run the scraper
run pipeline/wta/create_tables.py (from an ipython window I'm stuggling to get to this to work from command line)   
##### Install Debezium connector and submit connectors to Kafka Connect instance by using the script
bash scripts/install_connectors.sh.  This will take about 30 seconds because it needs to restart the connect container 

##### Verify that records have been inserted into ElasticSearch index
bash scripts/elasticsearch/queryES.sh


![](pipeline.png)
