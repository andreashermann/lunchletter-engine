#!/bin/bash
set -x
docker run -it --rm \
	-p 8000:8000 \
	-p 7070:7070 \
	-p 9000:9000 \
	-v /data/elasticsearch:/PredictionIO-0.9.3/vendors/elasticsearch-1.4.4/data \
	-v /data/hbase:/PredictionIO-0.9.3/vendors/hbase-1.0.0/data
	--name engine-prod \
	lunchletter/engine
