class IODomain:
    def __init__(self, driver):
        self.driver = driver

    def close(self, handle):
        """
        Close the stream, discard any temporary backing storage.
        - handle (any): Handle of the stream to close.
        """
        params = {}
        params["handle"] = handle
        return self.driver.execute_and_wait("IO.close", params)

    def read(self, handle, offset=None, size=None):
        """
        Read a chunk of the stream
        - handle (any): Handle of the stream to read.
        - offset (integer): Seek to the specified offset before reading (if not specified, proceed with offset
following the last read). Some types of streams may only support sequential reads.
        - size (integer): Maximum number of bytes to read (left upon the agent discretion if not specified).
        """
        params = {}
        params["handle"] = handle
        if offset is not None:
            params["offset"] = offset
        if size is not None:
            params["size"] = size
        return self.driver.execute_and_wait("IO.read", params)

    def resolveBlob(self, objectId):
        """
        Return UUID of Blob object specified by a remote object id.
        - objectId (any): Object id of a Blob object wrapper.
        """
        params = {}
        params["objectId"] = objectId
        return self.driver.execute_and_wait("IO.resolveBlob", params)

