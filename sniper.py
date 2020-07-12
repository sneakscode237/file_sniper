import shutil
import os
import json

with open("dirs.json") as f:
    data = json.load(f)

source = data["source"]

f_text = [".txt", ".doc", "docx", ".pdf", ".tex", ".odt", ".rtf", ".wpd"]
f_images = [".ai", ".bmp", ".gif", ".ico", ".jpeg", ".png", ".ps", ".psd", ".svg", ".tif", ".tiff", ".PNG", ".JPEG",
            ".jpg"]
f_font = [".fnt", ".fon", ".otf", ".ttf"]
f_exe = [".apk", ".bat", ".bin", ".cgi", ".pl", ".com", ".exe", ".gadget", ".jar", ".msi", "wsf"]
f_mail = [".email", ".eml", ".emlx", ".msg", "oft", "ost", ".pst", ".vcf"]
f_comp = [".7z", ".arj", ".deb", ".pkg", ".rar", ".rpm", ".tar.gz", ".z", ".zip"]
f_prog = [".c", ".class", ".cpp", ".cs", ".h", ".java", ".pl", ".sh", ".swift", ".vb", ".py", ".js", ".php"]
f_spread = [".ods", ".xls", "xlsm", ".xlsx"]
f_audio = [".aif", ".cda", ".mid", ".midi", ".mp3", ".mpa", ".ogg", ".wav", ".wma", ".wpl"]
f_disc = [".bin", ".dmg", ".iso", ".toast", ".vcd"]
f_data = [".csv", ".dat", ".db", ".dbf", ".mdb", ".sav", ".sql", ".tar", ".xml"]
f_inet = [".asp", ".aspx", ".cer", ".cfm", ".css", ".html", ".htm", ".jsp", ".part", ".rss", ".xhtml"]
f_present = [".key", ".odp", ".pps", ".ppt", ".pptx"]
f_video = [".3g2", ".3gp", ".avi", ".flv", ".h264", ".m4v", ".mkv", ".mov", ".mp4", "mpg", ".mpeg", ".rm", ".swf",
           ".vob", ".wmv"]
f_sys = [".bak", ".cab", ".cfg", ".cpl", ".cur", ".dll", ".dmp", ".drv", ".icns", ".ini", ".lnk", ".sys", ".tmp",]

for file in os.listdir(source):
    src = f"{source}\\{file}"
    print(f"Source directory: {src}")
    file, ext = os.path.splitext(src)
    if ext in f_text:
        shutil.move(src, data["text"])
        src = source
        print(file + " has been succesfully moved to " + data["text"])
    elif ext is f_images:
        shutil.move(src, data["images"])
        src = source
        print(file + " has been succesfully moved to " + data["images"])
    elif ext in f_font:
        shutil.move(src, data["font"])
        src = source
        print(file + " has been succesfully moved to " + data["font"])
    elif ext in f_exe:
        shutil.move(src, data["executables"])
        src = source
        print(file + " has been succesfully moved to " + data["executables"])
    elif ext in f_mail:
        shutil.move(src, data["mail"])
        src = source
        print(file + " has been succesfully moved to " + data["mail"])
    elif ext in f_comp:
        shutil.move(src, data["compressed"])
        src = source
        print(file + " has been succesfully moved to " + data["compressed"])
    elif ext in f_prog:
        shutil.move(src, data["programming"])
        src = source
        print(file + " has been succesfully moved to " + data["programming"])
    elif ext in f_spread:
        shutil.move(src, data["spreadsheet"])
        src = source
        print(file + " has been succesfully moved to " + data["spreadsheet"])
    elif ext in f_video:
        shutil.move(src, data["video"])
        src = source
        print(file + " has been succesfully moved to " + data["video"])
    elif ext in f_audio:
        shutil.move(src, data["audio"])
        src = source
        print(file + " has been succesfully moved to " + data["audio"])
    elif ext in f_disc:
        shutil.move(src, data["discfiles"])
        src = source
        print(file + " has been succesfully moved to " + data["discfiles"])
    elif ext in f_data:
        shutil.move(src, data["database"])
        src = source
        print(file + " has been succesfully moved to " + data["database"])
    elif ext in f_inet:
        shutil.move(src, data["internet"])
        src = source
        print(file + " has been succesfully moved to " + data["internet"])
    elif ext in f_present:
        shutil.move(src, data["presentation"])
        src = source
        print(file + " has been succesfully moved to " + data["presentation"])
    elif ext in f_sys:
        shutil.move(src, data["system"])
        src = source
        print(file + " has been succesfully moved to " + data["system"])
    else:
        print("Couldnt move file! Check the file extension!")









