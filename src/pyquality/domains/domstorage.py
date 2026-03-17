class DOMStorageDomain:
    def __init__(self, driver):
        self.driver = driver

    def clear(self, storageId):
        """
        Call DOMStorage.clear
        - storageId (any): 
        """
        params = {}
        params["storageId"] = storageId
        return self.driver.execute_and_wait("DOMStorage.clear", params)

    def disable(self):
        """
        Disables storage tracking, prevents storage events from being sent to the client.
        """
        params = {}
        return self.driver.execute_and_wait("DOMStorage.disable", params)

    def enable(self):
        """
        Enables storage tracking, storage events will now be delivered to the client.
        """
        params = {}
        return self.driver.execute_and_wait("DOMStorage.enable", params)

    def getDOMStorageItems(self, storageId):
        """
        Call DOMStorage.getDOMStorageItems
        - storageId (any): 
        """
        params = {}
        params["storageId"] = storageId
        return self.driver.execute_and_wait("DOMStorage.getDOMStorageItems", params)

    def removeDOMStorageItem(self, storageId, key):
        """
        Call DOMStorage.removeDOMStorageItem
        - storageId (any): 
        - key (string): 
        """
        params = {}
        params["storageId"] = storageId
        params["key"] = key
        return self.driver.execute_and_wait("DOMStorage.removeDOMStorageItem", params)

    def setDOMStorageItem(self, storageId, key, value):
        """
        Call DOMStorage.setDOMStorageItem
        - storageId (any): 
        - key (string): 
        - value (string): 
        """
        params = {}
        params["storageId"] = storageId
        params["key"] = key
        params["value"] = value
        return self.driver.execute_and_wait("DOMStorage.setDOMStorageItem", params)

