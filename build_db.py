#!/usr/bin/env python3

from pedgraph.BuildDB import BuildDB, AddNodeProperties, AddNodeLabels
from neo4j import GraphDatabase
import logging

logging.basicConfig(level=logging.INFO)

neo4j_uri = 'bolt://aebs-db:7687'

# URIs to files on the server. URIs are provided by MinIO, and expire 7 days after creation.

# Genealogy.
gen_uri = 'http://minio.default.10.12.139.152.xip.io/users/olavur/experiments/2020-08-28_aebs-db/data/csv/gen.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=minio%2F20200925%2F%2Fs3%2Faws4_request&X-Amz-Date=20200925T131906Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=03914bed2249c5e4c0983af3d8a1a389375f9c6b53dcbc501eadbd96066186a4'

# Birth year.
by_uri = 'http://minio.default.10.12.139.152.xip.io/users/olavur/experiments/2020-08-28_aebs-db/data/csv/by.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=minio%2F20200925%2F%2Fs3%2Faws4_request&X-Amz-Date=20200925T131931Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=c496263940f7852fb7276694c90e628a9f1712e875390246b7db7268eb14c2b9'

# Encrypted ID.
hashid_uri = 'http://minio.default.10.12.139.152.xip.io/users/olavur/experiments/2020-08-28_aebs-db/data/csv/hash_id.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=minio%2F20200925%2F%2Fs3%2Faws4_request&X-Amz-Date=20200925T131948Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=99260752b4f01f889c40f7cbf51cba3872311e8f6130d125e2d3414514561734'

# Census.
census_uri = 'http://minio.default.10.12.139.152.xip.io/users/olavur/experiments/2020-08-28_aebs-db/data/census/census_cleaned.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=minio%2F20200925%2F%2Fs3%2Faws4_request&X-Amz-Date=20200925T135859Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=cf356ac69811161d3902e15255a4339c278a52dfe94946a2bb07293814faaa55'

driver = GraphDatabase.driver(neo4j_uri)

# Delete and detach all nodes (if any exist) before building database.
#with driver.session() as session:
#    result = session.run('MATCH (p) DETACH DELETE p RETURN p')
#    print('Deleted %d nodes' % len(result.values()))
#
#BuildDB(neo4j_uri, gen_uri)

#AddNodeProperties(neo4j_uri, by_uri, 'Person', prop_type='Integer')

AddNodeProperties(neo4j_uri, hashid_uri, 'Person', prop_type='String')

#AddNodeProperties(neo4j_uri, census_uri, 'Person', prop_type='Integer')
