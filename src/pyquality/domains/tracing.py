class TracingDomain:
    def __init__(self, driver):
        self.driver = driver

    def end(self):
        """
        Stop trace events collection.
        """
        params = {}
        return self.driver.execute_and_wait("Tracing.end", params)

    def getCategories(self):
        """
        Gets supported tracing categories.
        """
        params = {}
        return self.driver.execute_and_wait("Tracing.getCategories", params)

    def getTrackEventDescriptor(self):
        """
        Return a descriptor for all available tracing categories.
        """
        params = {}
        return self.driver.execute_and_wait("Tracing.getTrackEventDescriptor", params)

    def recordClockSyncMarker(self, syncId):
        """
        Record a clock sync marker in the trace.
        - syncId (string): The ID of this clock sync marker
        """
        params = {}
        params["syncId"] = syncId
        return self.driver.execute_and_wait("Tracing.recordClockSyncMarker", params)

    def requestMemoryDump(self, deterministic=None, levelOfDetail=None):
        """
        Request a global memory dump.
        - deterministic (boolean): Enables more deterministic results by forcing garbage collection
        - levelOfDetail (any): Specifies level of details in memory dump. Defaults to "detailed".
        """
        params = {}
        if deterministic is not None:
            params["deterministic"] = deterministic
        if levelOfDetail is not None:
            params["levelOfDetail"] = levelOfDetail
        return self.driver.execute_and_wait("Tracing.requestMemoryDump", params)

    def start(self, categories=None, options=None, bufferUsageReportingInterval=None, transferMode=None, streamFormat=None, streamCompression=None, traceConfig=None, perfettoConfig=None, tracingBackend=None):
        """
        Start trace events collection.
        - categories (string): Category/tag filter
        - options (string): Tracing options
        - bufferUsageReportingInterval (number): If set, the agent will issue bufferUsage events at this interval, specified in milliseconds
        - transferMode (string): Whether to report trace events as series of dataCollected events or to save trace to a
stream (defaults to `ReportEvents`).
        - streamFormat (any): Trace data format to use. This only applies when using `ReturnAsStream`
transfer mode (defaults to `json`).
        - streamCompression (any): Compression format to use. This only applies when using `ReturnAsStream`
transfer mode (defaults to `none`)
        - traceConfig (any): 
        - perfettoConfig (string): Base64-encoded serialized perfetto.protos.TraceConfig protobuf message
When specified, the parameters `categories`, `options`, `traceConfig`
are ignored. (Encoded as a base64 string when passed over JSON)
        - tracingBackend (any): Backend type (defaults to `auto`)
        """
        params = {}
        if categories is not None:
            params["categories"] = categories
        if options is not None:
            params["options"] = options
        if bufferUsageReportingInterval is not None:
            params["bufferUsageReportingInterval"] = bufferUsageReportingInterval
        if transferMode is not None:
            params["transferMode"] = transferMode
        if streamFormat is not None:
            params["streamFormat"] = streamFormat
        if streamCompression is not None:
            params["streamCompression"] = streamCompression
        if traceConfig is not None:
            params["traceConfig"] = traceConfig
        if perfettoConfig is not None:
            params["perfettoConfig"] = perfettoConfig
        if tracingBackend is not None:
            params["tracingBackend"] = tracingBackend
        return self.driver.execute_and_wait("Tracing.start", params)

