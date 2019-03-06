#import os
#
#def ssplit_path(path):
#    path_list = []
#    if os.path.isabs(path) is True:
#        path = path.split(os.sep)
#        for item in path:
#            path_list.append(item)
#        if os.name == 'nt':
#            path_list[0] = os.path.join(path_list[0], os.sep)
#        else:
#            path_list[0] = os.sep
#    else:
#        path = path.split(os.sep)
#        for item in path:
#            path_list.append(item)
#    return path_list
#
#
#
#path = r"C:\fgh\abc\vcd\dfg\sdf\sdf\sdf"
#print(ssplit_path(path))
##path = r"fgh\abc"
##split_path(path)

from PySide2 import QtCore

class Test(object):
    valueChanged = QtCore.Signal(object)
    def __init__(self):
        super().__init__()
        print("Ich werde aufgerufen.")
        self._glubber = 1


    @property
    def glubber(self):
        return self._glubber

    @glubber.setter
    def glubber(self, value):
        self._glubber = value
        self.valueChanged.emit()


class Test2(Test):
    def __init__(self):
        super().__init__()


if __name__ == '__main__':
    test = Test2()