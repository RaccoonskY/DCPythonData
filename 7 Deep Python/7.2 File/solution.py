import os.path
import tempfile
import uuid

"""
This solution gives:
(1) example of working with files in python with
(2) implementing new behaviour to the default methods of P
(3) by using overloading magic methods such as: 
(4) __str__ to give string representation of File (absolute path of file here)
(5) __add__ overloads '+' for two files
(6) __iter__ returns iterable object (here it's RO file)
(7) __next__ gives us new object from the sequence 

PS. 'sequence' means not 'python sequence' (list,tuple etc) but objects from iterable instance
and with __iter__ and __next__ we get generator of string sequence
*Methods are too small to be commented separately*
"""


class File:
    def __init__(self, file_path: str):
        self.path = file_path
        if not os.path.exists(file_path):
            f = open(file_path, 'w')
            f.close()

    def read(self):
        with open(self.path, "r") as file:
            return file.read()

    def write(self, new_string: str):
        with open(self.path, "w") as file:
            file.write(new_string)
            return len(new_string)

    def __str__(self):
        return os.path.abspath(self.path)

    def __add__(self, other):
        with open(self.path, 'r') as a, open(other.path, 'r') as b:
            summary_string = a.read() + b.read()
            # tempfile.gettempdir() gives us path to current os temp dir and uuid.uuid4 gives unique sequence
            new_file = File(os.path.join(tempfile.gettempdir(), str(uuid.uuid4())))
            new_file.write(summary_string)
            return new_file

    def __iter__(self):
        self.file = open(self.path, 'r')
        return self.file

    def __next__(self):
        current = self.file.readline()
        if current == '':
            self.file.close()
            raise StopIteration
        return current  

