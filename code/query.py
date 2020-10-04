"""
File: query.py

Code for querying GROBID service (with biblio-glutton consolidation service) with raw citation
"""
import requests

def query(q):
    base = "cit-000000000028"
    GROBID_URL = "http://localhost:8070"
    url = '%s/api/processCitation' % GROBID_URL
    text = requests.post(url, data={"citations":q, "consolidateCitations":1}).text
    return text