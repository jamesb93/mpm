import json
from pathlib import Path
from mpm import copy_to_output, copy_main_patcher

patch = Path("/Users/james/Cloud/Projects/impulse/training.maxpat")
output_folder = Path('/Users/james/Cloud/Projects/impulse/training_example')
output_folder.mkdir(exist_ok=True)

valid_types = ['JSON', 'TEXT']

data = {}
with open (patch, 'r') as f:
    data = json.load(f)

dependencies = data['patcher']['dependency_cache']

for k in dependencies:
    if k['type'] in valid_types:
        dep_path = (Path(k['bootpath']) / Path(k['name'])).expanduser()
        copy_to_output(dep_path, output_folder)


# Copy the main patcher to the output folder
# Along the way wipe the dependency cache
copy_main_patcher(patch, output_folder)