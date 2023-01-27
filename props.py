class Properties:
    SSID_PROPERTY_NAME = "ssid"
    PASSWD_PROPERTY_NAME = "passwd"
    ENCODING = "utf8"
    PROP_SEPARATOR = ":"

    properties = {}

    def __init__(self) -> None:
        with open('properties/application.properties', 'r', encoding=self.ENCODING) as file:
            for line in file:
                vals = line.split(self.PROP_SEPARATOR)
                self.properties[vals[0]] = vals[1].replace('\n', ' ').replace('\r', '').replace(' ','')
        print(self.properties)

    def getProperty(self, propertyName):
        return self.properties[propertyName]

    def getSsid(self):
        return self.getProperty(self.SSID_PROPERTY_NAME)

    def getPassword(self):
        return self.getProperty(self.PASSWD_PROPERTY_NAME)
