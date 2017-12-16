# Audio File Format Analysis

## Aims
- Given a couple of audio files, query and reference, estimate if both are produced by the same device.

## Audio File Containers
* Audio Coding Format: The bit layout that defines audio data
  * Lossy (mp3, aac, …)
  * Lossless (wav, aiff, flac, …)
* Metadata: 
  * General information 
  * Specific information

## Requirements
* ExifTool CLI
* MediaInfo CLI
* pyExifTool
* pyMediaInfo
* pymysql

## How to use
* Macro.py 
Allows user to extract metadata from a sample and show them.
The script is properly called as follows:
`python macro.py /path/to/file`
And produces a json output like:
```json
var datas = [
		{‘label’: L1, ‘value’: V1}
		…
		{‘label’: Ln, ‘value’: Vn}
	];
```
