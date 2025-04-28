![Static Badge](https://img.shields.io/badge/python-v3.13-blue)
![Static Badge](https://img.shields.io/badge/FFmpeg-v7.1.1-green)
![Static Badge](https://img.shields.io/badge/PyTubeFix-v8.12.3-red)

# YT Downloader with PyTubeFix and FFmpeg Implementation

As a prerequisite, please ensure Python3.13 is installed. Follow the steps below to run the program.

## Package Installation

Ensure the following packages are installed.

### PyTubeFix

For Windows and Mac OSX:

```
pip install pytubefix
```

### FFmpeg


For Mac OSX:

```
brew install ffmpeg
```

For Windows, please visit the <a href=https://www.ffmpeg.org/download.html>FFmpeg</a> website to install the Windows FFmpeg package.

### SetupTools

For Windows and Mac OSX:

```
pip install setuptools
```

Alternatively, this works for Mac OSX:

```
brew install python-setuptools
```

### Install the CLI Tool Package

Navigate to the src folder that contains the file setup.py and execute the following command to install the CLI:

```
pip install -e .
```

## Tool Execution

To run the program, execute the command in your CLI; Command Prompt for Windows and Terminal for Mac OSX:

```
dyt url
```

This will prompt you to enter a url. Type or paste your url then press enter to submit your url. The video will be downloaded to the ```/downloads``` folder. This folder will be created if it does not exist.