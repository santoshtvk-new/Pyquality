class FileSystemDomain:
    def __init__(self, driver):
        self.driver = driver

    def getDirectory(self, bucketFileSystemLocator):
        """
        Call FileSystem.getDirectory
        - bucketFileSystemLocator (any): 
        """
        params = {}
        params["bucketFileSystemLocator"] = bucketFileSystemLocator
        return self.driver.execute_and_wait("FileSystem.getDirectory", params)

