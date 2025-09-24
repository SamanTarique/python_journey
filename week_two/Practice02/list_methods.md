##### a.append(<element>)
- inserts a value at the end of the list , return None

##### a.insert(<index> , <element>)
- insert a value at the specified position , return None

##### a.extend([<element>,...])
- insert the elements of an iterable to the end of a list

##### a.pop(<index>)
- removes the last element by defaultnad if index is provided removes the element from that specified index returns the popped element

##### a.remove(<element>)
- remove the specific element from the list , returns None

##### a.clear()
- empty the list [] , returns None

##### a.copy()
- returns the copy of the list

##### a.count(<element>)
- returns the count of the specified element , if not found in the list returns 0

##### a.reverse()
- Reverse the order of the list and return None

##### a.sort(reverse=True|False, key=myFunc)
- Sort the list in ascending order by default and for string list alphabetically. we can also reverse and pass a function to sort on the basis of a property or key

a = ['Ford', 'Mitsubishi', 'BMW', 'VW']
print(a.sort(reverse=True, key=lambda x: len(x)))
print(a)