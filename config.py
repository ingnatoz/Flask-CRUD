import os

# Build the Sqlite ULR for SqlAlchemy
user = "root"
password = "root"
host = "db-books"
database = "books"

SQLALCHEMY_ECHO = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
# SQLALCHEMY_POOL_SIZE = 20
SQLALCHEMY_POOL_TIMEOUT = 10
SEND_FILE_MAX_AGE_DEFAULT = 0
SQLALCHEMY_ENGINE_OPTIONS = {
    "max_overflow": 120,
    "pool_pre_ping": True,
    "pool_recycle": 60 * 60,
    "pool_size": 90,
}
SQLALCHEMY_DATABASE_URI = f'mysql://{user}:{password}@{host}/{database}'
