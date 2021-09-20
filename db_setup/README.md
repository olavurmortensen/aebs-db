

Deploy the neo4j database container:

```bash
rancher kubectl create -f aebs-db-master.yaml
```

Then deploy the service, to expose the HTTP and Bolt ports to an IP:

```bash
rancher kubectl create -f aebs-db-service.yaml
```

Now the database should be available through bolt://aebs-db:7687.
