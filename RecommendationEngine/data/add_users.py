"""
Import sample data for recommendation engine
"""

import predictionio
import argparse
import random

def import_events(client, file):
  f = open(file, 'r')
  count = 0
  print "Importing users..."
  for line in f:
    client.create_event(
      event="add_user",
      entity_type="user",
      entity_id=line.rstrip('\r\n')
    )
    count += 1
  f.close()
  print "%s users are imported." % count

if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    description="Import user data for recommendation engine")
  parser.add_argument('--access_key', default='invald_access_key')
  parser.add_argument('--url', default="http://localhost:7070")
  parser.add_argument('--file', default="./data/users.txt")

  args = parser.parse_args()
  print args

  client = predictionio.EventClient(
    access_key=args.access_key,
    url=args.url,
    threads=5,
    qsize=500)
  import_events(client, args.file)
