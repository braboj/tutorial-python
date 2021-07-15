from optparse import OptionParser
import sys


__parser = OptionParser()

__parser.add_option("-c", "--config",
                    action="store", dest="config_file",
                    help="read configuration from FILE", metavar="FILE")

__parser.add_option("-s", "--setting",
                    action="append", dest="settings",
                    help="override configuration parameter with given value e.g. -s Tests.UnattendedMode=yes")

__parser.add_option("--tc-property",
                    action="append", dest="properties",
                    help='add a testcase property which should included to the test run e.g --tc-property api '
                         '--tc-property reset"')

__parser.add_option("--dump-config",
                    action="store", dest="dump_config_file",
                    help="write configuration to FILE", metavar="FILE")

__parser.add_option("--list-testcases",
                    action="store_true", dest="list_testcases",
                    help="List Information About Testcases instead of running them")

__parser.add_option("--list-devices",
                    action="store_true", dest="list_devices",
                    help="List Information About Devices instead of running them")

__parser.add_option("-v", "--version",
                    action="store_true", dest="show_version",
                    help="Show version of the application")


class __Opts(object):
    pass


opts = __Opts()

if 'waflib.Scripting' in sys.modules:
    # allow integrating testframework into waf
    # do not parse the commad line
    (opts.options, opts.args) = __parser.parse_args([], None)

elif "pydev_runfiles_unittest" in sys.modules or "pydev_runfiles_xml_rpc" in sys.modules:
    # workaround for pydev unittest
    # do not parse the commad line
    (opts.options, opts.args) = __parser.parse_args([], None)

else:
    (opts.options, opts.args) = __parser.parse_args()

# determinate the resulting action
if opts.options.show_version:
    opts.action = "show-version"

elif opts.options.dump_config_file is not None:
    opts.action = "dump-config"

elif opts.options.list_testcases:
    opts.action = "list-testcases"

elif opts.options.list_devices:
    opts.action = "list-devices"

else:
    opts.action = "run-tests"
