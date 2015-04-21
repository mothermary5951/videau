def new(num_buckets=256):               # creates a new function with the potential for 256 (2 to the 7th) containers                      
    """Initializes a Map with the given number of buckets."""   #  python uses 'map' instead of 'dictionary'                               
    aMap = []                           # variable 'aMap' starts as an empty list of lists WHICH CAN BE INDEXED BECAUSE THEY ARE ORDERED
    for i in range(0, num_buckets):    # for integer in range of 0 to 256, makes a bucket list to                                           
        aMap.append([])                # append new buckets to variable list 'aMap' within the function 'new' and                          
    return aMap                    # returns the total list aMap increased by one bucket list.                                                         

def hash_key(aMap, key):              #'hash is a builtin function. 'hash_key' requires 2 arguments: a new key and the aMap list index           
    """Given a key, this will create a number and then convert it to an index for the aMap's buckets.""" # hash converts string to integer
    return hash(key) % len(aMap)   #  returns the modulo remainder to be sure the index fits within the aMap larger string                 

def get_bucket(aMap, key):        # 'Get' is a builtin method for finding values:  this 'get' matches a key to where its bucket could be   
    """Given a key, find the bucket where it would go."""
    bucket_id = hash_key(aMap, key) # the bucket_id is defined by calling hash_key on a specific key in aMap list.                         
    return aMap[bucket_id]      #  Adds the bucket_id to the aMap list                                                                     

def get_slot(aMap, key, default=None):  #  Slots are subdivisions within bucket, like '1a, 1b', to avoid computer hash collisions.         
    """                                                                                                                                    
    Returns the index, key, and value of a slot found in a bucket.                                                                         
    Returns -1, key, and default (None if not set) when not found.                                                                         
    """
    bucket = get_bucket(aMap, key)  # Identifies a bucket                                                                                  

    for i, kv in enumerate(bucket):   # iterates through the 3 features 'enumerated' in a general slot in a bucket,                        
        k, v = kv                     #  where key, value = kv                                                                             
        if key == k:                 # if specified key is recognized, then                                                                
            return i, k, v          # return the 3-feature tuple that is in the bucket's slot on the aMap list,                            

    return -1, key, default       # if it's not, the function returns the default "none"                                                   

def get(aMap, key, default=None):       #  fetches the list aMap and its keys or non-members                                               
    """Gets the value in a bucket for the given key, or the default."""
    i, k, v = get_slot(aMap, key, default=default)  #  calls get_slot to identify the 3 features of each slot                              
    return v              # returns only the value in a given slot                                                                         

def set(aMap, key, value):      # new function called set;  not the python builtin class                                                   
    """Sets the key to the value, replacing any existing value."""
    bucket = get_bucket(aMap, key)   # names get_bucket return 'bucket'                                                                    
    i, k, v = get_slot(aMap, key)    # names get_slot return 'i, k, v'                                                                     

    if i >= 0:                        # for slot-integer numbers >= 0, set the key and value in place of the integer                       
        # the key exists, replace it.                                                                                                      
        bucket[i] = (key, value)    # sets one integer,one key, and one value per bucket, overwriting whatever is in there before.         
    else:
        # the key does not, append to create it    # if the key does not exist, make a new bucket and add it to aMap list                  
        bucket.append((key, value))

def delete(aMap, key):          #  deletes a key from the aMap list                                                                        
    """Deletes the given key from the Map."""
    bucket = get_bucket(aMap, key)  # restatement of 'bucket' definition on lines 22 & 38                                                  

    for i in xrange(len(bucket)):  # for slot-integer number inside the length of the bucket                                               
        k, v = bucket[i]         #  where key and value map to the integer                                                                 
        if key == k:             # if the 'key' specified matches the k in bucket[i]                                                       
            del bucket[i]        #  then delete the bucket                                                                                 
            break               # and then stop deleting                                                                                   

def dump(aMap):                 # print out hash/index integer (same thing in this script) & keys/values list for each bucket in the aMap list
    """Prints out what's in the Map."""
    for index, bucket in enumerate(aMap):  # The index of each dict pair/list in aMap list is the Same Thing as the hash assignment in THIS script.
        for kv in bucket:
            k, v = kv                     #  where key, value = kv
            print index, k, v      


## NOTE ON 'ENUMERATE':  The builtin function 'enumerate' counts items in any iterable object (MUST be an object) and assigns an index to each item, which
## can be acccessed with a two-part for-loop such as
##            for index, item in enumerate(SomeListorListofListsorWhatever)
##                print index, item
##  or like the first for-loop in the 'dump' function above, but there the index counts the Buckets and the key & value are tuples In the buckets.

##  NOTE ON 'HASH':  Hash is a python builtin function that (among other things) assigns an integer to a string to establish its           
##   position in a Map or larger string;  works sort of like an index in a tuple.  It uses the modulo to divide the hash(key) assigned     
##   integer into the total string length to be sure that the position assigned fits within the string length.  Hashing is made of deep    
##  computer magic algorithms developed by thousands of programmers over 30 years.  BELIEVE, TRUST, and USE!!!                             

########  In python, printing out list members and then printing out 'i'-indices and 'b'-list members via the 'enumerate' builtin
## >>> bucket = [1, 2, 3, 4]
## >>> for b in bucket:
## ...   print b
## ... 
## 1
## 2
## 3
## 4
## >>> for i,b in enumerate(bucket):
## ... 
## ...   print i,b
## ... 
## 0 1
## 1 2
## 2 3
## 3 4
## >>> 


