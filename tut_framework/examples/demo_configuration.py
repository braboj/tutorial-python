from tut_framework.components.Configuration import Section, Parameter
from tut_framework.components.Configuration import defineParameter, getParameter
from tut_framework.components.Configuration import createSection, getSection


def test_section_classes():

    print("#" * 120)

    s = Section(name="Config")

    s1 = Section(name="Bus")

    p1 = Parameter(name="Baudrate", description="CAN bus speed", default=125)
    s1.addParameter(parameter=p1)

    p2 = Parameter(name="SlaveAddr", description="Slave's Node-ID", default=0)
    s1.addParameter(parameter=p2)

    p3 = Parameter(name="MasterAddr", description="Master's Node-ID", default=1)
    s1.addParameter(parameter=p3)

    s.addSubSection(s1)

    print(s.getSubSection(name="Bus").getName())
    print(s1.getParameter(parameter_name="Baudrate").value)

    print("")


def test_section_methods():

    print("#" * 120)

    createSection("Config")

    # Create new parameter in a section
    defineParameter("Config.Test", "Baudrate", "CAN bus speed", 125)
    print(getParameter("Config.Test", "Baudrate").value)

    # Access directly the value of the parameter
    getParameter(section_name="Config.Test", parameter_name="Baudrate").value = 250
    print(getParameter("Config.Test", "Baudrate").value)

    # Access the value of the parameter using section names
    print(getSection(section_name="Config.Test").parameters["Baudrate"].value)
    getSection(section_name="Config.Test").parameters["Baudrate"].value = 500
    print(getSection(section_name="Config.Test").parameters["Baudrate"].value)

    print("")


def test_nested_sections():

    print("#" * 120)

    defineParameter(section_name="Config.Bus", description="", parameter_name="Baudrate", default=125)
    defineParameter(section_name="Config.Bus", description="", parameter_name="SlaveAddr", default=0)
    defineParameter(section_name="Config.Bus", description="", parameter_name="MasterAddr", default=1)

    print(getParameter("Config.Bus", "Baudrate").value)

    print("")


if __name__ == "__main__":
    test_section_classes()
    test_section_methods()
    test_nested_sections()
