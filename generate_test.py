import os

image_files = []
os.chdir("test")
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".png"):
        image_files.append("data/test/" + filename)
os.chdir("..")
with open("test.txt", "w", newline='\n') as outfile:
    for image in image_files:
        outfile.write(image)
        outfile.write("\n")
    outfile.close()
os.chdir("..")