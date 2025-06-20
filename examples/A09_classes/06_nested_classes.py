# Nested classes for constants, settings, etc.
# ------------------------------------------------------------------------------
# Classes can contain other classes that serve as containers for related
# constants or configuration. Nesting keeps these auxiliary definitions close to
# the code that uses them.

class Settings:

    LANG = "English"
    THEME = "Light"
    IP_ADDR = "192.168.210.10"
    PORT = 8080

    class AdvancedSettings:

        ENABLE_LOGGING = False
        MAX_CONNECTIONS = 10

    class ExperimentalSettings:

        ENABLE_NEW_FEATURE = False


# Access the basic settings
print(Settings.THEME)

# Access the b settings
print(Settings.AdvancedSettings.ENABLE_LOGGING)  # Output: False

# Access the experimental settings
print(Settings.ExperimentalSettings.ENABLE_NEW_FEATURE)  # Output: False
