
# refactor 1
def checkMenuBarIsHidden(self):
    self.elementClick(loc_Universal.LEFT_ARROW, "xpath")
    time.sleep(1)
    el = self.getElement(loc_Universal.MENU_DISPLAYED)
    barHidden = el.size["width"]
    if barHidden < 30:
        return True
    else:
        return False  # otherwise it returns None


# refactor 2
def verifyExpectedDevice_1(self, attr):
    gridList = self.getTextFromElements(loc_EdgeMngtConfigureGateways.CLMN_GATEWAY_NAME)

    """for name in gridList:
        if name == data_EdgeGatewayManagement.expected_device_1:
            return True"""
    return any(name for name in gridList if name == getattr(data_EdgeGatewayManagement, attr))

# insert data_EdgeGatewayManagement.expected_device_1 in place of (data_EdgeGatewayManagement, attr)