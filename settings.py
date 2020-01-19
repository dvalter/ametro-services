import os
import datetime

from globalization.builder import build_geonames_database
from pmetro import ini_files
from pmetro import pmz_transports
from pmetro.log import CompositeLog, LogLevel, ConsoleLog, FileLog


def ensure_directories_created(paths):
    for directory_path in paths:
        if not os.path.isdir(directory_path):
            os.mkdir(directory_path)


FORCE_REFRESH = False
FORCE_IMPORT = False

MAPS_SOURCE_URL = 'file://' + os.path.realpath('.') + '/www/autoupdate/'

base_dir = ''

GEONAMES_PATH = os.path.join(base_dir, 'geonames')
GEONAMES_DB = os.path.join(GEONAMES_PATH, 'geonames.db')

PMETRO_PATH = os.path.join(base_dir, 'www/autoupdate')
MANUAL_PATH = os.path.join(base_dir, 'manual/app')
CACHE_PATH = os.path.join(base_dir, 'cache')
IMPORT_PATH = os.path.join(base_dir, 'import')
PUBLISHING_PATH = os.path.join(base_dir, 'www')
TEMP_PATH = os.path.join(base_dir, 'tmp')
LOG_BASE_PATH = os.path.join(base_dir, 'logs')
LOG_PATH = os.path.join(LOG_BASE_PATH, datetime.datetime.now().strftime("%Y%m%d.%H%M%S.%f"))

ensure_directories_created([GEONAMES_PATH, CACHE_PATH, IMPORT_PATH, TEMP_PATH, LOG_BASE_PATH, LOG_PATH, PUBLISHING_PATH])

APP_LOG = CompositeLog([
    ConsoleLog(level=LogLevel.Info),
    FileLog(file_path=os.path.join(LOG_PATH, 'import.verbose.log'), level=LogLevel.Debug),
    FileLog(file_path=os.path.join(LOG_PATH, 'import.info.log'), level=LogLevel.Info),
    FileLog(file_path=os.path.join(LOG_PATH, 'import.warnings.log'), level=LogLevel.Warning),
    FileLog(file_path=os.path.join(LOG_PATH, 'import.errors.log'), level=LogLevel.Error)
])

ini_files.LOG = APP_LOG
pmz_transports.LOG = APP_LOG

build_geonames_database(GEONAMES_PATH, GEONAMES_DB)
