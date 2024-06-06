class HashTable:
    def __init__(self,size):
        self.size=size
        self.create_hash_table()

    def create_hash_table(self):
        self.hash_table=[[] for _ in range(self.size)]
    
    #insert key and value pair in hashtable, if key already exists update its value
    def insert(self,key,value):
        hash_value=hash(key)%self.size
        bucket=self.hash_table[hash_value]

        isFound=False
        idx=-1
        for i in range(len(bucket)):
            stored_key,stored_value=bucket[i]
            if stored_key == key:
                isFound=True
                idx=i
                break
        if isFound:
            self.hash_table[hash_value][idx]=(key, value)
        else:
            self.hash_table[hash_value].append((key,value))


    #Given a key, return its value if exists else return an error message
    def get(self,key):
        hash_value=hash(key)%self.size
        bucket=self.hash_table[hash_value]
        for i in range(len(bucket)):
            stored_key,stored_value=bucket[i]
            if stored_key == key:
                return stored_value
        
        return "Hashtable doesnot contain key : "+key
    
    #Takes a key and deletes it from the hashtable if it exists
    #else returns an error message
    def delete(self,key):
        hash_val=hash(key)%self.size
        bucket=self.hash_table[hash_val]

        isFound=False
        idx=-1
        for i in range (len(bucket)):
            stored_key,stored_value=bucket[i]

            if stored_key==key:
                isFound=True
                idx=i
        if isFound:
            self.hash_table[hash_val].pop(idx)
        else:
            print("Entry not found with key : ",key)


#Main
hash_table=HashTable(10)
hash_table.insert("Sam",93)
hash_table.insert("Annie",88)
print(hash_table.get("Annie"))
print(hash_table.get("Harry"))
hash_table.insert("Harry",82)
print(hash_table.get("Harry"))

hash_table.delete("Sandra")
hash_table.delete("Harry")
print(hash_table.get("Harry"))
print(hash_table.get("Sam"))