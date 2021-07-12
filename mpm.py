from shutil import copyfile
from pathlib import Path
import json

def copy_to_output(input_file, output_folder):
    """
    Copy the input file to the output folder, keeping the same name of the file
    """
    new_file = Path(output_folder) / Path(input_file).name
    copyfile(input_file, new_file)

def copy_main_patcher(main_patcher, output_folder):
    with open (main_patcher, 'r') as f:
        data = json.load(f)
        data['patcher'].pop('dependency_cache') # remove the dependency cache

        new_file = output_folder / main_patcher.name

        with open(new_file, 'w') as f:
            json.dump(data, f, indent=4)