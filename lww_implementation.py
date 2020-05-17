from threading import RLock

class LWW_implementation:
    
    def _init_(self):
        self.add_set = {}
        self.remove_set = {}
        self.lock_add = Rlock()
        self.lock_remove = Rlock()
        
    def add(self, element, timestamp):
        '''
        Purpose: This function adds an element to the add_set dictionary of the LWW, 
        where key is the element and value is the current timestamp
        
        On calling check_and_add(), if element is existing, timestamp is updated
        Else element is added as new entry
        '''
        
        self.lock_add.acquire()
        try:
            self.check_and_add(self.add_set, element, timestamp)
        except:
            return_flag = False
        finally:
            self.lock_add.release()
            
        return return_flag
        
    def remove(self, element, timestamp):
        '''
        Purpose: This function removes an element by adding an element to the remove_set dictionary of the LWW, 
        where key is the element and value is the current timestamp
        
        On calling check_and_add(), if element is existing, timestamp is updated
        Else element is added as new entry
        '''
        
        self.lock_remove.acquire()
        try:
            self.check_and_add(self.remove_set, element, timestamp)
        except:
            return_flag = False
        finally:
            self.lock_remove.release()
        
        return return_flag
        
    def check_and_add(self, target_set, element, timestamp):
        '''
        Purpose: This function checks the existence of an element either in add_set or remove_set
        
        If element is non-existent, insertion of the element happens.
        Else if element exists, update timestamp if passed timestamp is greater(i.e.latest) than the
        existing timestamp of the element.
        '''
                
        if element in target_set:
            current_timestamp = target_set[element]
            if current_timestamp < timestamp:
                target_set[element] = timestamp
        
        else:
            target_set[element] = timestamp
            
    def exist(self, element):
        '''
        Purpose: This function checks the existence of an element either in add_set or remove_set
        Keyword returns:
            -True: The element exists in lww-set
            -False: The element does not exists in lww-set
        '''
                       
        try:
            if element not in self.add_set:
                return False
            elif element not in self.remove_set:
                return True
            elif self.add_set[element] >= self.remove_set[element]:
                return True
            else:
                return False
        
        except:
            raise RuntimeError("Internal error")
            
    def merge(self):
        '''
        Purpose: This function returns an array of all the elements existing in the lww-set
        '''
        
        final_result = []
        for element in self.add_set:
            if self.exist(element):
                final_result.append(element)
        return final_result
