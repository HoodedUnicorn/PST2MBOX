# PST2MBOX v0.1

A simple Windows GUI tool to convert Microsoft Outlook PST files to MBOX format using WSL and readpst.

## Screenshot

<img width="693" height="324" alt="PST2MBOXv0 1" src="https://github.com/user-attachments/assets/cb2b52b3-1839-462f-879c-63586430a2fd" /> <br>
Version v0.1


## Features

- Convert Outlook PST to MBOX
- Simple and lightweight PyQt GUI
- Uses WSL and readpst for reliable conversion
- Handles large PST files
- Preserves folder structure

## Requirements

- Windows 10 or 11
- WSL (Windows Subsystem for Linux)
- `readpst` installed in WSL

## Setup

### 1. Install WSL

```bash
wsl --install
```

### 2. Install readpst inside WSL
```bash
sudo apt update
sudo apt install pst-utils
```

### Usage
1. Launch the application
2. Select a .pst file
3. Select an output folder
4. Click Convert

### Output
- MBOX files are generated per folder
- Files are written to the selected output directory

### Notes
- Large PST files may take time to process
- The application may use high CPU during conversion
- WSL is required
- Output structure depends on PST content

### Download
Download the latest executable from the Releases section

### How it works
PyQt GUI <br>
   ↓<br>
WSL subprocess<br>
   ↓<br>
readpst<br>
   ↓<br>
MBOX output<br>

### Known limitations

- Large PST conversions may temporarily feel unresponsive while processing.
- Conversion performance depends on PST size, disk speed, WSL overhead, and readpst behavior.
- Progress reporting and responsiveness will be improved in a future release.

### License

Apache 2.0

### Author
HoodedUnicorn
