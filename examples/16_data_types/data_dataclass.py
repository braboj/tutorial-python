# Lightweight data classes
# -----------------------------------------------------------------------------
# Dataclasses eliminate boilerplate when defining classes meant primarily to store data.

import dataclasses
from dataclasses import dataclass, field
from typing import List


@dataclass
class DataClass(object):
    name: str
    value: int

    def __post_init__(self):
        self.value = self.value * 2

    def __str__(self):
        return f"{self.name}: {self.value}"


@dataclass
class DataClassWithDefaults(DataClass):

    name: str = "MyData with defaults"
    value: int = 0
    data: List[int] = field(default_factory=list)

    def add_value(self, value):
        self.data.append(value)

    def __str__(self):
        return f"{self.name}: {self.value}, {self.data}"


if __name__ == "__main__":

    my_data = DataClass(name="MyData", value=10)
    print(my_data)

    my_data = DataClassWithDefaults()
    my_data.add_value(1)
    print(my_data)
