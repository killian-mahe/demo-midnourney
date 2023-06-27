import json


def load_config(config_file: str) -> dict:
    """Load the desired configuration.

    Parameters
    ----------
    config_file : str
        The configuration file name, without or without the extension.

    Returns
    -------
    A dictionary containing the configuration.
    """

    if config_file[:-5] != ".json":
        config_file += ".json"

    with open(f"conf/{config_file}", "r") as file:
        return json.load(file)
