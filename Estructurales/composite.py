#COMPOSITE
class FileSystemComponent:
    def display(self, indent=0):
        pass

class File(FileSystemComponent):
    def __init__(self, name):
        self.name = name

    def display(self, indent=0):
        print(" " * indent + self.name)

class Folder(FileSystemComponent):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add(self, component):
        self.children.append(component)

    def display(self, indent=0):
        print(" " * indent + f"Folder: {self.name}")
        for child in self.children:
            child.display(indent + 2)

# Uso COMPOSITE
file1 = File("file1.txt")
file2 = File("file2.txt")
folder = Folder("Documentos")
folder.add(file1)
folder.add(file2)

root = Folder("Root")
root.add(folder)

root.display()