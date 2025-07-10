#Creating Connection
from pymongo import MongoClient
client=MongoClient('mongodb://localhost:27017/)')
#Using Database and collection
db=client['student_data_janitha']
collection=db["college"]
#Function for inserting documents
def create_doc():
    document=[{'id':1,'name':'JJ','city':'calicut'},
              {'id':2,'name':'cody','city':'mumbai'},
              {'id':3,'name':'bella','city':'mumbai'},
              {'id':4,'name':'nina','city':'delhi'},
              {'id':5,'name':'cece','city':'chennai'},
              {'id':6,'name':'cody','city':'kolkata'},
              {'id':7,'name':'cody','city':'bhopal'},
              {'id':8,'name':'bella','city':'pune'},
              {'id':9,'name':'nina','city':'delhi'},
              {'id':10,'name':'JJ','city':'bangalore'}]
    collection.insert_many(document)
#Function for reading documents
def read_doc():
    result=collection.find()
    print("\nREADING THE DOCUMENTS")
    for i in result:
        print(i)
#function for updating documents
def update_doc(x,y,z):
    if z=='one':
        result=collection.update_one({'name':x},{'$set':{'city':y}})
        print(f"\nUPDATED {z} OCCURENCE OF {x}: changed city {y}")
        read_doc()
    else:
        result=collection.update_many({'name':x},{'$set':{'city':y}})
        print(f"\nUPDATED {z} OCCURENCES OF {x}: changed city {y}")
        read_doc()
#Function for Deleting documents
def delete_doc(x,z):
    if z=='one':
        result=collection.delete_one({'name':x})
        print(f"\nDELETED {z} OCCURENCE OF {x}")
        read_doc()
    else:
        result=collection.delete_many({'name':x})
        print(f"\nDELETED {z} OCCURENCES OF {x}")
        read_doc()
#Main function
def main():
    collection.delete_many({}) #clears the collection
    create_doc()
    read_doc()
    update_doc('bella','amritsar','one') #update bella: city "amritsar" one time
    update_doc('cody','kochi','many') #update cody: city "kochi" multiple times
    delete_doc('cody','one') #update bella: city "amritsar" one time
    delete_doc('nina','many') #update cody: city "kochi" multiple times
    read_doc()
main()