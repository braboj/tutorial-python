## Authors
- Branimir Georgiev (bgeorgiev@hilscher.com)
- Yordan Dragnev (ydragnev@hilscher.com)

## Usage

```python
# Use the vendor library to initialize the CAN capable device
device = ... (HilscherFramework.Stacks, Saleae, IXXAT, etc...)

# Create the CAN interface
can = CanNode(device)

# Accept messages from a CAN node with address 0x01
can.start_listen(can_id=0x01)

# Wait for a message from a CAN node with address 0x01
message = can.recv(timeout=0x01)
print(message)

# Create a CAN frame
frame = CanFrame(can_id=0x01, data=[1, 2, 3, 4, 5, 6, 7, 8])

# Send a frame to a CAN node with address 0x01
can.send(frame)

# Ignore message from a CAN node with address 0x01
can.stop_listen(can_id=0x01)

```