class ExtensionsDomain:
    def __init__(self, driver):
        self.driver = driver

    def triggerAction(self, id_, targetId):
        """
        Runs an extension default action. Available if the client is connected using the --remote-debugging-pipe flag and the --enable-unsafe-extension-debugging flag is set.
        - id (string): Extension id.
        - targetId (string): A tab target ID to trigger the default extension action on.
        """
        params = {}
        params["id"] = id_
        params["targetId"] = targetId
        return self.driver.execute_and_wait("Extensions.triggerAction", params)

    def loadUnpacked(self, path, enableInIncognito=None):
        """
        Installs an unpacked extension from the filesystem similar to --load-extension CLI flags. Returns extension ID once the extension has been installed. Available if the client is connected using the --remote-debugging-pipe flag and the --enable-unsafe-extension-debugging flag is set.
        - path (string): Absolute file path.
        - enableInIncognito (boolean): Enable the extension in incognito
        """
        params = {}
        params["path"] = path
        if enableInIncognito is not None:
            params["enableInIncognito"] = enableInIncognito
        return self.driver.execute_and_wait("Extensions.loadUnpacked", params)

    def getExtensions(self):
        """
        Gets a list of all unpacked extensions. Available if the client is connected using the --remote-debugging-pipe flag and the --enable-unsafe-extension-debugging flag is set.
        """
        params = {}
        return self.driver.execute_and_wait("Extensions.getExtensions", params)

    def uninstall(self, id_):
        """
        Uninstalls an unpacked extension (others not supported) from the profile. Available if the client is connected using the --remote-debugging-pipe flag and the --enable-unsafe-extension-debugging.
        - id (string): Extension id.
        """
        params = {}
        params["id"] = id_
        return self.driver.execute_and_wait("Extensions.uninstall", params)

    def getStorageItems(self, id_, storageArea, keys=None):
        """
        Gets data from extension storage in the given `storageArea`. If `keys` is specified, these are used to filter the result.
        - id (string): ID of extension.
        - storageArea (any): StorageArea to retrieve data from.
        - keys (array): Keys to retrieve.
        """
        params = {}
        params["id"] = id_
        params["storageArea"] = storageArea
        if keys is not None:
            params["keys"] = keys
        return self.driver.execute_and_wait("Extensions.getStorageItems", params)

    def removeStorageItems(self, id_, storageArea, keys):
        """
        Removes `keys` from extension storage in the given `storageArea`.
        - id (string): ID of extension.
        - storageArea (any): StorageArea to remove data from.
        - keys (array): Keys to remove.
        """
        params = {}
        params["id"] = id_
        params["storageArea"] = storageArea
        params["keys"] = keys
        return self.driver.execute_and_wait("Extensions.removeStorageItems", params)

    def clearStorageItems(self, id_, storageArea):
        """
        Clears extension storage in the given `storageArea`.
        - id (string): ID of extension.
        - storageArea (any): StorageArea to remove data from.
        """
        params = {}
        params["id"] = id_
        params["storageArea"] = storageArea
        return self.driver.execute_and_wait("Extensions.clearStorageItems", params)

    def setStorageItems(self, id_, storageArea, values):
        """
        Sets `values` in extension storage in the given `storageArea`. The provided `values` will be merged with existing values in the storage area.
        - id (string): ID of extension.
        - storageArea (any): StorageArea to set data in.
        - values (object): Values to set.
        """
        params = {}
        params["id"] = id_
        params["storageArea"] = storageArea
        params["values"] = values
        return self.driver.execute_and_wait("Extensions.setStorageItems", params)

