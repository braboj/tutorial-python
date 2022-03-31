"""
@file HilscherFramework/Configuration.py
@author Andreas Messer

@brief Configuration & Parameters

This file contains everything related to configuration parameters
for the test system. The user can influence the parameters using
config file for instance.
"""

from ConfigParser import SafeConfigParser, NoSectionError, NoOptionError
import atexit
import re
from CommandLine import opts

"""
@defgroup Config Configuration & Parameters
@brief Functions and classes to handle user changeable parameters. 

The configuration of the test system is organized as a tree of sections and 
parameters. Each section can contain a variable number of subsections and
parameters. Section names must not conatain a "." 
"""

# __all__ = ['getParameter', 'defineParameter', 'Section', 'Parameter', 'getSection', 'loadConfigurationFile',
#            'loadCommandLineOption', 'dumpConfigurationFile']

__config = SafeConfigParser()


def loadConfigurationFile(file):
    __config.read(file)


def loadCommandLineOption(opt):
    section, parameter, value = re.match('(.+)\\.(.+)\\s*=\\s*(.+)', opt).group(1, 2, 3)

    try:
        __config.add_section(section)
    except StandardError:
        pass

    __config.set(section, parameter, value)


def dumpConfigurationFile(file):
    def dump_config(file):
        fh = open(file, "w")

        try:
            __write_config_self(fh, __sections)
        finally:
            fh.close()

    atexit.register(dump_config, file)


class Section(object):
    """
    @brief Represents a section of the configuration tree.
    @ingroup Config
    
    In general this class should not be used directly.
    """

    def __init__(self, name):
        """
        @brief Constructor
        
        @param self Instance reference.
        @param name The name of the section.
        """
        self.name = name
        self.subsections = {}
        self.parameters = {}

    def getName(self):
        """
        @brief Get the name of the section.
        
        @param self Instance reference
        @return Name of section as string. 
        """
        return self.name

    def getSubsections(self):
        """
        @brief Get subsections of this section.
        
        @param self Instance reference.
        @return List of subsections.
        """
        return self.subsections.values()

    def getParameters(self):
        """
        @brief Get the parameters defined in this section.
        
        @param self Instance reference.
        @return List of parameters.
        """
        return self.parameters.values()

    def getSubSection(self, name):
        """
        @brief Get specific subsection
        
        @param self Instance Reference.
        @param name The name of the subsection.
        
        @exception KeyError The subsection does not exists. 
        @return The subsection.
        """
        return self.subsections[name]

    def getParameter(self, parameter_name):
        """
        @brief Get specific parameter
        
        @param self Instance Reference.
        @param parameter_name The parameter_name of the parameter.
        
        @exception KeyError The parameter does not exists. 
        @return The parameter.
        """
        return self.parameters[parameter_name]

    def addSubSection(self, section):
        """
        @brief Add a subsection.
        
        @param self Instance Reference.
        @param section The section to add as subsection.
        
        @exception KeyError Section with same name already exists. 
        """
        if section.name in self.subsections:
            raise KeyError("configuration subsection {name} already exists".format(name=section.name))

        self.subsections[section.name] = section

    def addParameter(self, parameter):
        """
        @brief Add a parameter.
        
        @param self Instance Reference.
        @param parameter The parameter to add.
        
        @exception KeyError Parameter with same name already exists. 
        """
        if parameter.name in self.parameters:
            raise KeyError("configuration parameter {name} already exists".format(name=parameter.name))

        self.parameters[parameter.name] = parameter


class Parameter(object):
    """
    @brief Class to used for parameters in configuration tree.
    @ingroup Config
    
    In general this class should not be instantiated directly. Please
    use function defineParameter to create a new parameter.
    """

    def __init__(self, name, description, default):
        """
        @brief Constructor
        
        @param self Instance reference.
        @param name The name of the parameter.
        @param description A short description of what the parameter influences.
        @param default The default value of the parameter
        """

        self.name = name
        self.description = description
        self.default = default
        self.value = default

    def getValue(self):
        """
        @brief Get the current value.
        
        @param self Instance reference.
        @return Current value as string.
        """
        return str(self.value)

    def setValue(self, value):
        """
        @brief Set the value.
        
        @param self Instance reference.
        @param value The new value.
        """
        self.value = value

    def getName(self):
        """
        @brief Get the name of the parameter.
        
        @param self Instance reference.
        @return The name of the parameter as string.
        """
        return str(self.name)

    def getDescription(self):
        """
        @brief Get the description of the parameter.
        
        @param self Instance reference.
        @return The description of the parameter as string.
        """
        return str(self.description)

    def getDefaultValue(self):
        """
        @brief Get the default value of the parameter.
        
        @param self Instance reference.
        @return The default value as string.
        """
        return str(self.default)


__sections = Section("root")


def getSection(section_name):
    """
    @brief Get a specific section.
    @ingroup Config

    Searches the configuration tree for the specified section and returns
    the section object. Usually this function has not to be used directly.

    @param section_name Name of section as string. Use a "." as separator between subsections.
    @exception KeyError If the section does not exists.
    @return The requested section.
    @sa defineParameter()
    """
    current = __sections

    if section_name != "":
        tree = section_name.split(".")

        for elem in tree:
            current = current.getSubSection(elem)

    return current


def createSection(section_name):
    """
    @brief Create a new section in configuration tree.
    @ingroup Config
    
    Tries to create a new section in configuration tree if the requested
    section does not exits. Returns a reference to the section. 
    Usually this function has not to be used directly.

    @param section_name Name of section as string. Use a "." as separator between subsections.
    @exception KeyError If the section does not exists.
    @return The section.
    @sa defineParameter()
    """
    tree = section_name.split(".")

    current = __sections

    for elem in tree:
        try:
            current = current.getSubSection(elem)
        except KeyError:
            s = Section(elem)
            current.addSubSection(s)
            current = s

    return current


def defineParameter(section_name, parameter_name, description, default):
    """
    @brief Define a user configurable parameter.
    @ingroup Config
    
    Function creates a new Parameter object and inserts it
    into the specified section_name of configuration tree.
    
    @param section_name The parameters section_name. A "." can be used to separate
                        subsections.
    @param parameter_name The of the parameter to create.
    @param description Description of what the parameter influences.
    @param default The default value of the parameter
    
    @exception KeyError A parameter with same name already exists in the 
                        specified section.
    
    @return The created parameter object  
    """

    try:
        s = getSection(section_name)
    except KeyError:
        s = createSection(section_name)

    try:
        p = s.getParameter(parameter_name)
    except KeyError:
        p = Parameter(parameter_name, description, default)

        try:
            p.value = __config.get(section_name, parameter_name)
        except (NoSectionError, NoOptionError):
            pass

        s.addParameter(p)

    return p


def getParameter(section_name, parameter_name):
    """
    @brief Search the configuration tree for a parameter.
    @ingroup Config
    
    @param section_name The parameter_name of the section the parameter is in. Use "." to 
                        separate subsections.
    @param parameter_name The name of the parameter.
    @exception KeyError Either the section or the parameter was not found.
    @return The requested parameter object.
    """
    s = getSection(section_name)

    return s.getParameter(parameter_name)


def __write_config(config, section, name=None):
    if len(section.parameters) > 0:
        config.add_section(name)

        for param in section.parameters.values():
            config.set(name, param.name, str(param.value))

    for subsection in section.subsections.values():
        if name is not None:
            __write_config(config, subsection, name + "." + subsection.name)
        else:
            __write_config(config, subsection, subsection.name)


def __write_config_self(file, section, name=None):
    if len(section.parameters) > 0:
        file.write("[{section}]\n".format(section=name))

        params = section.parameters.keys()
        params.sort()

        for name in params:
            param = section.parameters[name]
            file.write("# {param.name}: {param.description}\n".format(param=param))
            file.write("{param.name} = {param.value}\n".format(param=param))

    for subsection in section.subsections.values():
        if name is not None:
            __write_config_self(file, subsection, name + "." + subsection.name)
        else:
            __write_config_self(file, subsection, subsection.name)


if opts.options.config_file:
    loadConfigurationFile(opts.options.config_file)

if opts.options.settings:
    for elem in opts.options.settings:
        loadCommandLineOption(elem)
