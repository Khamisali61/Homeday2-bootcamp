def find_max_min(n):
  resultList = []
  max_number = max(n)
  min_number = min(n)
  if min_number == max_number: #if min and max are equal return number of elements in list
    number_of_elements = len(n)
    resultList.append(number_of_elements)
  else:
    resultList.append(min_number)
    resultList.append(max_number)
  return resultList