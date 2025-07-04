import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'fast_zero')))

from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
from fast_zero.models import Base 

config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata
