#process audios to chunks
import os 
import subprocess
files=os.listdir("samplevids")

for file in files:
    tutorial_number=file.split(" [")[0].split(" #")[1]
    file_name=file.split(" ｜ ")[0]
    print(file_name,tutorial_number)
    subprocess.run(["ffmpeg","-i",f"samplevids/{file}",f"audios/{tutorial_number}_{file_name}.mp3"])