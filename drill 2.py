import glob
import shutil
dest_dir = "C:/Users/Bret Spath/Desktop/b"
for file in glob.glob(r'C:/Users/Bret Spath/Desktop/a/*.txt'):
    print (file)                                                                                                                                        
    shutil.copy(file, dest_dir)

shutil.rmtree('C:/Users/Bret Spath/Desktop/a')
