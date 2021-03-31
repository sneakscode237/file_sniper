import getpass
import json

def json_creator(os_type):
    user = getpass.getuser()
    data = {}
    types = ["file_management", "chrome_downs", "application", "image", "video", "text", "audio", "font"]

    if os_type == "windows":
        for folder in types:
            if folder == "file_management":
                data[f"{folder}"] = f"C:\\Users\\{user}\\Documents\\file_management"
            else:
                data[f"{folder}"] = f"C:\\Users\\{user}\\Documents\\file_management\\{folder}"
    elif os_type == "linux":
        for folder in types:
            if folder == "file_management":
                data[f"{folder}"] = f"/home/{user}/Documents/file_management"
            else:
                data[f"{folder}"] = f"/home/{user}/Documents/file_management/{folder}"
    else:
        pass

    with open("directories.json", "w") as outfile:
        json.dump(data, outfile)
