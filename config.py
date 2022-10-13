import os
BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"

# db cmd
# 1. flask db init (first done only once.)
#    --> create migrations dir. (used by Flask-Migrate)
# 2. flask db migrate
#    --> used when creating or changing a model.
#       (work file is created when executed: migrations/versions/revision_id.py)
# 3. flask db upgrade
#    --> used to apply the model changes to the actual database
#       (change the database by executing the job file created above).
