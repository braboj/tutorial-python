from __future__ import print_function


###################################################################################################
# ERRORS                                                                                        100
###################################################################################################

class BaseAppError(Exception):
    pass


###################################################################################################
# MATERIALS                                                                                     100
###################################################################################################

class Material(object):
    symbol = "-"
    price = None

    def __init__(self, color=""):
        self.color = color


class Wood(Material):
    symbol = "W"
    price = 10


class Metal(Material):
    symbol = "M"
    price = 20


###################################################################################################
# TABLE LOGIC                                                                                   100
###################################################################################################

class Table(object):

    def __init__(self, template):
        self.template = template
        self.__table = self.__construct_table(template)

    @staticmethod
    def __construct_table(template):
        matrix = []
        try:
            for row in template:
                vector = []
                for element in row:
                    vector.append(element())
                matrix.append(vector)
        except Exception as e:
            raise BaseAppError(e)

        return matrix

    @classmethod
    def from_list(cls, template):
        table = cls(template)
        return table

    @property
    def table(self):
        return self.__table

    @table.setter
    def table(self, value):
        self.__table = value

    @property
    def price(self):
        try:
            price = 0
            for row in self.table:
                for element in row:
                    price += element.price
            return price
        except Exception as e:
            raise BaseAppError(e)


###################################################################################################
# VISUALIZATION                                                                                 100
###################################################################################################

class Printer(object):

    @staticmethod
    def print(table, attribute):

        # Convert attribute names to lowercase
        attribute = attribute.lower()

        # Extract the values from the table
        try:
            result = ""
            for row in table:
                line = ""
                for element in row:
                    # Use string name to get the attribute value
                    value = getattr(element, attribute)
                    line += str(value) + " "
                result += line

            print(result)

        except Exception as e:
            raise BaseAppError(e)


###################################################################################################
# APPLICATION                                                                                   100
###################################################################################################

# Create the viewer
pp = Printer()

# Demonstrate usage of the default constructor
table_design = [[Wood, Wood, Wood], ]
table1 = Table(template=table_design)

print('-' * 40)
pp.print(table1.table, "symbol")
pp.print(table1.table, "price")
print(table1.price)

# Demonstrate the usage of a named constructor
table_design[-1][-1] = Metal
table2 = Table.from_list(template=table_design)

print('-' * 40)
pp.print(table2.table, "symbol")
pp.print(table2.table, "price")
print(table2.price)
