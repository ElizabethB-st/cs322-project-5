
from pymongo import MongoClient
import os


client = MongoClient('mongodb://' + os.environ['MONGODB_HOSTNAME'], 27017)

# Use database "brevet"
db = client.brevet

# Use collection "lists" in the databse
collection = db.lists


def get_brevet():
    """
    Obtains the newest document in the "lists" collection in database "brevet".

    Returns title (string) and items (list of dictionaries) as a tuple.
    """
    # Get documents (rows) in our collection (table),
    # Sort by primary key in descending order and limit to 1 document (row)
    # This will translate into finding the newest inserted document.

    lists = collection.find().sort("_id", -1).limit(1)

    # lists is a PyMongo cursor, which acts like a pointer.
    # We need to iterate through it, even if we know it has only one entry:
    for brevet_list in lists:
        # We store all of our lists as documents with these fields:
        ## "items": items
        ## "start_time": start_time
        ## "brevet_dist_km": brevet_dist_km
        # Each item has:
        ##"km": km,
        ## "miles": miles,
        ## "location": location, 
        ##"open_time": open_time,
        ##"close_time": close_time
        return brevet_list["items"], brevet_list["start_time"], brevet_list["brevet_dist_km"]
    
def insert_brevet(items, start_time, brevet_dist_km):
    """
    Inserts a new to-do list into the database "brevet", under the collection "lists".
    
    Inputs a title (string) and items (list of dictionaries)

    Returns the unique ID assigned to the document by mongo (primary key.)
    """
    output = collection.insert_one({
        "items": items,
        "start_time": start_time,
        "brevet_dist_km": brevet_dist_km})
    _id = output.inserted_id # this is how you obtain the primary key (_id) mongo assigns to your inserted document.
    return str(_id)
