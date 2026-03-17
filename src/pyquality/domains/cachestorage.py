class CacheStorageDomain:
    def __init__(self, driver):
        self.driver = driver

    def deleteCache(self, cacheId):
        """
        Deletes a cache.
        - cacheId (any): Id of cache for deletion.
        """
        params = {}
        params["cacheId"] = cacheId
        return self.driver.execute_and_wait("CacheStorage.deleteCache", params)

    def deleteEntry(self, cacheId, request):
        """
        Deletes a cache entry.
        - cacheId (any): Id of cache where the entry will be deleted.
        - request (string): URL spec of the request.
        """
        params = {}
        params["cacheId"] = cacheId
        params["request"] = request
        return self.driver.execute_and_wait("CacheStorage.deleteEntry", params)

    def requestCacheNames(self, securityOrigin=None, storageKey=None, storageBucket=None):
        """
        Requests cache names.
        - securityOrigin (string): At least and at most one of securityOrigin, storageKey, storageBucket must be specified.
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
        return self.driver.execute_and_wait("CacheStorage.requestCacheNames", params)

    def requestCachedResponse(self, cacheId, requestURL, requestHeaders):
        """
        Fetches cache entry.
        - cacheId (any): Id of cache that contains the entry.
        - requestURL (string): URL spec of the request.
        - requestHeaders (array): headers of the request.
        """
        params = {}
        params["cacheId"] = cacheId
        params["requestURL"] = requestURL
        params["requestHeaders"] = requestHeaders
        return self.driver.execute_and_wait("CacheStorage.requestCachedResponse", params)

    def requestEntries(self, cacheId, skipCount=None, pageSize=None, pathFilter=None):
        """
        Requests data from cache.
        - cacheId (any): ID of cache to get entries from.
        - skipCount (integer): Number of records to skip.
        - pageSize (integer): Number of records to fetch.
        - pathFilter (string): If present, only return the entries containing this substring in the path
        """
        params = {}
        params["cacheId"] = cacheId
        if skipCount is not None:
            params["skipCount"] = skipCount
        if pageSize is not None:
            params["pageSize"] = pageSize
        if pathFilter is not None:
            params["pathFilter"] = pathFilter
        return self.driver.execute_and_wait("CacheStorage.requestEntries", params)

