import CanNetworkSimulator
import time

num_id = int(0)

while True:
    today = time.strftime("%H:%M:%S", time.localtime())
    data = CanNetworkSimulator.readCANNetwork()

    time.sleep(0.3)

    num_id += 1
    name_module = data[0:2]
    function_module = data[2:5]
    value = data[5:]

    if name_module == "01":
        name_module = "Engine:"
        if function_module == "010":
            function_module = "Speed:"
        elif function_module == "020":
            function_module = "Gear indicator"

    if name_module == "46":
        name_module = "Comfort:"
        if function_module == "010":
            function_module = "Windows:"
        elif function_module == "100":
            function_module = "Mirrors:"

    if name_module == "03":
        name_module = "ABS:"
        if function_module == "001":
            function_module = "ABS:"
        elif function_module == "010":
            function_module = "ESP:"
        elif function_module == "100":
            function_module = "TC:"

    if name_module == "08":
        name_module = "HVAC:"
        if function_module == "001":
            function_module = "Temp:"
        elif function_module == "010":
            function_module = "Fan speed:"
        elif function_module == "100":
            function_module = "Zone:"

    if name_module == "16":
        name_module = "Steering:"
        if function_module == "001":
            function_module = "Rotation:"
        elif function_module == "010":
            function_module = "Mode:"

    if name_module == "37":
        name_module = "Navigation:"
        if function_module == "001":
            function_module = "Height level:"
        elif function_module == "010":
            function_module = "Latitude:"
        elif function_module == "020":
            function_module = "Longitude:"
        elif function_module == "100":
            function_module = "Number of satelites:"

    if name_module == "56":
        name_module = "Radio:"
        if function_module == "010":
            function_module = "Brand:"
        elif function_module == "050":
            function_module = "Current Frequency:"
        elif function_module == "100":
            function_module = "RDS:"

    if name_module == "35":
        name_module = "Central lock:"
        if function_module == "001":
            function_module = "Door lock status:"

    print(num_id, "|", today, "|", data, "|", name_module, "|", function_module, "|", value)




