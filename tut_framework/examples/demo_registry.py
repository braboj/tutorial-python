import tut_framework.header.errors as errors
import tut_framework.header.comm as comm

from tut_framework.components.Registries import Registry, CommStateRegistry, ErrorCodeRegistry


def test_registry():

    print("#" * 120)

    # Demonstrate registry class
    reg = Registry(name="Test Registry")
    reg.register(key="TC1", value=1)
    reg.register(key="TC2", value=2)

    key = reg.getKeyByValue(value=1)
    value = reg.getValueByKey(key="TC1")
    print(key)
    print(value)
    print("")

    print(reg.getKeys())
    print(reg.getValues())
    print("")

    reg.unregister(key="TC2")
    print(reg.getKeys())
    print(reg.getValues())
    print("")


def test_error_registry():

    print("#" * 120)

    # Demonstrate registry class
    error_reg = ErrorCodeRegistry(name="Test Error Registry")
    error_reg.registerErrorCodes(dictionary=vars(errors), regexp="^CIFX_", raise_on_doubles=True)

    print(error_reg.getKeys())
    print(error_reg.getValues())
    print("")

    print(error_reg.getErrorCodeByErrorName(errorname="CIFX_NO_ERROR"))
    print(error_reg.getErrorNamebyErrorCode(errorcode=0))
    print("")


def test_comm_state_registry():

    print("#" * 120)

    # Demonstrate registry class
    state_reg = CommStateRegistry(name="Test Comm State Registry")
    state_reg.registerCommStatCode("COMM_STATE_UNKNOWN", comm.RCX_COMM_STATE_UNKNOWN)
    state_reg.registerCommStatCode("COMM_STATE_NOT_CONFIGURED", comm.RCX_COMM_STATE_NOT_CONFIGURED)
    state_reg.registerCommStatCode("COMM_STATE_STOP", comm.RCX_COMM_STATE_STOP)
    state_reg.registerCommStatCode("COMM_STATE_IDLE", comm.RCX_COMM_STATE_IDLE)
    state_reg.registerCommStatCode("COMM_STATE_OPERATE", comm.RCX_COMM_STATE_OPERATE)

    print(state_reg.getKeys())
    print(state_reg.getValues())
    print("")


if __name__ == "__main__":
    test_registry()
    test_error_registry()
    test_comm_state_registry()