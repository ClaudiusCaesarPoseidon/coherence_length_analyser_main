import os
import modules.eigen_widgets
hiddenimports = [
    "sys",
    "os",
    "re",
    "code",
    "lib.functions",
    "qtpy"
]


tmp = os.path.dirname(modules.eigen_widgets.__file__) + \
    "\\modules_eigen_widgets"
base = tmp + "\\"
tmp = os.listdir(tmp)

for item in tmp:
    if item.endswith('.py') is True and item[0] != '_':
        temp = item.split(".")[0]
        temp = "modules.modules_eigen_widgets." + temp
        hiddenimports.append(temp)
