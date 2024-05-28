from django.core.management.base import BaseCommand
from core.settings import DATABASES, deploy
from sqlalchemy import create_engine
from resources.models import City
import pandas as pd


class Command(BaseCommand):
    help = "Add data from excel into the database"

    def handle(self, *args, **options):
        data = pd.read_csv("ir.csv")
        
        if deploy:        
            database_url = "postgresql://{user}:{password}@{host}:{port}/{name}".format(
                user=DATABASES['default']['USER'],
                password=DATABASES['default']['PASSWORD'],
                host=DATABASES['default']['HOST'],
                port=DATABASES['default']['PORT'],
                name=DATABASES['default']['NAME'],
            )
            engine = create_engine(database_url, echo=False)
        else:
            engine = create_engine("sqlite:///db.sqlite3")
        
        data.to_sql(City._meta.db_table, con=engine, index=True, index_label="id", if_exists="replace")
