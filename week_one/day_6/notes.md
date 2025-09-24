# What is Dictionaties
    - Python dictionary is a data structure that stores the value in key: value pairs. Values in a dictionary can be of any data type and can be duplicated, whereas keys can't be repeated and must be immutable. 

    * Dictionary keys are case sensitive: the same name but different cases of Key will be treated distinctly. 

    * Keys must be immutable: This means keys can be strings, numbers or tuples but not lists.

    * Keys must be unique: Duplicate keys are not allowed and any duplicate key will overwrite the      previous value.
    
    * Dictionary internally uses hashing. Hence, operations like search, insert, delete can be performed in Constant Time. 

    # Dictionary Methods

        d={1:"anurodh",2:"kumar",3:"python",'a':"hello",'b':"world"}

        - del
            Deletes the key value pair from the dictionary.
            eg: del d[3]
        
        - pop(<key>)
            * Removes the key value pair from the dictionary on the basis of key passed in parenthesis. and returns the value of that key in response.
            * If that key is not present throws an error.
            
            eg: d.pop('a')
        
        - popitem()
            * Pops out the last key-value pair in the dictionary. Returns that key value pair in response.
            * Throws error if dictionary is empty.

            eg: d.popitem()

        - clear()
            Empty the dictionary , removes every key - value pair present.

            eg: d.clear()
            
# Pickiling
    - Pickling is a way to convert a Python object (list, dictionary, etc.) into a Byte stream. This Byte stream contains all essential information about the object so that it can be reconstructed, or "unpickled" and get back into its original form in any Python. 

                Object (list,tuple,dict,string,etc)
                    |
                    |
                    |
                Serialize
                    |
                    |
                    |
                Byte Stream
                    |
                    |
                    |
             File / DB / Memory
                    |
                    |
                    |
              De- Serialize ( Byte Stream )
                    |
                    |
                    |
                  Object

    Serealization
        - This is the process of converting a Python object (such as a list, dictionary, custom class instance, etc.) into a byte stream
    
    Deserialization
        - This is the reverse process of converting a byte stream back into a Python object. 

    