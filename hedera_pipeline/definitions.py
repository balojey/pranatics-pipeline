from dagster import Definitions, load_assets_from_modules

from . import assets
from .resources import database_resource
from .jobs import pipeline
from .schedules import pipeline_schedule

all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets=all_assets,
    jobs=[pipeline],
    schedules=[pipeline_schedule],
    resources={
        "database": database_resource
    }
)
