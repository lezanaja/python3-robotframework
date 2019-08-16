from .Face import Face
from .LeftHand import LeftHand


class AwareLibrary(Face, LeftHand):
    def __init__(self):
        Face.__init__(self)
        LeftHand.__init__(self)

    def get_hello_world(self):
        return "Helloworld"
