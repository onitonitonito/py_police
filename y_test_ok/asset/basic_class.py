"""
# Basic Class for Inheritance!
# Download! Everyone!
#
#\n\n\n"""
print(__doc__)
import inspect

class Basic_Kind(object):
    def __init__(self):
        activated = "... '{:}' IS GENERATED! ...".format(self.__class__.__name__)

        frame = inspect.currentframe()

        print(activated)
        print()
