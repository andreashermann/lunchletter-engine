#!/bin/bash

set -e

echo start PredictionIO
pio-start-all

echo create app lunchletter
pio app new lunchletter
KEY=$(pio app list | grep lunchletter | awk '{print $7}')
echo "APP KEY=$KEY"

cd /RecommendationEngine

echo "Importing sample data..."
python data/import_eventserver.py --access_key $KEY


echo start build
pio build --verbose

echo train
pio train

echo deploy
pio deploy

echo "done."
