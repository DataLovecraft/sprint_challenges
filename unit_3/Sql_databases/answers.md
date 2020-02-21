
# Part 4 - Questions (and your Answers)

Answer the following questions, baseline ~3-5 sentences each, as if they were interview screening questions (a form you fill when applying for a job):

- In the Northwind database, what is the type of relationship between the Employee and Territory tables?

`Employees and Territories have a many-to-many relationship`

- What is a situation where a document store (like MongoDB) is appropriate, and what is a situation where it is not appropriate?

`Document stores are suited towards storing documents like objects - unstructured data such as news articles, user-generated content, and tags, etc.

Document stores are less appropriate when you either really need the strong ACID guarantees of a relational database.`

- What is "NewSQL", and what is it trying to achieve?

  `NewSQL is the new kid on the block that wants to show off its
   skill. NewSQL is a new approach to relational databases that wants to combine transactional ACID (atomicity, consistency, isolation, durability) guarantees of the old RDBMSs and the horizontal scalability of NoSQL`
