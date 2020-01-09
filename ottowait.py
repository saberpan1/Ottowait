import time
class Ottowait(object):
    def __init__(self,driver):
        self.driver = driver
    #TODO:find_elements
    def find_element(self,by,element,readonly=None):
        if readonly==None:
            for i in range(10):
                try:
                    time.sleep(1)
                    a = self.driver.find_element(by=by, value=element)
                    return a
                except Exception:
                    pass
            else:
                raise Exception('time out:未找到元素，请重新定位')
        elif readonly == 'readonly':
            try:
                element = Ottowait.find_element(self, by, element)
                self.driver.execute_script("arguments[0].removeAttribute('readonly')",element)
                element.clear()
                return element
            except:
                print('can not remove')
        else:
            raise Exception

    def find_elements(self,by,element,readonly=None):
        if readonly==None:
            for i in range(10):
                try:
                    time.sleep(1)
                    a = self.driver.find_elements(by=by, value=element)
                    return a
                except Exception:
                    pass
            else:
                raise Exception('time out:未找到元素，请重新定位')
        elif readonly == 'readonly':
            try:
                element = Ottowait.find_elements(self, by, element)
                self.driver.execute_script("arguments[0].removeAttribute('readonly')",element)
                element.clear()
                return element
            except:
                print('can not remove')
        else:
            raise Exception
