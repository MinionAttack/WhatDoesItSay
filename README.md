# What does it say?

![build](https://img.shields.io/badge/build-passing-brightgreen) ![license](https://img.shields.io/badge/license-MIT-brightgreen) ![python](https://img.shields.io/badge/python-3.8%2B-blue) ![platform](https://img.shields.io/badge/platform-linux--64%20%7C%20win--64-lightgrey) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=MinionAttack_WhatDoesItSay&metric=alert_status)](https://sonarcloud.io/dashboard?id=MinionAttack_WhatDoesItSay)

Table of contents.

1. [Introduction](#introduction)
2. [Requisites](#requisites)
3. [Project structure](#project-structure)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [How to use](#how-to-use)
7. [Licensing agreement](#licensing-agreement)

## Introduction

As I am not a native English speaker, I sometimes find it difficult to identify the lyrics of a song I like and not all songs have their
lyrics available on the Internet, either officially or unofficially.

That's why I came up with a small project to see if it was possible to make something that could guess the lyrics of songs. Although in my
head the idea sounded very good, even separating the voice from the rest of the sounds in the songs, the results are quite pitiful...

If you know how they can be improved don't hesitate to let me know!

## Requisites

In order to use the program it is necessary to have a compatible environment:

- **Operative system**: A *Linux* based system where the program will run. On *Windows* the program should work but this has not been
  tested.
- **Python version**: The program has been developed with version *3.8.9*. It may work with older versions, but this has not been tested.
- **A Google Cloud Platform account**: You need to have an active account and in addition to that:
  - **NOTE**: The project has been realised using non-public buckets. The use of public buckets has not been tested so in that case the *
    Google Cloud Platform* configuration may vary.
  - A project in which the *Speech-To-Text* service, *API and Services* and the *IAM and administration* are enabled and configured.
  - A service account enabled on the project.
  - A bucket in *Google Cloud Storage* where the service account has at least the permissions of Storage Administrator and Storage Object
    Manager.
  - The *JSON* with the credentials of the service account.

## Project structure

In this section you can have a quick view of the project structure.

```
.  
├── LICENSE  
├── logs (*)
│ ├── critical.log  
│ ├── debug.log  
│ ├── error.log  
│ ├── info.log  
│ └── warning.log  
├── modules  
│ ├── guesser.py  
│ ├── __init__.py  
│ ├── separator.py  
│ └── speech.py  
├── pretrained_models (*)
│ └── 2stems  
│ ├── checkpoint  
│ ├── model.data-00000-of-00001  
│ ├── model.index  
│ └── model.meta  
├── README.md  
├── requirements.txt
├── resources  
│ ├── log.yaml  
│ ├── properties.py  
│ └── <Google Cloud Password File>.json
└── src  
  ├── logger.py  
  └── main.py
```

Directories marked with a (*) will be created by the program as needed.

## Installation

This section expects the requirements stated in the previous section to be met and this is how this section has been written.

- **Program dependencies**: The program has some dependencies that must be installed in order to work. Those dependencies can be installed
  with the _requirements.txt_ file:
  - `pip install -r requirements.txt`
- It is highly recommended to use a **virtual environment** (*venv*), so the program dependencies installation will not conflict with the
  packages installed on the system.

If you want to run the program in a *venv*, open a terminal in the project's root folder and run:

```  
source path_to_your_virtual_environment/bin/activate  
pip install -r requirements.txt  
```  

If you do not want to run the program in a *venv*, open a terminal in the project's root folder and run:

```  
pip install -r requirements.txt  
```  

**Note**: If you have both **Python 2** and **Python 3** installed on your system, use **pip3** instead of **pip**.

## Configuration

There are some parameters that need to be set by the user, so the program can work. Those parameters are in the */resources/properties.py*
file.

- **GOOGLE_APPLICATION_CREDENTIALS**: This is the name of the *JSON* (with the extension) of the file with the credentials of the service
  account. The file must be located inside the `resources` folder.

- **BUCKET_NAME**: The name of the bucket created in *Google Cloud Storage* where the files will be uploaded and deleted.

There are other properties in the file, but they should not be changed unless you know what you are doing or if you want to continue with
the development of the program.

## How to use

This section explains how to use the program.

- Remember to activate the *venv* if you are using it.
- Add the root folder of the program to *Python*'s path variable:
  - `export PYTHONPATH=$PYTHONPATH:/full/path/project/root/folder/`
- Go to the `src` folder of the project and grant execute permissions to `main.py` file:
  - `$ chmod +x main.py`
- To run the program, from a terminal in the root directory, type:
  - `$ ./src/main.py`

This will show the usage:

```
usage: main.py [-h] {guess} ...

Extract the voice from the audio and transcribe it into text to find out what
is being said

optional arguments:
  -h, --help  show this help message and exit

Commands:
  {guess}
    guess     Extract the voice and transcribe it.
```

If you want to know how to use a specific command, for example the *guess* command, type:

```
usage: main.py guess [-h] --input INPUT --language_code LANGUAGE_CODE --model
                     {command_and_search,phone_call,video,medical_dictation,medical_conversation,default}

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT         Path to the audio file
  --language_code LANGUAGE_CODE
                        The BCP-47 code of the language spoken in the audio.
                        See the table at https://cloud.google.com/speech-to-
                        text/docs/languages for all available codes.
  --model {command_and_search,phone_call,video,medical_dictation,medical_conversation,default}
                        The type of transcription model to use. For more
                        details on each model see the table at
                        https://cloud.google.com/speech-to-
                        text/docs/transcription-
                        model#speech_transcribe_model_selection-python.
```

### Example of use

An example of use is:

```
./src/main.py guess --input samples/"Flo Rida - Zillionaire".mp3 --language_code en-US --model video
```

In the same folder where the audio file is, a folder with the name of the audio file will be created where the generated audio *WAV* files
and the transcription in a text file will be placed.

## Licensing agreement

Copyright © 2021 MinionAttack

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "
Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the
following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
