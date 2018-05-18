# implementation of the quicksort sorting algorithm

def qsort(li):
    if li == []:
      return []
    else:
      pivot = li[0]
      lesser = qsort([x for x in li[1:] if x<pivot])
      greater = qsort([x for x in li[1:] if x>=pivot])
      return lesser + [pivot] + greater
