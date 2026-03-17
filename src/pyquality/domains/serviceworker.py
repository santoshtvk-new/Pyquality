class ServiceWorkerDomain:
    def __init__(self, driver):
        self.driver = driver

    def deliverPushMessage(self, origin, registrationId, data):
        """
        Call ServiceWorker.deliverPushMessage
        - origin (string): 
        - registrationId (any): 
        - data (string): 
        """
        params = {}
        params["origin"] = origin
        params["registrationId"] = registrationId
        params["data"] = data
        return self.driver.execute_and_wait("ServiceWorker.deliverPushMessage", params)

    def disable(self):
        """
        Call ServiceWorker.disable
        """
        params = {}
        return self.driver.execute_and_wait("ServiceWorker.disable", params)

    def dispatchSyncEvent(self, origin, registrationId, tag, lastChance):
        """
        Call ServiceWorker.dispatchSyncEvent
        - origin (string): 
        - registrationId (any): 
        - tag (string): 
        - lastChance (boolean): 
        """
        params = {}
        params["origin"] = origin
        params["registrationId"] = registrationId
        params["tag"] = tag
        params["lastChance"] = lastChance
        return self.driver.execute_and_wait("ServiceWorker.dispatchSyncEvent", params)

    def dispatchPeriodicSyncEvent(self, origin, registrationId, tag):
        """
        Call ServiceWorker.dispatchPeriodicSyncEvent
        - origin (string): 
        - registrationId (any): 
        - tag (string): 
        """
        params = {}
        params["origin"] = origin
        params["registrationId"] = registrationId
        params["tag"] = tag
        return self.driver.execute_and_wait("ServiceWorker.dispatchPeriodicSyncEvent", params)

    def enable(self):
        """
        Call ServiceWorker.enable
        """
        params = {}
        return self.driver.execute_and_wait("ServiceWorker.enable", params)

    def setForceUpdateOnPageLoad(self, forceUpdateOnPageLoad):
        """
        Call ServiceWorker.setForceUpdateOnPageLoad
        - forceUpdateOnPageLoad (boolean): 
        """
        params = {}
        params["forceUpdateOnPageLoad"] = forceUpdateOnPageLoad
        return self.driver.execute_and_wait("ServiceWorker.setForceUpdateOnPageLoad", params)

    def skipWaiting(self, scopeURL):
        """
        Call ServiceWorker.skipWaiting
        - scopeURL (string): 
        """
        params = {}
        params["scopeURL"] = scopeURL
        return self.driver.execute_and_wait("ServiceWorker.skipWaiting", params)

    def startWorker(self, scopeURL):
        """
        Call ServiceWorker.startWorker
        - scopeURL (string): 
        """
        params = {}
        params["scopeURL"] = scopeURL
        return self.driver.execute_and_wait("ServiceWorker.startWorker", params)

    def stopAllWorkers(self):
        """
        Call ServiceWorker.stopAllWorkers
        """
        params = {}
        return self.driver.execute_and_wait("ServiceWorker.stopAllWorkers", params)

    def stopWorker(self, versionId):
        """
        Call ServiceWorker.stopWorker
        - versionId (string): 
        """
        params = {}
        params["versionId"] = versionId
        return self.driver.execute_and_wait("ServiceWorker.stopWorker", params)

    def unregister(self, scopeURL):
        """
        Call ServiceWorker.unregister
        - scopeURL (string): 
        """
        params = {}
        params["scopeURL"] = scopeURL
        return self.driver.execute_and_wait("ServiceWorker.unregister", params)

    def updateRegistration(self, scopeURL):
        """
        Call ServiceWorker.updateRegistration
        - scopeURL (string): 
        """
        params = {}
        params["scopeURL"] = scopeURL
        return self.driver.execute_and_wait("ServiceWorker.updateRegistration", params)

