import os
import subprocess
import json
import time

with open("dirs.linux.test.json") as f:
    data = json.load(f)

while True:
    if len(os.listdir(data["source"])) != 0:
        subprocess.call(["python", "mimesnipe_test.py"])
        time.sleep(1200)
    else:
        time.sleep(1200)
