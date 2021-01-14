#!/usr/bin/env python3

from pedgraph.BuildDB import BuildDB, AddNodeProperties, AddNodeLabels
from neo4j import GraphDatabase
import logging

logging.basicConfig(level=logging.INFO)

neo4j_uri = 'bolt://aebs-db:7687'

# URIs to files on the server. URIs are provided by MinIO, and expire 7 days after creation.

# Genealogy.
gen_uri = 'http://minio.default.10.12.139.152.xip.io/users/olavur/experiments/2020-08-28_aebs-db/data/csv/gen.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=minio%2F20210113%2F%2Fs3%2Faws4_request&X-Amz-Date=20210113T093442Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=c8e9bf2d584acc267a33948a76b7376b8a3d1aaf8010e2590ff686af1a12ae5b'

# Birth year.
by_uri = 'http://minio.default.10.12.139.152.xip.io/users/olavur/experiments/2020-08-28_aebs-db/data/csv/by.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=minio%2F20210114%2F%2Fs3%2Faws4_request&X-Amz-Date=20210114T112241Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=a0d0f8465b27418ed199ee7ccaccc0f8c0e5f4c18c31a2891eb64e9eaaaae2a9'

# Encrypted ID.
hashid_uri = 'http://minio.default.10.12.139.152.xip.io/users/olavur/experiments/2020-08-28_aebs-db/data/csv/hash_id.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=minio%2F20210113%2F%2Fs3%2Faws4_request&X-Amz-Date=20210113T101109Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=c9ee7f592c18608c4a1cde5c41ef72936c19893c209c970e7e976992af81df01'

# Census.
census_uri = 'http://minio.default.10.12.139.152.xip.io/users/olavur/experiments/2020-08-28_aebs-db/data/census/census_cleaned.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=minio%2F20210114%2F%2Fs3%2Faws4_request&X-Amz-Date=20210114T111549Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=c8e89134ba7dd6d0693cb85f5a3ae23276faf67c817fbdff7d363d3eece2e3f2'

driver = GraphDatabase.driver(neo4j_uri)

# Delete and detach all nodes (if any exist) before building database.
#with driver.session() as session:
#    result = session.run('MATCH (p) DETACH DELETE p RETURN p')
#    print('Deleted %d nodes' % len(result.values()))

BuildDB(neo4j_uri, gen_uri)

AddNodeProperties(neo4j_uri, by_uri, 'Person', prop_type='Integer')

AddNodeProperties(neo4j_uri, hashid_uri, 'Person', prop_type='String')

AddNodeProperties(neo4j_uri, census_uri, 'Person', prop_type='Integer')
