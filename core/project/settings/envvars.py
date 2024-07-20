from core.core.utils.collection import deep_update
from core.core.utils.settings import get_settings_from_environment

"""
This take env variable with matching prefix, strips it,
and adds it to global settings.

e.g.
export CORESETTINGS_IN_DOCKER=True

will add IN_DOCKER = True to settings

"""

# globals() is a dictionary that holds all the global variables
# this should not break as it was processed from the initializer
deep_update(globals(), get_settings_from_environment(ENVVAR_SETTINGS_PREFIX))  # type: ignore # noqa: F821
