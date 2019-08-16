from .Face import Face
from .LeftHand import LeftHand


class AwareLibrary(Face, LeftHand):
    def __init__(self):
        Face.__init__(self)
        LeftHand.__init__(self)

    def get_hello_world(self):
        return "Helloworld"

    def get_method_void(self):
        print('Void')

    def get_method_with_parameter(self, id):
        print('id:' + str(id))

    def get_method_with_return(self):
        return 'Aware'
