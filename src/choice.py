import yaml
from pathlib import Path

path = Path(__file__).parent / 'projects.yaml'

with path.open() as in_file:
    projects = yaml.load(in_file, Loader = yaml.loader.SafeLoader)


