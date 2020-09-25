#!/usr/bin/env python3

from pedgraph.BuildDB import BuildDB
from neo4j import GraphDatabase
import logging

logging.basicConfig(level=logging.INFO)

neo4j_uri = 'bolt://aebs-db:7687'
#csv_path = '/home/olavur/experiments/2020-08-28_aebs-db/data/trees/aebs.csv'
csv_uri = 'http://minio.default.10.12.139.152.xip.io/users/olavur/experiments/2020-08-28_aebs-db/data/trees/aebs.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=minio%2F20200914%2F%2Fs3%2Faws4_request&X-Amz-Date=20200914T123320Z&X-Amz-Expires=432000&X-Amz-SignedHeaders=host&X-Amz-Signature=e8a792f09a27c79970d587cf842e06219cdddea975e7c7f8f89c9fd6e183fe02'

census_uri = 'http://minio.default.10.12.139.152.xip.io/users/olavur/experiments/2020-08-28_aebs-db/data/census/census_cleaned.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=minio%2F20200915%2F%2Fs3%2Faws4_request&X-Amz-Date=20200915T103658Z&X-Amz-Expires=432000&X-Amz-SignedHeaders=host&X-Amz-Signature=795c83d3d551e4f8b904bf29f554138dcf4249c1130452ea64fc071658673719'

# FarGen genealogy
#csv_uri = 'http://minio.default.10.12.139.152.xip.io/users/olavur/experiments/2020-06-16_wgs_selection/data/trees/fargen.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=minio%2F20200914%2F%2Fs3%2Faws4_request&X-Amz-Date=20200914T152431Z&X-Amz-Expires=432000&X-Amz-SignedHeaders=host&X-Amz-Signature=0cdf3d9075beea05f2514f9108babd201b8c079f1eebc63716b1144639103d69'

driver = GraphDatabase.driver(neo4j_uri)

# FIXME: uncommon when done testing FIXME
#
#with driver.session() as session:
#    result = session.run('MATCH (p) DETACH DELETE p RETURN p')
#    print('Deleted %d nodes' % len(result.values()))
#
#BuildDB(neo4j_uri, csv_uri)

with driver.session() as session:
    result = session.run('LOAD CSV WITH HEADERS FROM $csv AS line               '
                         'MATCH (person:Person {ind: line.rin}) RETURN person.ind', csv=census_uri)

    n_matches = len(result.values())

    result = session.run('LOAD CSV WITH HEADERS FROM $csv AS line           '
                         'RETURN line', csv=census_uri)

    n_rows = len(result.values())

    logging.info('%d out of %d rows in census CSV matched a record.' % (n_matches, n_rows))

    # Create an index for property "census" for faster look-up.

    # Get a list of all database indexes.
    result = session.run('CALL db.indexes')
    indexes = result.values()

    # If the list contains the 'index_census' index, we will not create it.
    index_names = [index[1] for index in indexes]
    if 'index_census' not in index_names:
        logging.info('Creating an index "index_census" on individual IDs.')
        # The 'index_ind' index does not exist, so we will create it.
        # Create an index on "ind" and constain it to be unique.
        result = session.run('CREATE INDEX index_census FOR (n:Person) ON (n.census)')
    else:
        logging.info('Index "index_census" already exists, will not create.')


    result = session.run("USING PERIODIC COMMIT 1000                        "
                        "LOAD CSV WITH HEADERS FROM $csv AS line      "
                        "MATCH (person:Person {ind: line.rin})             "
                        "MERGE (:Person {ind: line.rin, census: line.year})             "
                        "RETURN person                                 ", csv=census_uri)

    result = session.run('MATCH (p:Person) WHERE EXISTS (p.census) RETURN p')
    n_census = len(result.values())

    result = session.run('MATCH (p:Person) WHERE EXISTS (p.census) RETURN p.census')
    years= [v[0] for v in result.values()]
    n_census_unique = len(set(years))
    logging.info('Added %d unique properties to %d individuals.' % (n_census_unique, n_census))


