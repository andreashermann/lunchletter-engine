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
    type = data[8]
    if count != 0 and type == "Gastwirtschaft":
      client.create_event(
        event="add_restaurant",
        entity_type="restaurant",
        entity_id=data[0],
        properties= {
          "name" : data[1],
          "address1" : data[2] + " " + data[3],
          "address2" : data[5] + " " + data[6],
          "opening_hours" : data[7],
          "type" : data[8],
          "status" : data[9],
          "coordinate_x" : data[10],
          "coordinate_y" : data[11]
        }
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
