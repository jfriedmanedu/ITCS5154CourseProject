import os
from configparser import ConfigParser
from glob import glob

def get_config():
    filename="config.ini"
    search_dir="."

    config_path = glob(os.path.join(search_dir, "**", filename), recursive=True)

    if config_path:
        print(f"Found config file at: {config_path}")
        # Load the configuration
        config = ConfigParser()
        config.read(config_path)
        print("Sections:", config.sections())
    else:
        print("No config.ini file found.")

    return config['claimrank']