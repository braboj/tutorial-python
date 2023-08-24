# https://commons.wikimedia.org/wiki/File:W3sDesign_Dependency_Injection_Design_Pattern_UML.jpg
#https://maximilienandile.github.io/2019/10/20/Dependency-injection-what-is-it-how-to-do-it-in
# -Java-and-why-to-use-it/
# https://www.youtube.com/watch?v=IKD2-MAkXyQ

class A(object):

    def __init__(self):
        super(A, self).__init__()


class B(object):

    def __init__(self, param: type):
        super(B, self).__init__()

        # This is a dependency injection
        self.o = param()


b = B(A)
print(type(b.o))
print(b.o)
