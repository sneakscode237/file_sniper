import shutil
import os
import json
import magic

def mimetype(y):
    with open(y) as f:
        data = json.load(f)

    source = data["chrome_downs"]

    types = ["application", "image", "video", "text", "audio", "font"]

    for file in os.listdir(source):
        src = f"{source}\\{file}"
        print(f"Source directory: {src}")
        mime = magic.Magic(mime=True)
        ext = mime.from_file(src).split('/')[0]
        if ext in types:
            for element in types:
                if ext == element:
                    shutil.move(src, data[ext])
                    print("File has been successfully moved to" + data[ext])
                else:
                    pass
        else:
            print("Couldn't move file! Check the file extension!")
