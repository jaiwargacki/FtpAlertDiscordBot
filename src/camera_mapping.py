UNKNOWN_CAMERA = 'Unknown Camera'

# This is specific to the camera system 
# and maps the channel identifiers in filenames 
# to human-readable camera names.
CAMERA_MAPPINGS = {
    '_00_': 'Porch',
    '_01_': 'Side Yard',
    '_02_': 'Backyard',
    '_03_': UNKNOWN_CAMERA,
    '_04_': 'Driveway',
    '_05_': 'Side Yard',
    '_06_': 'Garage',
    '_07_': 'Backyard',
}

def get_camera_name(file_name: str) -> str:
    for key, name in CAMERA_MAPPINGS.items():
        if key in file_name:
            return name
    return UNKNOWN_CAMERA