import subprocess
import json


# presets = [1,]
def reset_json():
    with open(r'presets.json', 'w') as f:
        json.dump({}, f)
global preset_dict
#check if presets.json is present, if not, create presets.json
try:
    with open(r'presets.json', 'r') as f:
        pass
except:
    reset_json()
with open(r'presets.json', 'r') as f:
    try:
        preset_dict = dict(json.load(f))
    except:
        reset_json()
        preset_dict = dict(json.load(f))

def run_start_up(i):
    global preset_dict
    with open(r'presets.json', 'r') as f:
        preset_dict = json.load(f)
    paths = preset_dict[str(i)]

    for i in paths:
        subprocess.Popen(i, shell=True, stdout=subprocess.DEVNULL)
        print(f"[LAUNCHING]: {i}")

def run_add(preset_name, files):
    preset_dict.update({preset_name: files})

    with open(r'presets.json', 'w') as f:
        json.dump(preset_dict, f,)

