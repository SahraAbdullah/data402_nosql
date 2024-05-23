## NOSQL

What is it?  NoSQL stands for Not Only SQL, it is a type of database management and system that differs from traditional relational databases. Nosql is unstructured and more scalable due its flexiblity.   
Compare SQL to NoSQL:  
- SQL databases are relational and NoSQL databases are non-relational
- SQL is vertically scalable, whereas NoSQL is githorizontally scalable
- SQL has on language which is sql, whereas in NoSQL there is a wide variety of languages you can use
- SQL is more structured, it used relational tables, NoSQL is unstructured which means you can use documents, graphs 
  
What language(s) can be used? in NoSQL, you can use JSON, XML, YAML, binary schema   

*Example NoSQL Schema design* 

![NoSQL Schema design](https://miro.medium.com/v2/resize:fit:1400/1*1_soKFBUMCpC8tnGQ3Y-2A.png)

NoSQL is scalable. Explain the concept and some benefits of it. Any negatives?    

NoSQL databases and MongoB are designed to be highly scalable. The scalability of NoSQL refers to their ability to handle increasing amounts if data and growing workloads without sacrificing performance.
benefits?  
- handling increased workload
- improved performance
- cost-effectiveness
- enhanced availability 
- future-proofing
negatives?  
- complexity 
- cost,
- data consistency 


Types of NoSQL Database?
- key-value pair
- documented-oriented
- graph-based
- time series

## MONGODB

What is MongoDB?    

is a built on a scale-out architecture that has become popular with developers because of developing scabale applications with evolving data schemas  


What are collections in Mongo?    
a collection is a grouping of MongoDB documents.
MongoDB stores data records as documents which gathered together in collections

What are Documents?  
- a record in MongoDB is a document, which is a data structure composed of field and value pairs.

MongoDB Architecture, how does it work?  

What are replica sets?  
is a group of mongodb processes that maintain the same data set.

What is sharding?   
is a method for distributing data across multiple machines

Advantages of MongoDB?
- flexibility
- simplicity
- documentation
- easy environment and a quick set up
- scalability
- Sharidng 

Disadvantages of MongoDB?    
- joins
- indexing
- limited data size and nesting
- duplicates 
- high memory usage  


What scenarios is MongoDB good for? 
- when dealing with big data
- real-time analytics, mongoDB is a flexible schema  allows for easy storage and retrieval of real-time data, making it ideal for analytics and reporting
- mobile and social apps, ability to handle hig read and write loads makes it a popular choice for mobile and social aps that requires fast and scalable data storage.

What scenarios is it not good for?  
- if you have a highly structured data model with complex relationships and transcations, a traditional SQL database would be more suitable.
- if an application requires strict data consistency.
  
## MongoDB Code along  


Use Sparta to create a new document  

db.createCollection("Academy")   

db.Academy.insertOne({
... "name": "Sahra"})  

db.Academy.insertMany([
... {"course":"Data Engineering", "length":10}, 
... {"course": "Data Analysis", "length":8}])
 
db.getCollectionInfos({name: "students"})

db.students.insertOne({name: "Mr S. Global", year: NumberInt(2024), score:88.2, address: {city: "Birmingham"}, course: "Data"})  

db.getCollectionNames()
db.students.find({})  
db.students.updateOne({name: "Mr S. Global"}, {$set: {score:92.5, newfield: true}})
db.students.updateOne({name: "Mr S. Global"}, {$unset: { newfield:null}})
db.students.updateMany({}, {$set: {year: NumberInt(2025)}})
  
Exercise 1   
- use Films
- db.createCollection("FavouriteFilms")
- db.FavouriteFilms.insertOne({"name": "Bullet Train"})
- db.FavouriteFilms.insertMany([{"name": "Bullet Train", "length":120}, {"name": "Notebook", "length":130}])

Exercise 2  
- db.collection.insertOne({"actors": "Brad Pitt"})
- db.FavouriteFilms.aggregate([{$addFields: {actresses: { $sum: "$name"}}}])
- db.FavouriteFilms.updateOne({actors: "Brad Pitt"}, {$set: {films:21, newfield: true}})
- db.FavouriteFilms.updateOne({actors: "Brad Pitt"}, {$unset: {newfield:null}})
- db.FavouriteFilms.deleteOne({actors: "Brad Pitt"})


exercise 5

use Starwars

db.characters.find({"name": "Luke Skywalker"})

db.characters.find({name: "chewbacca"}, {name:1, eye_color:1, _id:0})
excercise 6

db.characters.find({"species.name": "human"}, { name: 1, "homeworld.name"})
exercise 7 

db.characters.find({"eye_colour": {$in: ["yellow", "orange"]}})

db.characthers.find({eye_color: {$in: ["yellow", "orangne"]}})

Method 1 (simple)
Unset/set method - First query selects all documents where height = "unknown" and removes the height field from those documents only.
 

db.characters.updateMany(
  {height: "unknown"},
  {$unset: {height: ""}}
)
 
The second query gets all records and if they have a height feild, converts the contents to an int

db.characters.updateMany(
  {},
  [{$set: {height: {$toInt: "$height"}}}]
)
has context menu