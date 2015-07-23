"""
Import sample data for recommendation engine
"""

import predictionio
import argparse
import random

RATE_ACTIONS_DELIMITER = "::"
SEED = 3

def import_events(client, file):
  f = open(file, 'r')
  random.seed(SEED)
  count = 0
  print "Importing restaurants..."
  for line in f:
    data = line.rstrip('\r\n').split(RATE_ACTIONS_DELIMITER)
    if count != 0:
      client.create_event(
        event="add_restaurant",
        entity_type="item",
        entity_id=data[1]
        )
    count += 1
  f.close()
  print "%s restaurants are imported." % count

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    description="Import restaurant data for recommendation engine")
  parser.add_argument('--access_key', default='invald_access_key')
  parser.add_argument('--url', default="http://localhost:7070")
  parser.add_argument('--file', default="./data/restaurants.txt")

  args = parser.parse_args()
  print args

  client = predictionio.EventClient(
    access_key=args.access_key,
    url=args.url,
    threads=5,
    qsize=500)
  import_events(client, args.file)
