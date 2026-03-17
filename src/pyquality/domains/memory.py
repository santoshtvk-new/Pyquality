class MemoryDomain:
    def __init__(self, driver):
        self.driver = driver

    def getDOMCounters(self):
        """
        Retruns current DOM object counters.
        """
        params = {}
        return self.driver.execute_and_wait("Memory.getDOMCounters", params)

    def getDOMCountersForLeakDetection(self):
        """
        Retruns DOM object counters after preparing renderer for leak detection.
        """
        params = {}
        return self.driver.execute_and_wait("Memory.getDOMCountersForLeakDetection", params)

    def prepareForLeakDetection(self):
        """
        Prepares for leak detection by terminating workers, stopping spellcheckers, dropping non-essential internal caches, running garbage collections, etc.
        """
        params = {}
        return self.driver.execute_and_wait("Memory.prepareForLeakDetection", params)

    def forciblyPurgeJavaScriptMemory(self):
        """
        Simulate OomIntervention by purging V8 memory.
        """
        params = {}
        return self.driver.execute_and_wait("Memory.forciblyPurgeJavaScriptMemory", params)

    def setPressureNotificationsSuppressed(self, suppressed):
        """
        Enable/disable suppressing memory pressure notifications in all processes.
        - suppressed (boolean): If true, memory pressure notifications will be suppressed.
        """
        params = {}
        params["suppressed"] = suppressed
        return self.driver.execute_and_wait("Memory.setPressureNotificationsSuppressed", params)

    def simulatePressureNotification(self, level):
        """
        Simulate a memory pressure notification in all processes.
        - level (any): Memory pressure level of the notification.
        """
        params = {}
        params["level"] = level
        return self.driver.execute_and_wait("Memory.simulatePressureNotification", params)

    def startSampling(self, samplingInterval=None, suppressRandomness=None):
        """
        Start collecting native memory profile.
        - samplingInterval (integer): Average number of bytes between samples.
        - suppressRandomness (boolean): Do not randomize intervals between samples.
        """
        params = {}
        if samplingInterval is not None:
            params["samplingInterval"] = samplingInterval
        if suppressRandomness is not None:
            params["suppressRandomness"] = suppressRandomness
        return self.driver.execute_and_wait("Memory.startSampling", params)

    def stopSampling(self):
        """
        Stop collecting native memory profile.
        """
        params = {}
        return self.driver.execute_and_wait("Memory.stopSampling", params)

    def getAllTimeSamplingProfile(self):
        """
        Retrieve native memory allocations profile collected since renderer process startup.
        """
        params = {}
        return self.driver.execute_and_wait("Memory.getAllTimeSamplingProfile", params)

    def getBrowserSamplingProfile(self):
        """
        Retrieve native memory allocations profile collected since browser process startup.
        """
        params = {}
        return self.driver.execute_and_wait("Memory.getBrowserSamplingProfile", params)

    def getSamplingProfile(self):
        """
        Retrieve native memory allocations profile collected since last `startSampling` call.
        """
        params = {}
        return self.driver.execute_and_wait("Memory.getSamplingProfile", params)

