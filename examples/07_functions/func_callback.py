# Using callback functions to handle events
# --------------------------------------------------------------------------------
# A callback function is passed as an argument to another function and executed
# when a particular event occurs. This technique lets the caller customize
# behavior without changing the callee. Callbacks are common in event-driven
# architectures and asynchronous code.

_listeners = {}

def on(event_name, callback):
    _listeners.setdefault(event_name, []).append(callback)


def emit(event_name, *args, **kwargs):
    for callback in _listeners.get(event_name, []):
        callback(*args, **kwargs)


def handle_data(data):
    print(f"[DATA] Received: {data!r}")


def handle_error(msg):
    print(f"[ERROR] {msg}")


on("data", handle_data)
on("error", handle_error)

emit("data", {"id": 1, "value": 42})
emit("data", {"id": 2, "value": 99})
emit("error", "Timeout occurred")
