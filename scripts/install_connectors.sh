#!/bin/bash
docker exec connect confluent-hub install  debezium/debezium-connector-postgresql:0.9.4 --no-prompt
docker restart connect
sleep 25
bash scripts/pipeline/post.sh elasticsearch_sink_connector.json
bash scripts/pipeline/post.sh debezium_source_connector.json