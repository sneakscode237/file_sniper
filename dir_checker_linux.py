import json
import os

missing_dirs = []

with open("dirs.linux.test.json") as f:
    data = json.load(f)
    for values in data.values():
        if os.path.isdir(values):
            pass
        else:
            missing_dirs.append(values)
    for missing in missing_dirs:
        print("%s is missing in your system!" % missing)
    if not missing_dirs:
        print("Every required directory exists in your system!")


if missing_dirs:
    user = str(input("There are missing directories! Do you want to create all of the missing directories?"
                     "(y/n) "))
    directory = ""

    if user == "y":
        try:
            for directory in missing_dirs:
                os.mkdir(directory)
        except OSError:
            print("Creation of the directory %s failed" % directory)
        else:
            print("Successfully created all missing directories!")
    elif user == "n":
        print("No directories have been created!")
    else:
        print("Sorry something went wrong!")



