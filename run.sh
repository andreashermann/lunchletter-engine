#!/bin/bash
set -e

echo start PredictionIO
pio-start-all

KEY=$(pio app list | grep lunchletter | awk '{print $7}')
echo "APP KEY=$KEY"

cd /RecommendationEngine

echo start build
pio build --verbose

echo train
pio train

echo deploy
pio deploy

echo "done."
