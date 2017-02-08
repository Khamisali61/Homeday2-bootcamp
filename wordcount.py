def words(n): #function takes words as input and separates them using their whitespaces
    results = {} #sictionary to store results
    
    separatedwords = n.split() #split string to single words
    
    if len(separatedwords) == 1:
        results[separatedwords[0]] = 1
        return results
    else:
        for item in separatedwords:
            if item.isdigit():
                item = int(item)
            results[item] = separatedwords.count(str(item))
        return results
