import os

DOI_FORMAT = "{prefix}/osf.io/{guid}"

DATACITE_USERNAME = os.environ.get("DATACITE_USERNAME")
DATACITE_PASSWORD = os.environ.get("DATACITE_PASSWORD")
OSF_BEARER_TOKEN = os.environ.get("OSF_BEARER_TOKEN")

# New tokens can be found at https://archive.org/account/s3.php
IA_ACCESS_KEY = os.environ.get("IA_ACCESS_KEY")
IA_SECRET_KEY = os.environ.get("IA_SECRET_KEY")
DATACITE_PREFIX = "10.17605"

PIGEON_TEMP_DIR = os.environ.get(
    "PIGEON_TEMP_DIR", None
)  # setting to None allows tempfile.py to decide

HOST = "0.0.0.0"

PORT = 2020

SENTRY_DSN = os.environ.get("SENTRY_DSN")

ENV = {
    "production": {
        "OSF_API_URL": "https://api.osf.io/",
        "OSF_FILES_URL": "https://files.us.osf.io/",
        "DATACITE_PREFIX": "10.17605",
        "DATACITE_URL": "https://mds.datacite.org/",
        "DOI_FORMAT": "{prefix}/osf.io/{guid}",
        "OSF_COLLECTION_NAME": "yet-to-be-named",
        "ID_VERSION": "v1",
    },
    "staging": {
        "OSF_API_URL": "https://api.staging.osf.io/",
        "OSF_FILES_URL": "https://files.us.staging.osf.io/",
        "DATACITE_PREFIX": "10.70102",
        "DATACITE_URL": "https://mds.test.datacite.org/",
        "DOI_FORMAT": "{prefix}/fk2osf.io/{guid}",
        "OSF_COLLECTION_NAME": "cos-dev-sandbox",
        "ID_VERSION": "staging_v1",
    },
    "local": {
        "OSF_API_URL": "http://192.168.168.167:8000/",
        "OSF_FILES_URL": "http://192.168.168.167:7777/",
        "DATACITE_PREFIX": "10.70102",
        "DATACITE_URL": "https://mds.test.datacite.org/",
        "DOI_FORMAT": "{prefix}/fk2osf.io/{guid}",
        "OSF_COLLECTION_NAME": "cos-dev-sandbox",
        "ID_VERSION": "staging_v1",
    },
}
