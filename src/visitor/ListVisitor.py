from visitor.Visitor import Visitor
from visitor.File import File
from visitor.Directory import Directory


class ListVisitor(Visitor):
    def __init__(self):
        self.currentdir = ""

    def visit(self, entry):
        if isinstance(entry, File):
            print("{0}/{1}".format(self.currentdir, entry))
        elif isinstance(entry, Directory):
            print("{0}/{1}".format(self.currentdir, entry))
            savedir = self.currentdir
            self.currentdir = "{0}/{1}".format(self.currentdir, entry.getName())
            for _, dir in enumerate(entry.dir):
                dir.accept(self)
            self.currentdir = savedir
