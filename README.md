# AEBS-DB

Analysing AEBS (Ættarbandsskráin), the Multi-Generation Registry of the Genetic Biobank of the Faroe Islands. Using [aebs-db-utils](https://github.com/olavurmortensen/aebs-db-utils) to manage AEBS data and [PedGraph](https://github.com/olavurmortensen/pedgraph) to analyse the data.

## Install

Install all requirements to a Python3 virtual environment using `pip`.

```bash
# Create Python virtual environment called "venv".
python3 -m venv venv
# Activate venv.
source venv/bin/activate
# Install requirements.
pip install -r requirements.txt
```

## Neo4j DB

Deploy the neo4j database container:

```bash
rancher kubectl create -f db_setup/aebs-db-master.yaml
```

Then deploy the service, to expose the HTTP and Bolt ports to an IP:

```bash
rancher kubectl create -f db_setup/aebs-db-service.yaml
```

Now the database should be available through bolt://aebs-db:7687.

Alternatively, setup the Neo4j database as done [here](https://github.com/olavurmortensen/pedgraph/#run-neo4j-with-docker).

## Setup DB

**NOTE:** paths and URIs are hardcoded into these scripts.

Convert the GEDCOM genealogy file to a CSV file.

```bash
./ged2csv.py
```

Build the Neo4j database.

```bash
./build_db.py
```

## Notebooks

Start JupyterLab.

```bash
cd notebooks
jupyter lab
```

If you're running in a container you need to use the following arguments.

```bash
jupyter lab --ip=0.0.0.0 --port=80 --allow-root
```
