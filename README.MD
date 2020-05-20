# Snotel data pipeline and full stack web application
This repository contains a data pipeline as well as a front end (Angular) and backend (Django REST) to query and
plot the data.  

This pipeline scrapes streamflow data from the USDA as well as trip reports from the WTA (Washginton Trails Assosication) and uses 
    - Use psycopg2 to insert data into a postgresDB
    - Kafka Connect & the Debezium postgres source connector to publish trip reports into a Kafka topic which are then consumed by an
    ElasticSearch
    - Django REST framework provides an API for searching trip reports, supported by Elastic Search backend.
    - Angular front end allows users to search trip reports based on keywords,  and view stream flow data plotted with D3js


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
