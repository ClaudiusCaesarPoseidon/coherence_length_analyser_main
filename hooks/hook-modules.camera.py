import os
import modules.camera
hiddenimports = [
    "lib.functions",
    "datetime",
    "qimage2ndarray"
]


tmp = os.path.dirname(modules.camera.__file__) + "\\modules_camera"
base = tmp + "\\"
tmp = os.listdir(tmp)

for item in tmp:
    if item.endswith('.py') is True and item[0] != '_':
        temp = item.split(".")[0]
        temp = "modules.modules_camera." + temp
        hiddenimports.append(temp)
