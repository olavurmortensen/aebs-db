#!/usr/bin/env python3

from aebsDButils.utils import clean_ged
from aebsDButils.ged2csv import Ged2Genealogy, GetBirthYear, GetEncryptedID
import logging

logging.basicConfig(level=logging.INFO)

# All data is stored here.
DATA_DIR = '/home/olavur/experiments/2020-08-28_aebs-db/data/'

# GEDCOME 5.5.1 file exported from Legacy Family Tree.
GED_RAW = DATA_DIR + 'ged/aebs_export_2020-06-18.ged'

# Path to output files.
GED_PATH = DATA_DIR + 'ged/cleaned.ged'  # Cleaned GED.
GEN_CSV = DATA_DIR + 'csv/gen.csv'  # CSV with genealogical tree.
BY_CSV = DATA_DIR + 'csv/by.csv'  # CSV with birth years.
HASHID_CSV = DATA_DIR + 'csv/hash_id.csv'  # CSV with encrypted IDs.

# Clean GED file.
clean_ged(GED_RAW, GED_PATH)

# Construct genealogical tree.
Ged2Genealogy(GED_PATH, GEN_CSV)

# Get birth years.
GetBirthYear(GED_PATH, BY_CSV)

# Get encrypted IDs.
GetEncryptedID(GED_PATH, HASHID_CSV)
