import os
import os.path
from json_creator import json_creator
from dir_checker import dir_checker
from mimetype import mimetype

if os.path.isfile("directories.json"):
    pass
else:
    if os.path.isdir("C:\\Users"):
        json_creator("windows")
    elif os.path.isdir("/home"):
        json_creator("linux")

dir_checker("directories.json")

try:
    mimetype("directories.json")
except Exception as e:
    print("Sorry something went wrong!")
