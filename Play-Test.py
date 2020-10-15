#!/usr/bin/env python
# coding: utf-8

# In[9]:


import csv, json, math, pandas as pd, requests, unittest, uuid

# MangoDB class declaration below here
class MangoDB:
    
    def __init__(self):
    #The MangoDB class should create only the default collection, as shown, 
    #on instantiation including a randomly generated uuid using the uuid4() method
        self.d = {
            'default': {
            'version':1.0,
            'db':'mangodb',
            'uuid':uuid.uuid4()
            }
        }
        #self.d = {}
        #self.d['default'] = {}
        #self.d['default']['version'] = '1.0'
        #self.d['default']['db'] = 'mangodb'
        #self.d['default']['uuid'] = uuid.uuid4()
    
    def display_all_collections(self):
        #iterate through every collection and print name and content
        for k, v in self.d.items():
            print("{0} : {1}".format(k, v))
        
        #there might be another layer here (ie. collection, dictionary) I have to access before ...
        
    def add_collection(self, collection_name):
        #add new (empty) collection with specified name
        self.d.update({collection_name:{}})
    
    def update_collection(self, collection_name, updates):
        self.d[collection_name] = updates #since updates is passed in as a dictionary
    
    def remove_collection(self, collection_name):
        del self.d[collection_name]
    
    def list_collections(self):
        #Display list of collection names
        print(self.d.get_collection_names())
    
    def get_collection_size(self, collection_name):
        return len(self.d[collection_name])
    
    def to_json(self, collection_name):
        json_object = json.dumps(self.d[collection_name], indent = 4) 
        return json_object
    
    def wipe(self):
        #iterate over collections, delete all
        for coll in self.d.items():
            remove_collection(coll)
        
        #reset with just default
        self.d = {
            'default': {
            'version':1.0,
            'db':'mangodb',
            'uuid':uuid.uuid4()
            }
        }
    
    def get_collection_names(self):
        #Return list of collection names
        return self.d.keys()
    
    
# ------ Create your classes here /\ /\ /\ ------

def exercise02():
    '''
    Create a class called MangoDB. The MangoDB class wraps a dictionary of dictionaries. At the the root level, each key/value will be called a collection, similar to the terminology used by MongoDB, an inferior version of MangoDB ;) A collection is a series of 2nd level key/value paries. The root value key is the name of the collection and the value is another dictionary containing arbitrary data for that collection.
    For example:
        {
            'default': {
            'version':1.0,
            'db':'mangodb',
            'uuid':'0fd7575d-d331-41b7-9598-33d6c9a1eae3'
            },
        {
            'temperatures': {
                1: 50,
                2: 100,
                3: 120
            }
        }

    The above is a representation of a dictionary of dictionaries. Default and temperatures are dictionaries or collections. The default collection has a series of key/value pairs that make up the collection. The MangoDB class should create only the default collection, as shown, on instantiation including a randomly generated uuid using the uuid4() method and have the following methods:
        - display_all_collections() which iterates through every collection and prints to screen each collection names and the collection's content underneath and may look something like:
            collection: default
                version 1.0
                db mangodb
                uuid 739bd6e8-c458-402d-9f2b-7012594cd741
            collection: temperatures
                1 50
                2 100
        - add_collection(collection_name) allows the caller to add a new collection by providing a name. The collection will be empty but will have a name.
        - update_collection(collection_name,updates) allows the caller to insert new items into a collection i.e.
                db = MangoDB()
                db.add_collection('temperatures')
                db.update_collection('temperatures',{1:50,2:100})
        - remove_collection() allows caller to delete a specific collection by name and its associated data
        - list_collections() displays a list of all the collections
        - get_collection_size(collection_name) finds the number of key/value pairs in a given collection
        - to_json(collection_name) that converts the collection to a JSON string
        - wipe() that cleans out the db and resets it with just a default collection
        - get_collection_names() that returns a list of collection names
        Make sure to never expose the underlying data structures
        
        For exercise02(), perform the following:
        - Create an instance of MangoDB
        - Add a collection called testscores
        - Take the test_scores list and insert it into the testscores collection, providing a sequential key i.e 1,2,3...
        - Display the size of the testscores collection
        - Display a list of collections
        - Display the db's UUID
        - Wipe the database clean
        - Display the db's UUID again, confirming it has changed
    '''

    test_scores = [99, 89, 88, 75, 66, 92, 75, 94, 88, 87, 88, 68, 52]

    # ------ Place code below here \/ \/ \/ ------
    
    db = MangoDB()
    db.add_collection('testscores')
    
    temp_dict = {}
    
    for k in range(len(test_scores)):
        temp_dict.update({str(k) : str(test_scores[k])})
    
    db.update_collection('testscores', temp_dict)
    
    db.get_collection_size('testscores')
    
    db.list_collections()
    
    db.display_all_collections() #is there a way to just display UUID?
    
    db.wipe()
    
    db.display_all_collections()
    
    ### LEFT OFF HERE
    
    # ------ Place code above here /\ /\ /\ ------
    

class TestAssignment3(unittest.TestCase):
    
    def test_exercise02(self):
        print('Testing exercise 2')
        exercise02()
        db = MangoDB()
        self.assertEqual(db.get_collection_size('default'), 3)
        self.assertEqual(len(db.get_collection_names()), 1)
        self.assertTrue('default' in db.get_collection_names())
        db.add_collection('temperatures')
        self.assertTrue('temperatures' in db.get_collection_names())
        self.assertEqual(len(db.get_collection_names()), 2)
        db.update_collection('temperatures', {1: 50})
        db.update_collection('temperatures', {2: 100})
        self.assertEqual(db.get_collection_size('temperatures'), 2)
        self.assertTrue(type(db.to_json('temperatures')) is str)
        self.assertEqual(db.to_json('temperatures'), '{"1": 50, "2": 100}')
        db.wipe()
        self.assertEqual(db.get_collection_size('default'), 3)
        self.assertEqual(len(db.get_collection_names()), 1)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)


# In[ ]:





# In[ ]:




