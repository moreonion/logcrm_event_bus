"""Define celery app for initializing workers."""
from logcrm_event_bus import App

APP = App('logcrm_event_bus').celery
