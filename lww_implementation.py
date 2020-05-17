from threading import RLock

class LWW:
    
    def _init_(self):
        self.add_set = {}
        self.remove_set = {}
        self.lock_add = Rlock()
        self.lock_remove = Rlock()
        
    def add(self, element, timestamp):
        
        self.lock_add.acquire()
        try:
            self.check_and_add(self.add_set, element, timestamp)
        except:
            return_flag = False
        finally:
            self.lock_add.release()
            
        return return_flag
        
    def remove(self, element, timestamp):
        
        self.lock_remove.acquire()
        try:
            self.check_and_add(self.remove_set, element, timestamp)
        except:
            return_flag = False
        finally:
            self.lock_remove.release()
        
        return return_flag
        
    def check_and_add(self, target_set, element, timestamp):
        
        if element in target_set:
            current_timestamp = target_set[element]
            if current_timestamp < timestamp:
                target_set[element] = timestamp
        
        else:
            target_set[element] = timestamp
            
    def exist(self, element):
        
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
        final_result = []
        for element in self.add_set:
            if self.exist(element):
                final_result.append(element)
        return final_result
