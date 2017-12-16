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
```
var datas = [
	{‘label’: L1, ‘value’: V1}
	…
	{‘label’: Ln, ‘value’: Vn}
	];
```
* Compare.py 
Allows to compare couples of files. It shows their differences and highlights possible alerts due to manipulation.
The script is properly called as follows:
`python compare.py /path/to/query /path/to/reference`
And produces a json output like:
```
var datas = [
	{‘label’: L1, ‘alert’: A1, ‘value1’: V11, ‘value2’: V21}
	…
	{‘label’: Ln, ‘alert’: An, ‘value1’: V2n, ‘value2’: V2n}

	];
```
* Classify.py
Looks over a dataset, and scores the distance between various samples.
The script is properly called as follow:
`python classify.py /path/to/file`
And produces a json output like:
```
var datas = [
	{‘label’: L1,‘score’: S1}
	…
	{‘label’: Ln,‘score’: Sn}

	];
```
