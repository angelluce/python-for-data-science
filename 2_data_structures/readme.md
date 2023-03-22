# Python Data Structures

## Glossary

| Term       | Definition |
| ---------- | ---------- |
| Compound Data Type | A composite of primitive data types. Lists and tuples are examples. |
| Dictionary | A mutable ordered data structure in Python used to store key-value pairs. A value can be referred to by its key. |
| Intersection | In two or more sets of data, the intersection of those sets is the set of elements that the original data sets have in common. |
| List       | A mutable ordered data structure in Python that contains zero or more primitive or compound data type elements. |
| Set        | An unordered, mutable collection of unique elements. |
| Tuple      | An immutable ordered data structure in Python that contains zero or more primitive or compound data type elements. |
| Union      | In two or more sets of data, the union of those data sets is the set of all the elements in each data set. |


## Cheatsheet

| Class or Method | Description | Example     |
| --------------- | ----------- | ----------- |
| `<varname>[-<index>]` | A negative index counts from the last value in a list or a tuple. | `myList=[‘a’,‘b’,‘c’,‘d’,‘e’,‘f’]` </br> `#myValue is assigned ‘e’` </br> `myValue=myList[-2]` |
| `<varname>[<index1>:<index2>]` | Slice a list or a tuple. | `myList=[‘a’,‘b’,‘c’,‘d’,‘e’,‘f’]` </br> `# myValues=[‘c’,‘d’,‘e’]` </br> `myValues=myList[2:5]` |
| `append()` | Add elements to the end of a list. | `myList=[‘a’,‘b’,‘c’,‘d’,‘e’,‘f’]` </br> `# myList is assigned` </br> `# myList=[‘a’,‘b’,‘c’,‘d’,‘e’,‘f’,‘g’,‘h’]` </br> `myList.append([‘g’,‘h’])` |
| `del()` | Deletes a value from a list. | `myList=[‘a’,‘b’,‘c’,‘d’,‘e’,‘f’]` </br> `#myList is now =[‘b’,‘c’,‘d’,‘e’,‘f’]` </br> `del(myList[0])` |
| `split()` | Convert a string to a list. Every group of characters separated by a space becomes an element. | `myList=“hard rock”` </br> `#myValues is assigned [‘hard’, ‘rock’]` </br> `MyValues=myList.split()` |
|  `sorted()` | Sort a tuple, returns a list. | `myList=(‘d’,‘c’,‘a’,‘e’,‘b’,‘f’)` </br> `#myValues is assigned [‘a’,‘b’,‘c’,‘d’,‘e’,‘f’]` </br> `myValues=sorted(myList)` |
| `<varname>={<key1>:<value1>, <key2>:<value2>…<keyi:valuei>}` | Create a dictionary and assign to a variable. Duplicated keys are not allowed. | Dict={“breed”:“german shepherd”, “color”: “black”, “gender”:“female”} |
| `keys()` | Get all the keys in a dictionary. Returns a list. | `Dict={“breed”:“german shepherd”, “color”: “black”, “gender”:“female”}` </br> `#getkeys is assigned [“breed”, “color”, “gender”]` </br> `getkeys=Dict.keys()` |
| `values()` | Get all the values in a dictionary. Returns a list. | `Dict={“breed”:“german shepherd”, “color”:“black”, “gender”:“female”}` </br> `#getvalues is assigned [“german shepherd”, “black”, “gender”]` </br> `getvalues=Dict.values()` |
