import os
import modules.analyser
hiddenimports = [
    "lib.functions",
    "subprocess",
    "shutil",
    "hashlib",
    "qimage2ndarray",
    "matplotlib"
]


tmp = os.path.dirname(modules.analyser.__file__) + "\\modules_analyser"
base = tmp + "\\"
tmp = os.listdir(tmp)

for item in tmp:
    if item.endswith('.py') is True and item[0] != '_':
        temp = item.split(".")[0]
        temp = "modules.modules_analyser." + temp
        hiddenimports.append(temp)
