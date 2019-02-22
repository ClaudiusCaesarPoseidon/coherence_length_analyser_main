import os
import modules.register
hiddenimports = [
    "lib.functions",
    "hashlib",
]


tmp = os.path.dirname(modules.register.__file__) + "\\modules_register"
base = tmp + "\\"
tmp = os.listdir(tmp)

for item in tmp:
    if item.endswith('.py') is True and item[0] != '_':
        temp = item.split(".")[0]
        temp = "modules.modules_register." + temp
        hiddenimports.append(temp)
