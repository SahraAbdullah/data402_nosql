## NOSQL

What is it?  NoSQL stands for Not Only SQL, it is a type of database management and system that differs from traditional relational databases. Nosql is unstructured and more scalable due its flexiblity.   
Compare SQL to NoSQL-   
- SQL databases are relational and NoSQL databases are non-relational
- SQL is vertically scalable, whereas NoSQL is horizontally scalable
- SQL has on language which is sql, whereas in NoSQL there is a wide variety of languages you can use
- SQL is more structured, it used relational tables, NoSQL is unstructured which means you can use documents, graphs 
  
What language(s) can be used? in NoSQL, you can use JSON, XML, YAML, binary schema   

Example NoSQL Schema design
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
- a record in MongoDB is a document, which is a data struture composed of field and value pairs.

MongoDB Architecture, how does it work?  

What are replica sets?  
is a group of mongod processess that maintain the same data set.

What is sharding?   
is a method for distributing data acroos multiple machines

Advantages of MongoDB?
- flexibility
- simplicity
- documentation
- easy environment and a quick set up
- scalability
- sharidng 

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