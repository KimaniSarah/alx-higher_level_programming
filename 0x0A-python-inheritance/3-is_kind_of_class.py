#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Args:
        obj: the object taht is being checked
        a_class:the class we are checking
    Return:
    True if the object is an instance of,or if the object is an
    instance of a class that inherited from,the specified clas
    """
    def inherits_from(obj, a_class):
        return isinstance(obj, a_class)
    for subclass in type(obj).mro():
        if subclass == a_class:
            return True
    return False