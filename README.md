

# PST2MBOX v1.0.0

A simple Windows GUI tool to convert Microsoft Outlook PST files to MBOX format using WSL and `readpst`.

---

## 📥 Download

Download the latest executable from the **Releases** section.

---

## 📸 Screenshot

<img width="694" height="322" alt="PST2MBOXv1 0 0" src="https://github.com/user-attachments/assets/1d69e20f-4e99-4e55-9d01-125f6d702912" /> <br>
Version 1.0.0

<img width="693" height="324" alt="PST2MBOXv0 1" src="https://github.com/user-attachments/assets/cb2b52b3-1839-462f-879c-63586430a2fd" /> <br>
Version v0.1


## ✨ Features

* Convert Outlook PST to MBOX
* Simple and lightweight PyQt GUI
* Uses WSL and `readpst` for reliable conversion
* Handles large PST files
* Preserves folder structure

---

## ⚙️ Requirements

* Windows 10 or 11
* WSL (Windows Subsystem for Linux)
* `readpst` installed in WSL

---

## 🛠️ Setup

### 1. Install WSL

```bash
wsl --install
```

### 2. Install readpst inside WSL

```bash
sudo apt update
sudo apt install pst-utils
```

---

## ▶️ Usage

1. Launch the application
2. Select a `.pst` file
3. Select an output folder
4. Click **Convert**

---

## 📂 Output

* MBOX files are generated per folder
* Files are written to the selected output directory

---

## ⚠️ Known limitations

* Large PST conversions can be CPU-intensive
* UI may feel temporarily less responsive during conversion
* Conversion performance depends on PST size, disk speed, and WSL overhead
* Requires WSL and `readpst`

---

## 🧠 How it works

```
PyQt GUI
   ↓
WSL subprocess
   ↓
readpst
   ↓
MBOX output
```

---

## 🚀 Roadmap

### v1.1.0 — UI & Performance Improvements

* Improve UI responsiveness (no “not responding” feel)
* Stream conversion logs in real-time
* Add progress feedback during conversion
* Disable UI controls while conversion is running
* Optional cancel button

---

### Future ideas

* Auto-open output folder after conversion
* Improved error handling
* Better input validation
* Optional installer (setup.exe)
* UI polish

---

## 📜 License

Apache 2.0

---

## 👤 Author

HoodedUnicorn

---

## 🎨 Credits

Icon by NajmunNahar from Flaticon
