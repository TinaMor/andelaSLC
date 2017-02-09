class BinarySearch(object):
  def __init__(self, a, b):
    self.a = a
    self.b = b
    self.myList = range(b, (a*b)+1)
    self.length = a

  def __getitem__(self, number):
    return self.myList[number]
  def __setitem__(self, number, n):
    return self.myList[number] == n

  def search(self, n):
    index_0 = 0
    index_last = self.a - 1
    count = 0

    if self.myList[index_0] == n:
      return {'count': 0, 'index': index_0}
    elif self.myList[index_last] == n:
      return {'count': 0, 'index': index_last}
    else:
      while index_0 <= index_last:
        index_mid = (index_0 + index_last) // 2
        count += 1

        if self.myList[index_mid] == n:
          return {'count': count, 'index': index_mid}
        elif n > self.myList[index_mid]:
          index_0 = index_mid + 1
        elif n < self.myList[index_mid]:
          index_last = index_mid - 1
        if index_0 > index_last :
          return {'count': 0, 'index': -1}