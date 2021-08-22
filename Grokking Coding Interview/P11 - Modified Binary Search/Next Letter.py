def search_next_letter(letters, key):
  if ord(key) >= ord(letters[-1]):
    return letters[0] # circular

  start = 0
  end = len(letters)-1

  while start <= end:
    mid = start + (end-start)/2
    mid = int(mid)


    if ord(letters[mid]) <= ord(key):
      start = mid + 1

    else:
      end = mid - 1

  return letters[start]


def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()
