# Example : Demonstrate that both lamda and def return the same result when compiled
import dis

func1 = lambda x: x * x


def func2(x):
    return x * x


print(dis.dis(func1))
print(dis.dis(func2))
