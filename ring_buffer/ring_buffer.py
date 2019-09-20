class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    #This check will will run first
    # essentially finding the oldest.
    # ex [a, c, e] append g then i
    # wil be [g, i, e]
    if self.current == self.capacity:
      self.current = 0
      self.storage[0] = item

    self.storage[self.current] = item
    self.current += 1

  def get(self):
    return [x for x in self.storage if x is not None]