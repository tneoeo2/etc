import os
import glob
from pydub import AudioSegment

input = 'inputPath'
file_list = glob.glob(input + '*.flac')
# print(file_list)

EXPORT_PATH = './export/'

for file in file_list :
    file_name = file.split("\\")[-1]
    file_name = os.path.splitext(file_name)[0]
    print(file_name)
    flac_audio = AudioSegment.from_file(file, "flac")
    flac_audio.export(EXPORT_PATH + file_name + ".mp3", format="mp3")



##? conda install -c main ffmpeg  <
