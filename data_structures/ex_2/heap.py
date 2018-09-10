def heapsort(arr):
  # newHeap = Heap()
  # newArr = []
  # for i in arr:
  #   newHeap.insert(i)
  # while len(newHeap.storage) > 0:
  #   newArr.append(newHeap.storage[0])
  #   newHeap.delete()
  # return newArr

  newHeap = Heap()
  newArr = [0] * len(arr) #Allows you to set the size of the array, to avoid Python auto-setting a length and then working to epand it upon each new addition.
  for i in arr:
    newHeap.insert(i)
  for i in range(len(arr)-1, 0, -1):
    newArr[i] = newHeap.delete()
  return newArr

class Heap:
  def __init__(self):
    self.storage = []
    
  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    retval = self.storage[0]
    self.storage[0] = self.storage[len(self.storage) - 1]
    self.storage.pop()
    self._sift_down(0)
    return retval 

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while (index - 1) // 2 >= 0:
      if self.storage[(index - 1) // 2] < self.storage[index]:
        self.storage[index], self.storage[(index - 1) // 2] = self.storage[(index - 1) // 2], self.storage[index]
      index = (index - 1) // 2

  def _sift_down(self, index):
    while index * 2 + 1 <= len(self.storage) - 1:
      mc = self._max_child(index)
      if self.storage[index] < self.storage[mc]:
        self.storage[index], self.storage[mc] = self.storage[mc], self.storage[index]
      index = mc

  def _max_child(self, index):
    if index * 2 + 2 > len(self.storage) - 1:
      return index * 2 + 1
    else:
      return index * 2 + 1 if self.storage[index * 2 + 1] > self.storage[index * 2 + 2] else index * 2 + 2