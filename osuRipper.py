from pathlib import Path # Handling folder paths and file structure
import os # OS, for making folders
import shutil # Shell Utilities, for managing files and zipping up folders

listOfFolders = []
listOfSubFolders = []
listOfFiles = []

print("Drag and drop your osu data folder here: ")
inputtedPath = Path(input().replace("'", ""))
print("Preparing output paths, please wait...")
os.mkdir(Path.home() / "Documents" / "osu_data_backup")
for i in range(1, 15):
    os.mkdir(Path.home() / "Documents" / "osu_data_backup" / f"osu{i}")
os.mkdir(Path.home() / "Documents" / "osu_data_backup" / "osu128")

for x in inputtedPath.iterdir():
    if x.is_dir():
        listOfFolders.append(x)
for x in listOfFolders:
    for y in x.iterdir():
        if '.DS_Store' not in str(y):
            listOfSubFolders.append(y)
print("searching for metadata files....")

for x in listOfSubFolders:
    for y in x.iterdir():
        #print(y.is_dir())
        if y.is_dir() == False:
            with open(str(y), 'r', errors="ignore") as file:
                firstLine = file.readline()
                firstLine = firstLine.replace("\n", "")
                header = firstLine[:3]
                #print(f"STEM {y.suffix}\n")
                #if y.suffix == ".txt":
                #    os.remove(y)
                #    continue
                if header == "osu":
                    for x in range(1, 15):
                        if firstLine == f"osu file format v{x}":
                            print(f"copying {str(y)} , with metadata format {firstLine}, to v{x} folder")
                            shutil.copy(y, Path.home() / "Documents" / "osu_data_backup" / f"osu{x}" / f"{y.name}.txt")
                    if firstLine == "osu file format v128":
                        print(f"copying {str(y)} , with metadata format {firstLine}, to v128 folder")
                        shutil.copy(y, Path.home() / "Documents" / "osu_data_backup" / "osu128" / f"{y.name}.txt")
print("zipping up folder, please wait...")      
shutil.make_archive(base_name="osu_backup_send_this_to_me", format="zip", root_dir=(Path.home() / "Documents" / "osu_data_backup"), base_dir=(Path.home() / "Documents" / "osu_data_backup"))  
shutil.move((Path.cwd() / "osu_backup_send_this_to_me.zip"), (Path.home() / "Desktop"))          
print("done without any errors, check your desktop for a zip file!!")