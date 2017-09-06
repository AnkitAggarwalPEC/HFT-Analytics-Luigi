
class DequeQueue(collection.deque):
    """
    This is double ended queue interface
    """
    def put(self , obj , block= None , timeout = None):
        return self.append(obj)
    def get(self , block = None , timeout = None):
        try:
            return self.pop()
        except IndexError:
            raise Queue.Empty

class SingleProcessPool(object):
    """
    This is dummy process pool when we use a single processor
    """
    def apply_async(self , function , args):
        return function(*args)
    def close(self):
        pass
    def join(self):
        pass

def check_complete(task , out_queue):
    """
    Check if the task is comepleted , puts the result to the queue
    """
    try:
        #TODO:Implement the complete function
        is_complete = task.complete()
    except Exception:
        pass
    out_queue.put((task , is_complete))
class Worker(object):
    """
    Worker object that will handle the task submitted to it
    """

    def  add(self , task , multiprocess = False):
        """
        This will add the task submitted to a queue depending upon the multiprocess or not
        """
        if multiprocess:
            queue = multiprocessing.Manager().Queue()
            pool = multiprocess.Pool()
        else:
            queue = DequeQueue()
            pool = SingleProcessPool()
        pool.apply_async(check_complete , [task,queue])



