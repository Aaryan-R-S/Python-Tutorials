import os

# ----------- 1 -----------
os.chdir('path-of-folder-to-be-cleaned')
files = os.listdir()
for f in files:
    if os.path.isdir(f):
        print(f)
        files.remove(f)
files.remove('Others')

# ----------- 2 -----------
imgexts = ['.png', '.jpg', '.jpeg']
images = [f for f in files if os.path.splitext(f)[1].lower() in imgexts]
print(images)

docsext = ['.txt', '.docx', '.pdf']
docs = [f for f in files if os.path.splitext(f)[1].lower() in docsext]
print(docs)

medexts = ['.mp3', '.mp4', '.wav']
media = [f for f in files if os.path.splitext(f)[1].lower() in medexts]
print(media)

others = []
for f in files :
    e = os.path.splitext(f)[1].lower()
    if (e not in imgexts) and (e not in docsext) and (e not in medexts):
        others.append(f)
print(others)

# ----------- 3 -----------
if not os.path.exists('Images'):
    os.mkdirs('Images')
if not os.path.exists('Docs'):
    os.mkdirs('Docs')
if not os.path.exists('Media'):
    os.mkdirs('Media')
if not os.path.exists('Others'):
    os.mkdirs('Others')


# ----------- 4 -----------
def moveFile(folder, files):
    for file in files:
        os.replace(file, f"{folder}/{file}") 


moveFile("Images", images)
moveFile("Docs", docs)
moveFile("Media", media)
moveFile("Others", others)
