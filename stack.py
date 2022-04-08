#stack implememntation in python using list
#last in first out
class queue:

    def __init__(self):
        self.queue = []
    def equeue(self,item):
        self.queue.append(item)
    def dequeue(self):
        self.queue.pop(0)


