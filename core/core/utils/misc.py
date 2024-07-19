import yaml


def yaml_coerce(value):
    """
    Coerce a YAML string into a Python object.

    e.g. converts string dict to python dict
    useful as sometimes we need to stringify settings this way like in Dockerfiles

    Args:
        value (str): The YAML string to coerce.

    Returns:
        object: The coerced Python object.
    """
    if isinstance(value, str):
        return yaml.load('dummy: ' + value, Loader=yaml.SafeLoader)['dummy']

    return value