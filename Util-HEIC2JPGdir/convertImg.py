import os, subprocess

directory = '.'

for filename in os.listdir('.'):
    if filename.upper().endswith('.HEIC'):
        newFile = '.\jpg\\' + filename[0:-5] + '.jpg'
        #print('Converting %s to %s' % (os.path.join(directory,filename), newFile))
        subprocess.run(['magick', filename, newFile])