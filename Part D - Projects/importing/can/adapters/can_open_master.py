# coding=utf-8
from __future__ import print_function
from __future__ import unicode_literals

# Framework libraries
from Components.can.frame import *
from Components.can.interface import CanNodeABC
from Components.CANDL.Device import *

# Add the local directories to the system path
import sys
sys.path.append(str("."))
sys.path.append(str(".."))


class CanNode(CanNodeABC):
    """ A CAN adapter for the CanOpenMaster Device from HilscherFramework

    Args:
         device     : Instance of a CANDL capable device (adaptee)

    Attributes:
        node_list   : A pool of CAN addresses that the node listens to
        pool        : A pool of CAN frames received by the node


    Examples:

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

    """

    def __init__(self, device):
        super(CanNode, self).__init__(device=device)
        self.log = logging.getLogger(self.__class__.__name__)

        self.node_list = []
        self.pool = []

    ##########################################################################################

    def reset(self):
        """ Resets the CAN device """

        try:
            self.device.reset_system()
            self.device.wait_ready()

        except Exception as e:
            self.log.error(e)

    ##########################################################################################

    def configure(self, node_id=1, baudrate=125):
        """ Configures the bus parameters of the device

        Args:
            node_id     (int, optional)   : Address to be used by the master device (1..127)
            baudrate    (int, optional)   : Baudrate to be used by the master device

            Valid baud rates of CANopen Network
                    * 1000    : CANOPEN_MASTER_CFG_BAUD_1000 (1 MBaud)
                    * 800     : CANOPEN_MASTER_CFG_BAUD_800  (800 KBaud)
                    * 500     : CANOPEN_MASTER_CFG_BAUD_500  (500 KBaud)
                    * 250     : CANOPEN_MASTER_CFG_BAUD_250  (250 KBaud)
                    * 125     : CANOPEN_MASTER_CFG_BAUD_125  (125 KBaud)
                    * 100     : CANOPEN_MASTER_CFG_BAUD_100  (100 KBaud)
                    * 50      : CANOPEN_MASTER_CFG_BAUD_50   (50 KBaud)
                    * 20      : CANOPEN_MASTER_CFG_BAUD_20   (20 KBaud)
                    * 10      : CANOPEN_MASTER_CFG_BAUD_10   (10 KBaud)

        """

        baudrates = {
            1000: API_V2.CANOPEN_MASTER_CFG_BAUD_1000,
            800: API_V2.CANOPEN_MASTER_CFG_BAUD_800,
            500: API_V2.CANOPEN_MASTER_CFG_BAUD_500,
            250: API_V2.CANOPEN_MASTER_CFG_BAUD_250,
            125: API_V2.CANOPEN_MASTER_CFG_BAUD_125,
            100: API_V2.CANOPEN_MASTER_CFG_BAUD_100,
            50: API_V2.CANOPEN_MASTER_CFG_BAUD_50,
            20: API_V2.CANOPEN_MASTER_CFG_BAUD_20,
            10: API_V2.CANOPEN_MASTER_CFG_BAUD_10
        }

        try:
            self._register_application()
            self.device.configure(node_id, baudrates[baudrate])

        except Exception as e:
            self.log.error(e)

    ##########################################################################################

    def deconfigure(self):
        """ Clears the device configuration and resets the device """

        try:
            self.device.deconfigure()

        except Exception as e:
            self.log.error(e)

    ##########################################################################################

    def start_listen(self, can_id):
        """ Add one or more CAN-IDs to the listener

        Args:
            can_id  : List of CAN-IDs to be registered for listening

        """

        # Check for iteration capabilities
        try:
            iter(can_id)
            can_id = list(can_id)
        except TypeError:
            can_id = [can_id, ]

        # Fills in the list of listened nodes ID by ID
        try:
            if can_id:
                for node in can_id:
                    self._set_listener(node)
                    self.node_list.append(node)
            else:
                for node in self.node_list:
                    self._set_listener(node)
                    self.node_list.extend(node)

            self.device.enable_receive()

        except ValueError:
            pass

    ##########################################################################################

    def stop_listen(self, can_id):
        """ Remove one or more CAN-IDs from the listener

        Args:
            can_id  : List of CAN-IDs to be unregistered for listening

        """

        # Check for iteration capabilities
        try:
            iter(can_id)
            can_id = list(can_id)
        except TypeError:
            can_id = [can_id, ]

        # Clears the list of listened nodes ID by ID
        try:
            if can_id:
                for node in can_id:
                    self._clear_listener(node)
                    self.node_list.remove(node)
            else:
                for node in self.node_list:
                    self._clear_listener(node)
                    self.node_list = []

        except ValueError:
            pass

    ##########################################################################################

    def send(self, frame, timeout=0):
        """ Transmits a raw CAN frame

        Args:
            frame (:obj:CanFrame)   : Instance of class CanFrame()
            timeout (int, optional) : Maximum wait time for confirmation from the master

        """

        # The message array to prepare for sending
        message = []

        # Unique packet identifier, not sent to network
        unique_id = 0

        # Part of the frame information to set the frame as extended
        extended_frame_value = 0x80000000

        # Part of the frame information to set the frame as basic
        basic_frame_value = 0x0

        # Check the type of frame and sets the maximum frame number
        if type(frame) is CanFrameExtended:
            frame_info = extended_frame_value
        else:
            frame_info = basic_frame_value

        # Check if the RTR value is set and forms the "frame_info" packet field
        if frame.rtr:
            frame_info += 0x10

        # Forming the packet structure
        message.append([])
        message[0].append(unique_id)
        message[0].append(frame_info)
        message[0].append(frame.can_id)
        message[0].append(frame.data)

        # Trying to send the formed frame and waits for respond
        try:
            self.device.send_frame_service(frames_data=message)
            if timeout:
                self.device.wait_packet()

        except Exception as e:
            self.log.error(e)

    ##########################################################################################

    def recv(self, timeout=10):
        """ Receives a raw CAN frame

        Args:
            timeout (int, optional)   : Maximum wait time for indications from the master
        """

        if len(self.pool) == 0:
            try:
                indication = self.device.wait_packet(timeout=timeout)
                indication = castTo(indication, API_V2.CAN_DL_PACKET_DATA_IND_T)
                self._handle_indication(self.device, indication)

            except PacketTimeout as e:
                self.log.debug(e)

        result = self.pool.pop(0) if len(self.pool) else None

        self.log.debug(result)

        return result

    ##########################################################################################

    def _register_application(self):
        """ Register host application to receive and handle packets """

        try:
            self.device.register_app()

        except Exception as e:
            self.log.error(e)

    ##########################################################################################

    def _set_listener(self, can_id=0):
        """ Enable CAN data indication forwarding for a specific CAN-ID

        Args:
            can_id (int, optional)   : CAN identificator

        """

        self.device.add_identifier(can_id)
        self.log.debug("Application registered to receive frames from 0x{}".format(can_id))

    ##########################################################################################

    def _clear_listener(self, can_id=0):
        """ Disable CAN data indication forwarding for a specific CAN-ID

        Args:
            can_id (int, optional)   : CAN identificator

        """

        self.device.remove_identifier(identifier=can_id)

        self.log.debug("Application unregistered to receive frames from 0x{0:X}".
                       format(can_id))

        self.device.enable_receive()

    def _handle_indication(self, device, indication):
        """ Callback on received CAN indications

        Args:
            device      (:obj:Device)   : device instance
            indication  (:obj:Packet)   : CAN frame indication packet

        """

        # Parse the CAN frame info from the CAN data indication
        rx_frame = indication.tData.atRxFrame[0]
        dlc, rtr, frame_format = device.parse_frame_info(rx_frame.ulFrameInfo)

        # Create the CAN frame data structure from the indication packet
        message = CanFrameBasic()
        message.can_id = rx_frame.ulIdentifier
        message.rtr = rtr
        message.data = rx_frame.abData[:dlc]

        # Save the CAN frame to the pool
        self.pool.append(message)

        # Prepare the response packet
        response = API_V2.CAN_DL_PACKET_DATA_RES_T()
        response.tHead.ulCmd = API_V2.CAN_DL_CMD_DATA_RES
        response.tHead.ulSrc = indication.tHead.ulSrc
        response.tHead.ulSrcId = indication.tHead.ulSrcId
        response.tHead.ulDest = RCX_PACKET_DEST_DEFAULT_CHANNEL
        response.tHead.ulLen = 0

        # Send the response packet
        device.send_packet(response)

    def flush(self):
        """ Clear the CAN frames pool """
        self.pool[:] = []
