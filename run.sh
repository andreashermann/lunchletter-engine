#!/bin/bash

set -e

pio-start-all
cd /RecommendationEngine
pio build --verbose
pio deploy
