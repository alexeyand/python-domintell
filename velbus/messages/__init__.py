"""
:author: Thomas Delaet <thomas@delaet.org>
"""
# pylint: disable-msg=C0301
from velbus.messages.bus_active import BusActiveMessage
from velbus.messages.bus_error_counter_status_request import BusErrorStatusRequestMessage
from velbus.messages.bus_error_counter_status import BusErrorCounterStatusMessage
from velbus.messages.bus_off import BusOffMessage
from velbus.messages.channel_name_part1 import ChannelNamePart1Message
from velbus.messages.channel_name_part2 import ChannelNamePart2Message
from velbus.messages.channel_name_part3 import ChannelNamePart3Message
from velbus.messages.channel_name_request import ChannelNameRequestMessage
from velbus.messages.clear_led import ClearLedMessage
from velbus.messages.fast_blinking_led import FastBlinkingLedMessage
from velbus.messages.interface_status_request import InterfaceStatusRequestMessage
from velbus.messages.memory_data_block import MemoryDataBlockMessage
from velbus.messages.memory_data import MemoryDataMessage
from velbus.messages.memory_dump_request import MemoryDumpRequestMessage
from velbus.messages.module_status_request import ModuleStatusRequestMessage
from velbus.messages.module_status import ModuleStatusMessage
from velbus.messages.module_type import ModuleTypeMessage
from velbus.messages.module_type_request import ModuleTypeRequestMessage
from velbus.messages.push_button_status import PushButtonStatusMessage
from velbus.messages.read_data_block_from_memory import ReadDataBlockFromMemoryMessage
from velbus.messages.read_data_from_memory import ReadDataFromMemoryMessage
from velbus.messages.receive_buffer_full import ReceiveBufferFullMessage
from velbus.messages.receive_ready import ReceiveReadyMessage
from velbus.messages.relay_status import RelayStatusMessage
from velbus.messages.set_led import SetLedMessage
from velbus.messages.slow_blinking_led import SlowBlinkingLedMessage
from velbus.messages.start_relay_blinking_timer import StartRelayBlinkingTimerMessage
from velbus.messages.start_relay_timer import StartRelayTimerMessage
from velbus.messages.switch_relay_off import SwitchRelayOffMessage
from velbus.messages.switch_relay_on import SwitchRelayOnMessage
from velbus.messages.update_led_status import UpdateLedStatusMessage
from velbus.messages.very_fast_blinking_led import VeryFastBlinkingLedMessage
from velbus.messages.write_data_to_memory import WriteDataToMemoryMessage
from velbus.messages.write_memory_block import WriteMemoryBlockMessage
from velbus.messages.write_module_address_and_serial_number import WriteModuleAddressAndSerialNumberMessage
from velbus.messages.cover_down import CoverDownMessage
from velbus.messages.cover_up import CoverUpMessage
from velbus.messages.blind_status import BlindStatusMessage
from velbus.messages.sensor_temperature import SensorTemperatureMessage
from velbus.messages.kwh_status import KwhStatusMessage
from velbus.messages.temp_sensor_status import TempSensorStatusMessage
from velbus.messages.temp_set_heating import TempSetHeatingMessage
from velbus.messages.temp_set_cooling import TempSetCoolingMessage
