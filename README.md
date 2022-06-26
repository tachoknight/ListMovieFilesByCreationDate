# ListMovieFilesByCreationDate
This is a small Python script using [FFmpeg]('https://ffmpeg.org') to get the creation date of video files.

## Installation
The script should be set to executable by way of `chmod +x ./getfilebyts.py`. Also, [ffmpy](https://pypi.org/project/ffmpy/) needs to be installed. You can do that using:

`pip3 install --user ffmpy`

## How to use it
`getfilebyts.py <directory with files>`

### Note
There will be a lot of output from `ffmprobe` being forked and returning all its output to `stdout`. The resulting list will show up at the end of the program.
