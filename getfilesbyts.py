#!/usr/bin/env python3

import os
import subprocess
import json
import datetime
import argparse

# FFMPEG wrapper
import ffmpy

class FileTimestamp:
    def __init__(self, filename, creationTS):
        self.filename = filename
        self.creationTS = creationTS

def main(argv):        
	files = []
	
	for filename in os.listdir(argv.directory):
		if (filename.endswith(".MP4")):  # Change to the format you want
			ff = ffmpy.FFprobe(inputs={f'{argv.directory}/{filename}': '-print_format json -show_entries stream=index,codec_type:stream_tags=creation_time:format_tags=creation_time'})
			data = ff.run(stdout=subprocess.PIPE)
			fileInfo = json.loads(data[0].decode('UTF-8'))               
			createTimestamp = fileInfo["streams"][0]["tags"]["creation_time"]
			cts = datetime.datetime.strptime(createTimestamp, '%Y-%m-%dT%H:%M:%S.%fZ')
			timestamp = cts.strftime("%m/%d/%Y, %H:%M:%S")
			files.append(FileTimestamp(filename, timestamp))
		else:
			continue
	
	# Now sort the list so we show the files in timestamp order
	files.sort(key=lambda x: x.creationTS, reverse=False)

	for f in files:
		print(f"{f.filename} - {f.creationTS}")
    
    
if __name__ == "__main__":
	# Add all our arguments we're expecting so there's nice info about
	# what's necessary to make this all work
	parser = argparse.ArgumentParser("getfilesbyts")
	parser.add_argument("directory", help="The directory with the files", type=str)
	args = parser.parse_args()
	main(args)    