import sys
import subprocess
from PyQt5 import QtWidgets


def to_wsl_path(path):
    # Convert C:\Users\... → /mnt/c/Users/...
    return path.replace("C:", "/mnt/c").replace("\\", "/")


class PST2MBOX(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PST → MBOX Converter (WSL) v1.0.0")
        self.setGeometry(300, 300, 700, 300)

        layout = QtWidgets.QVBoxLayout()

        self.pst_path = QtWidgets.QLineEdit()
        self.out_path = QtWidgets.QLineEdit()

        self.btn_pst = QtWidgets.QPushButton("Select PST File")
        self.btn_out = QtWidgets.QPushButton("Select Output Folder")
        self.btn_run = QtWidgets.QPushButton("Convert")

        self.log = QtWidgets.QTextEdit()
        self.log.setReadOnly(True)

        layout.addWidget(self.pst_path)
        layout.addWidget(self.btn_pst)
        layout.addWidget(self.out_path)
        layout.addWidget(self.btn_out)
        layout.addWidget(self.btn_run)
        layout.addWidget(self.log)

        self.setLayout(layout)

        self.btn_pst.clicked.connect(self.pick_pst)
        self.btn_out.clicked.connect(self.pick_out)
        self.btn_run.clicked.connect(self.run_convert)

    def pick_pst(self):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select PST")
        self.pst_path.setText(file)

    def pick_out(self):
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Output")
        self.out_path.setText(folder)

    def log_msg(self, msg):
        self.log.append(msg)

    def run_convert(self):
        pst = self.pst_path.text()
        out = self.out_path.text()

        if not pst or not out:
            self.log_msg("❌ Select PST and output folder")
            return

        pst_wsl = to_wsl_path(pst)
        out_wsl = to_wsl_path(out)

        cmd = [
            "wsl",
            "readpst",
            "-o",
            out_wsl,
            pst_wsl
        ]

        self.log_msg("🚀 Running conversion...")
        self.log_msg(" ".join(cmd))

        process = subprocess.run(cmd, capture_output=True, text=True)

        self.log_msg(process.stdout)
        self.log_msg(process.stderr)

        self.log_msg("✅ Done")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = PST2MBOX()
    win.show()
    sys.exit(app.exec_())