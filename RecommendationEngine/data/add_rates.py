"""
Import sample data for recommendation engine
"""

import predictionio
import argparse
import random

RATE_ACTIONS_DELIMITER = "::"
SEED = 3

def import_events(client, file):
  users_file = open("./data/users.txt", 'r')
  restaurants_file = open(file, 'r')
  random.seed(SEED)
  count = 0
  print "Generating random rates..."
  users = []
  for line in users_file:
    users.append(line.rstrip('\r\n'))
  for line in restaurants_file:
    restaurant_data = line.rstrip('\r\n').split(RATE_ACTIONS_DELIMITER)
    type = data[8]
    if count != 0 and type == "Gastwirtschaft":
      client.create_event(
        event="rate",
        entity_type="user",
        entity_id=users[random.randint(0, 5)],
        target_entity_type="restaurant",
        target_entity_id=restaurant_data[0],
        properties= { "rating" : random.randint(1, 5) } # random rating
      )
    count += 1
  restaurants_file.close()
  users_file.close()
  print "%s rates are generated." % count

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    description="Import sample data for recommendation engine")
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
