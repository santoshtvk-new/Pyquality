class StorageDomain:
    def __init__(self, driver):
        self.driver = driver

    def getStorageKeyForFrame(self, frameId):
        """
        Returns a storage key given a frame id. Deprecated. Please use Storage.getStorageKey instead.
        - frameId (any): 
        """
        params = {}
        params["frameId"] = frameId
        return self.driver.execute_and_wait("Storage.getStorageKeyForFrame", params)

    def getStorageKey(self, frameId=None):
        """
        Returns storage key for the given frame. If no frame ID is provided, the storage key of the target executing this command is returned.
        - frameId (any): 
        """
        params = {}
        if frameId is not None:
            params["frameId"] = frameId
        return self.driver.execute_and_wait("Storage.getStorageKey", params)

    def clearDataForOrigin(self, origin, storageTypes):
        """
        Clears storage for origin.
        - origin (string): Security origin.
        - storageTypes (string): Comma separated list of StorageType to clear.
        """
        params = {}
        params["origin"] = origin
        params["storageTypes"] = storageTypes
        return self.driver.execute_and_wait("Storage.clearDataForOrigin", params)

    def clearDataForStorageKey(self, storageKey, storageTypes):
        """
        Clears storage for storage key.
        - storageKey (string): Storage key.
        - storageTypes (string): Comma separated list of StorageType to clear.
        """
        params = {}
        params["storageKey"] = storageKey
        params["storageTypes"] = storageTypes
        return self.driver.execute_and_wait("Storage.clearDataForStorageKey", params)

    def getCookies(self, browserContextId=None):
        """
        Returns all browser cookies.
        - browserContextId (any): Browser context to use when called on the browser endpoint.
        """
        params = {}
        if browserContextId is not None:
            params["browserContextId"] = browserContextId
        return self.driver.execute_and_wait("Storage.getCookies", params)

    def setCookies(self, cookies, browserContextId=None):
        """
        Sets given cookies.
        - cookies (array): Cookies to be set.
        - browserContextId (any): Browser context to use when called on the browser endpoint.
        """
        params = {}
        params["cookies"] = cookies
        if browserContextId is not None:
            params["browserContextId"] = browserContextId
        return self.driver.execute_and_wait("Storage.setCookies", params)

    def clearCookies(self, browserContextId=None):
        """
        Clears cookies.
        - browserContextId (any): Browser context to use when called on the browser endpoint.
        """
        params = {}
        if browserContextId is not None:
            params["browserContextId"] = browserContextId
        return self.driver.execute_and_wait("Storage.clearCookies", params)

    def getUsageAndQuota(self, origin):
        """
        Returns usage and quota in bytes.
        - origin (string): Security origin.
        """
        params = {}
        params["origin"] = origin
        return self.driver.execute_and_wait("Storage.getUsageAndQuota", params)

    def overrideQuotaForOrigin(self, origin, quotaSize=None):
        """
        Override quota for the specified origin
        - origin (string): Security origin.
        - quotaSize (number): The quota size (in bytes) to override the original quota with.
If this is called multiple times, the overridden quota will be equal to
the quotaSize provided in the final call. If this is called without
specifying a quotaSize, the quota will be reset to the default value for
the specified origin. If this is called multiple times with different
origins, the override will be maintained for each origin until it is
disabled (called without a quotaSize).
        """
        params = {}
        params["origin"] = origin
        if quotaSize is not None:
            params["quotaSize"] = quotaSize
        return self.driver.execute_and_wait("Storage.overrideQuotaForOrigin", params)

    def trackCacheStorageForOrigin(self, origin):
        """
        Registers origin to be notified when an update occurs to its cache storage list.
        - origin (string): Security origin.
        """
        params = {}
        params["origin"] = origin
        return self.driver.execute_and_wait("Storage.trackCacheStorageForOrigin", params)

    def trackCacheStorageForStorageKey(self, storageKey):
        """
        Registers storage key to be notified when an update occurs to its cache storage list.
        - storageKey (string): Storage key.
        """
        params = {}
        params["storageKey"] = storageKey
        return self.driver.execute_and_wait("Storage.trackCacheStorageForStorageKey", params)

    def trackIndexedDBForOrigin(self, origin):
        """
        Registers origin to be notified when an update occurs to its IndexedDB.
        - origin (string): Security origin.
        """
        params = {}
        params["origin"] = origin
        return self.driver.execute_and_wait("Storage.trackIndexedDBForOrigin", params)

    def trackIndexedDBForStorageKey(self, storageKey):
        """
        Registers storage key to be notified when an update occurs to its IndexedDB.
        - storageKey (string): Storage key.
        """
        params = {}
        params["storageKey"] = storageKey
        return self.driver.execute_and_wait("Storage.trackIndexedDBForStorageKey", params)

    def untrackCacheStorageForOrigin(self, origin):
        """
        Unregisters origin from receiving notifications for cache storage.
        - origin (string): Security origin.
        """
        params = {}
        params["origin"] = origin
        return self.driver.execute_and_wait("Storage.untrackCacheStorageForOrigin", params)

    def untrackCacheStorageForStorageKey(self, storageKey):
        """
        Unregisters storage key from receiving notifications for cache storage.
        - storageKey (string): Storage key.
        """
        params = {}
        params["storageKey"] = storageKey
        return self.driver.execute_and_wait("Storage.untrackCacheStorageForStorageKey", params)

    def untrackIndexedDBForOrigin(self, origin):
        """
        Unregisters origin from receiving notifications for IndexedDB.
        - origin (string): Security origin.
        """
        params = {}
        params["origin"] = origin
        return self.driver.execute_and_wait("Storage.untrackIndexedDBForOrigin", params)

    def untrackIndexedDBForStorageKey(self, storageKey):
        """
        Unregisters storage key from receiving notifications for IndexedDB.
        - storageKey (string): Storage key.
        """
        params = {}
        params["storageKey"] = storageKey
        return self.driver.execute_and_wait("Storage.untrackIndexedDBForStorageKey", params)

    def getTrustTokens(self):
        """
        Returns the number of stored Trust Tokens per issuer for the current browsing context.
        """
        params = {}
        return self.driver.execute_and_wait("Storage.getTrustTokens", params)

    def clearTrustTokens(self, issuerOrigin):
        """
        Removes all Trust Tokens issued by the provided issuerOrigin. Leaves other stored data, including the issuer's Redemption Records, intact.
        - issuerOrigin (string): 
        """
        params = {}
        params["issuerOrigin"] = issuerOrigin
        return self.driver.execute_and_wait("Storage.clearTrustTokens", params)

    def getInterestGroupDetails(self, ownerOrigin, name):
        """
        Gets details for a named interest group.
        - ownerOrigin (string): 
        - name (string): 
        """
        params = {}
        params["ownerOrigin"] = ownerOrigin
        params["name"] = name
        return self.driver.execute_and_wait("Storage.getInterestGroupDetails", params)

    def setInterestGroupTracking(self, enable):
        """
        Enables/Disables issuing of interestGroupAccessed events.
        - enable (boolean): 
        """
        params = {}
        params["enable"] = enable
        return self.driver.execute_and_wait("Storage.setInterestGroupTracking", params)

    def setInterestGroupAuctionTracking(self, enable):
        """
        Enables/Disables issuing of interestGroupAuctionEventOccurred and interestGroupAuctionNetworkRequestCreated.
        - enable (boolean): 
        """
        params = {}
        params["enable"] = enable
        return self.driver.execute_and_wait("Storage.setInterestGroupAuctionTracking", params)

    def getSharedStorageMetadata(self, ownerOrigin):
        """
        Gets metadata for an origin's shared storage.
        - ownerOrigin (string): 
        """
        params = {}
        params["ownerOrigin"] = ownerOrigin
        return self.driver.execute_and_wait("Storage.getSharedStorageMetadata", params)

    def getSharedStorageEntries(self, ownerOrigin):
        """
        Gets the entries in an given origin's shared storage.
        - ownerOrigin (string): 
        """
        params = {}
        params["ownerOrigin"] = ownerOrigin
        return self.driver.execute_and_wait("Storage.getSharedStorageEntries", params)

    def setSharedStorageEntry(self, ownerOrigin, key, value, ignoreIfPresent=None):
        """
        Sets entry with `key` and `value` for a given origin's shared storage.
        - ownerOrigin (string): 
        - key (string): 
        - value (string): 
        - ignoreIfPresent (boolean): If `ignoreIfPresent` is included and true, then only sets the entry if
`key` doesn't already exist.
        """
        params = {}
        params["ownerOrigin"] = ownerOrigin
        params["key"] = key
        params["value"] = value
        if ignoreIfPresent is not None:
            params["ignoreIfPresent"] = ignoreIfPresent
        return self.driver.execute_and_wait("Storage.setSharedStorageEntry", params)

    def deleteSharedStorageEntry(self, ownerOrigin, key):
        """
        Deletes entry for `key` (if it exists) for a given origin's shared storage.
        - ownerOrigin (string): 
        - key (string): 
        """
        params = {}
        params["ownerOrigin"] = ownerOrigin
        params["key"] = key
        return self.driver.execute_and_wait("Storage.deleteSharedStorageEntry", params)

    def clearSharedStorageEntries(self, ownerOrigin):
        """
        Clears all entries for a given origin's shared storage.
        - ownerOrigin (string): 
        """
        params = {}
        params["ownerOrigin"] = ownerOrigin
        return self.driver.execute_and_wait("Storage.clearSharedStorageEntries", params)

    def resetSharedStorageBudget(self, ownerOrigin):
        """
        Resets the budget for `ownerOrigin` by clearing all budget withdrawals.
        - ownerOrigin (string): 
        """
        params = {}
        params["ownerOrigin"] = ownerOrigin
        return self.driver.execute_and_wait("Storage.resetSharedStorageBudget", params)

    def setSharedStorageTracking(self, enable):
        """
        Enables/disables issuing of sharedStorageAccessed events.
        - enable (boolean): 
        """
        params = {}
        params["enable"] = enable
        return self.driver.execute_and_wait("Storage.setSharedStorageTracking", params)

    def setStorageBucketTracking(self, storageKey, enable):
        """
        Set tracking for a storage key's buckets.
        - storageKey (string): 
        - enable (boolean): 
        """
        params = {}
        params["storageKey"] = storageKey
        params["enable"] = enable
        return self.driver.execute_and_wait("Storage.setStorageBucketTracking", params)

    def deleteStorageBucket(self, bucket):
        """
        Deletes the Storage Bucket with the given storage key and bucket name.
        - bucket (any): 
        """
        params = {}
        params["bucket"] = bucket
        return self.driver.execute_and_wait("Storage.deleteStorageBucket", params)

    def runBounceTrackingMitigations(self):
        """
        Deletes state for sites identified as potential bounce trackers, immediately.
        """
        params = {}
        return self.driver.execute_and_wait("Storage.runBounceTrackingMitigations", params)

    def setAttributionReportingLocalTestingMode(self, enabled):
        """
        https://wicg.github.io/attribution-reporting-api/
        - enabled (boolean): If enabled, noise is suppressed and reports are sent immediately.
        """
        params = {}
        params["enabled"] = enabled
        return self.driver.execute_and_wait("Storage.setAttributionReportingLocalTestingMode", params)

    def setAttributionReportingTracking(self, enable):
        """
        Enables/disables issuing of Attribution Reporting events.
        - enable (boolean): 
        """
        params = {}
        params["enable"] = enable
        return self.driver.execute_and_wait("Storage.setAttributionReportingTracking", params)

    def sendPendingAttributionReports(self):
        """
        Sends all pending Attribution Reports immediately, regardless of their scheduled report time.
        """
        params = {}
        return self.driver.execute_and_wait("Storage.sendPendingAttributionReports", params)

    def getRelatedWebsiteSets(self):
        """
        Returns the effective Related Website Sets in use by this profile for the browser session. The effective Related Website Sets will not change during a browser session.
        """
        params = {}
        return self.driver.execute_and_wait("Storage.getRelatedWebsiteSets", params)

    def getAffectedUrlsForThirdPartyCookieMetadata(self, firstPartyUrl, thirdPartyUrls):
        """
        Returns the list of URLs from a page and its embedded resources that match existing grace period URL pattern rules. https://developers.google.com/privacy-sandbox/cookies/temporary-exceptions/grace-period
        - firstPartyUrl (string): The URL of the page currently being visited.
        - thirdPartyUrls (array): The list of embedded resource URLs from the page.
        """
        params = {}
        params["firstPartyUrl"] = firstPartyUrl
        params["thirdPartyUrls"] = thirdPartyUrls
        return self.driver.execute_and_wait("Storage.getAffectedUrlsForThirdPartyCookieMetadata", params)

    def setProtectedAudienceKAnonymity(self, owner, name, hashes):
        """
        Call Storage.setProtectedAudienceKAnonymity
        - owner (string): 
        - name (string): 
        - hashes (array): 
        """
        params = {}
        params["owner"] = owner
        params["name"] = name
        params["hashes"] = hashes
        return self.driver.execute_and_wait("Storage.setProtectedAudienceKAnonymity", params)

