import os
folders=os.listdir("Clutter")
print(folders)
k=0
for file in folders:
    if file.endswith(".png"):
        os.rename(f"Clutter/{file}",f"Clutter/{k}.png")
        k=k+1
folders=os.listdir("Clutter")
print(folders)