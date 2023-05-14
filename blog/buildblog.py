import sys
import os

# Run WebPageGen.exe from the directory of this .py file on the blog directory

# Get the path of the directory of this .py file
path = sys.path[0]

# Get the path of the blog directory
blogPath = path + "\\blog"

# Run WebPageGen.exe on the blog directory
os.system(path + "\\WebPageGen.exe " + blogPath)

# Copy the blog/output directory to ../publish/
os.system("xcopy " + blogPath + "\\output ..\\publish\\ /E /Y")