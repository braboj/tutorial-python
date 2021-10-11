from scapy.arch.windows import get_windows_if_list

adapters = get_windows_if_list(extended=False)

for element in adapters:
    print(element)