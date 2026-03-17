class BluetoothEmulationDomain:
    def __init__(self, driver):
        self.driver = driver

    def enable(self, state, leSupported):
        """
        Enable the BluetoothEmulation domain.
        - state (any): State of the simulated central.
        - leSupported (boolean): If the simulated central supports low-energy.
        """
        params = {}
        params["state"] = state
        params["leSupported"] = leSupported
        return self.driver.execute_and_wait("BluetoothEmulation.enable", params)

    def setSimulatedCentralState(self, state):
        """
        Set the state of the simulated central.
        - state (any): State of the simulated central.
        """
        params = {}
        params["state"] = state
        return self.driver.execute_and_wait("BluetoothEmulation.setSimulatedCentralState", params)

    def disable(self):
        """
        Disable the BluetoothEmulation domain.
        """
        params = {}
        return self.driver.execute_and_wait("BluetoothEmulation.disable", params)

    def simulatePreconnectedPeripheral(self, address, name, manufacturerData, knownServiceUuids):
        """
        Simulates a peripheral with |address|, |name| and |knownServiceUuids| that has already been connected to the system.
        - address (string): 
        - name (string): 
        - manufacturerData (array): 
        - knownServiceUuids (array): 
        """
        params = {}
        params["address"] = address
        params["name"] = name
        params["manufacturerData"] = manufacturerData
        params["knownServiceUuids"] = knownServiceUuids
        return self.driver.execute_and_wait("BluetoothEmulation.simulatePreconnectedPeripheral", params)

    def simulateAdvertisement(self, entry):
        """
        Simulates an advertisement packet described in |entry| being received by the central.
        - entry (any): 
        """
        params = {}
        params["entry"] = entry
        return self.driver.execute_and_wait("BluetoothEmulation.simulateAdvertisement", params)

    def simulateGATTOperationResponse(self, address, type_, code):
        """
        Simulates the response code from the peripheral with |address| for a GATT operation of |type|. The |code| value follows the HCI Error Codes from Bluetooth Core Specification Vol 2 Part D 1.3 List Of Error Codes.
        - address (string): 
        - type (any): 
        - code (integer): 
        """
        params = {}
        params["address"] = address
        params["type"] = type_
        params["code"] = code
        return self.driver.execute_and_wait("BluetoothEmulation.simulateGATTOperationResponse", params)

    def simulateCharacteristicOperationResponse(self, characteristicId, type_, code, data=None):
        """
        Simulates the response from the characteristic with |characteristicId| for a characteristic operation of |type|. The |code| value follows the Error Codes from Bluetooth Core Specification Vol 3 Part F 3.4.1.1 Error Response. The |data| is expected to exist when simulating a successful read operation response.
        - characteristicId (string): 
        - type (any): 
        - code (integer): 
        - data (string): 
        """
        params = {}
        params["characteristicId"] = characteristicId
        params["type"] = type_
        params["code"] = code
        if data is not None:
            params["data"] = data
        return self.driver.execute_and_wait("BluetoothEmulation.simulateCharacteristicOperationResponse", params)

    def simulateDescriptorOperationResponse(self, descriptorId, type_, code, data=None):
        """
        Simulates the response from the descriptor with |descriptorId| for a descriptor operation of |type|. The |code| value follows the Error Codes from Bluetooth Core Specification Vol 3 Part F 3.4.1.1 Error Response. The |data| is expected to exist when simulating a successful read operation response.
        - descriptorId (string): 
        - type (any): 
        - code (integer): 
        - data (string): 
        """
        params = {}
        params["descriptorId"] = descriptorId
        params["type"] = type_
        params["code"] = code
        if data is not None:
            params["data"] = data
        return self.driver.execute_and_wait("BluetoothEmulation.simulateDescriptorOperationResponse", params)

    def addService(self, address, serviceUuid):
        """
        Adds a service with |serviceUuid| to the peripheral with |address|.
        - address (string): 
        - serviceUuid (string): 
        """
        params = {}
        params["address"] = address
        params["serviceUuid"] = serviceUuid
        return self.driver.execute_and_wait("BluetoothEmulation.addService", params)

    def removeService(self, serviceId):
        """
        Removes the service respresented by |serviceId| from the simulated central.
        - serviceId (string): 
        """
        params = {}
        params["serviceId"] = serviceId
        return self.driver.execute_and_wait("BluetoothEmulation.removeService", params)

    def addCharacteristic(self, serviceId, characteristicUuid, properties):
        """
        Adds a characteristic with |characteristicUuid| and |properties| to the service represented by |serviceId|.
        - serviceId (string): 
        - characteristicUuid (string): 
        - properties (any): 
        """
        params = {}
        params["serviceId"] = serviceId
        params["characteristicUuid"] = characteristicUuid
        params["properties"] = properties
        return self.driver.execute_and_wait("BluetoothEmulation.addCharacteristic", params)

    def removeCharacteristic(self, characteristicId):
        """
        Removes the characteristic respresented by |characteristicId| from the simulated central.
        - characteristicId (string): 
        """
        params = {}
        params["characteristicId"] = characteristicId
        return self.driver.execute_and_wait("BluetoothEmulation.removeCharacteristic", params)

    def addDescriptor(self, characteristicId, descriptorUuid):
        """
        Adds a descriptor with |descriptorUuid| to the characteristic respresented by |characteristicId|.
        - characteristicId (string): 
        - descriptorUuid (string): 
        """
        params = {}
        params["characteristicId"] = characteristicId
        params["descriptorUuid"] = descriptorUuid
        return self.driver.execute_and_wait("BluetoothEmulation.addDescriptor", params)

    def removeDescriptor(self, descriptorId):
        """
        Removes the descriptor with |descriptorId| from the simulated central.
        - descriptorId (string): 
        """
        params = {}
        params["descriptorId"] = descriptorId
        return self.driver.execute_and_wait("BluetoothEmulation.removeDescriptor", params)

    def simulateGATTDisconnection(self, address):
        """
        Simulates a GATT disconnection from the peripheral with |address|.
        - address (string): 
        """
        params = {}
        params["address"] = address
        return self.driver.execute_and_wait("BluetoothEmulation.simulateGATTDisconnection", params)

