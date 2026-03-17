class IndexedDBDomain:
    def __init__(self, driver):
        self.driver = driver

    def clearObjectStore(self, databaseName, objectStoreName, securityOrigin=None, storageKey=None, storageBucket=None):
        """
        Clears all entries from an object store.
        - securityOrigin (string): At least and at most one of securityOrigin, storageKey, or storageBucket must be specified.
Security origin.
        - storageKey (string): Storage key.
        - storageBucket (any): Storage bucket. If not specified, it uses the default bucket.
        - databaseName (string): Database name.
        - objectStoreName (string): Object store name.
        """
        params = {}
        if securityOrigin is not None:
            params["securityOrigin"] = securityOrigin
        if storageKey is not None:
            params["storageKey"] = storageKey
        if storageBucket is not None:
            params["storageBucket"] = storageBucket
        params["databaseName"] = databaseName
        params["objectStoreName"] = objectStoreName
        return self.driver.execute_and_wait("IndexedDB.clearObjectStore", params)

    def deleteDatabase(self, databaseName, securityOrigin=None, storageKey=None, storageBucket=None):
        """
        Deletes a database.
        - securityOrigin (string): At least and at most one of securityOrigin, storageKey, or storageBucket must be specified.
Security origin.
        - storageKey (string): Storage key.
        - storageBucket (any): Storage bucket. If not specified, it uses the default bucket.
        - databaseName (string): Database name.
        """
        params = {}
        if securityOrigin is not None:
            params["securityOrigin"] = securityOrigin
        if storageKey is not None:
            params["storageKey"] = storageKey
        if storageBucket is not None:
            params["storageBucket"] = storageBucket
        params["databaseName"] = databaseName
        return self.driver.execute_and_wait("IndexedDB.deleteDatabase", params)

    def deleteObjectStoreEntries(self, databaseName, objectStoreName, keyRange, securityOrigin=None, storageKey=None, storageBucket=None):
        """
        Delete a range of entries from an object store
        - securityOrigin (string): At least and at most one of securityOrigin, storageKey, or storageBucket must be specified.
Security origin.
        - storageKey (string): Storage key.
        - storageBucket (any): Storage bucket. If not specified, it uses the default bucket.
        - databaseName (string): 
        - objectStoreName (string): 
        - keyRange (any): Range of entry keys to delete
        """
        params = {}
        if securityOrigin is not None:
            params["securityOrigin"] = securityOrigin
        if storageKey is not None:
            params["storageKey"] = storageKey
        if storageBucket is not None:
            params["storageBucket"] = storageBucket
        params["databaseName"] = databaseName
        params["objectStoreName"] = objectStoreName
        params["keyRange"] = keyRange
        return self.driver.execute_and_wait("IndexedDB.deleteObjectStoreEntries", params)

    def disable(self):
        """
        Disables events from backend.
        """
        params = {}
        return self.driver.execute_and_wait("IndexedDB.disable", params)

    def enable(self):
        """
        Enables events from backend.
        """
        params = {}
        return self.driver.execute_and_wait("IndexedDB.enable", params)

    def requestData(self, databaseName, objectStoreName, skipCount, pageSize, securityOrigin=None, storageKey=None, storageBucket=None, indexName=None, keyRange=None):
        """
        Requests data from object store or index.
        - securityOrigin (string): At least and at most one of securityOrigin, storageKey, or storageBucket must be specified.
Security origin.
        - storageKey (string): Storage key.
        - storageBucket (any): Storage bucket. If not specified, it uses the default bucket.
        - databaseName (string): Database name.
        - objectStoreName (string): Object store name.
        - indexName (string): Index name. If not specified, it performs an object store data request.
        - skipCount (integer): Number of records to skip.
        - pageSize (integer): Number of records to fetch.
        - keyRange (any): Key range.
        """
        params = {}
        if securityOrigin is not None:
            params["securityOrigin"] = securityOrigin
        if storageKey is not None:
            params["storageKey"] = storageKey
        if storageBucket is not None:
            params["storageBucket"] = storageBucket
        params["databaseName"] = databaseName
        params["objectStoreName"] = objectStoreName
        if indexName is not None:
            params["indexName"] = indexName
        params["skipCount"] = skipCount
        params["pageSize"] = pageSize
        if keyRange is not None:
            params["keyRange"] = keyRange
        return self.driver.execute_and_wait("IndexedDB.requestData", params)

    def getMetadata(self, databaseName, objectStoreName, securityOrigin=None, storageKey=None, storageBucket=None):
        """
        Gets metadata of an object store.
        - securityOrigin (string): At least and at most one of securityOrigin, storageKey, or storageBucket must be specified.
Security origin.
        - storageKey (string): Storage key.
        - storageBucket (any): Storage bucket. If not specified, it uses the default bucket.
        - databaseName (string): Database name.
        - objectStoreName (string): Object store name.
        """
        params = {}
        if securityOrigin is not None:
            params["securityOrigin"] = securityOrigin
        if storageKey is not None:
            params["storageKey"] = storageKey
        if storageBucket is not None:
            params["storageBucket"] = storageBucket
        params["databaseName"] = databaseName
        params["objectStoreName"] = objectStoreName
        return self.driver.execute_and_wait("IndexedDB.getMetadata", params)

    def requestDatabase(self, databaseName, securityOrigin=None, storageKey=None, storageBucket=None):
        """
        Requests database with given name in given frame.
        - securityOrigin (string): At least and at most one of securityOrigin, storageKey, or storageBucket must be specified.
Security origin.
        - storageKey (string): Storage key.
        - storageBucket (any): Storage bucket. If not specified, it uses the default bucket.
        - databaseName (string): Database name.
        """
        params = {}
        if securityOrigin is not None:
            params["securityOrigin"] = securityOrigin
        if storageKey is not None:
            params["storageKey"] = storageKey
        if storageBucket is not None:
            params["storageBucket"] = storageBucket
        params["databaseName"] = databaseName
        return self.driver.execute_and_wait("IndexedDB.requestDatabase", params)

    def requestDatabaseNames(self, securityOrigin=None, storageKey=None, storageBucket=None):
        """
        Requests database names for given security origin.
        - securityOrigin (string): At least and at most one of securityOrigin, storageKey, or storageBucket must be specified.
Security origin.
        - storageKey (string): Storage key.
        - storageBucket (any): Storage bucket. If not specified, it uses the default bucket.
        """
        params = {}
        if securityOrigin is not None:
            params["securityOrigin"] = securityOrigin
        if storageKey is not None:
            params["storageKey"] = storageKey
        if storageBucket is not None:
            params["storageBucket"] = storageBucket
        return self.driver.execute_and_wait("IndexedDB.requestDatabaseNames", params)

