import shutil, os

print("this script will not be in final lab")
shutil.rmtree("./outputs/")
os.mkdir("./outputs/")
if (var := input("choose_lab (2 or 3)")) == "2":
    import main_lab2
else:
    import main_lab3
