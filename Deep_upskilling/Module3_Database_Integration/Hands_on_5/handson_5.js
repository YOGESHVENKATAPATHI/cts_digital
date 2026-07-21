// Module 3 : Database Integration

// Hands-On 5: MongoDB - CRUD & Aggregation

// TASK 1: Create Database & Collection

// QN 60: Creation of database

//use college_nosql_db

// QN 61: Create Collection
db.createCollection("feedback")


// QN 62: Insert Sample Documents

db.feedback.insertMany([
{
student_id:1,
course_code:"CS101",
semester:"2022-ODD",
rating:5,
comments:"Excellent teaching and easy to understand.",
tags:["challenging","well-structured","good-examples"],
submitted_at:new Date("2022-11-30"),
attachments:[{ filename:"notes.pdf", size_kb:240 }]
},
{
student_id:2,
course_code:"CS101",
semester:"2022-ODD",
rating:4,
comments:"Very informative.",
tags:["challenging","interactive"],
submitted_at:new Date("2022-11-25"),
attachments:[{ filename:"assignment.pdf", size_kb:180}]
},

{
student_id:3,
course_code:"CS101",
semester:"2022-ODD",
rating:3,
comments:"Average course.",
tags:["difficult"],
submitted_at:new Date("2022-11-28"),
attachments:[{ filename:"feedback.docx", size_kb:120 }]
},

{
student_id:4,
course_code:"CS102",
semester:"2022-ODD",
rating:5,
comments:"Loved the database concepts.",
tags:["sql","interesting"],
submitted_at:new Date("2022-11-22"),
attachments:[{ filename:"db.pdf",size_kb:150 }]
},
{
student_id:5,
course_code:"CS102",
semester:"2022-ODD",
rating:2,
comments:"Needs more practical sessions.",
tags:["boring"],
submitted_at:new Date("2022-11-23"),
attachments:[{ filename:"report.pdf",size_kb:210 } ]
},
{
student_id:6,
course_code:"CS103",
semester:"2022-ODD",
rating:4,
comments:"Good examples.",
tags:["oop","coding"],
submitted_at:new Date("2022-11-21"),
attachments:[{ filename:"lab.pdf",size_kb:170 }]
},
{
student_id:7,
course_code:"EC101",
semester:"2021-EVEN",
rating:2,
comments:"Very difficult.",
tags:["challenging"],
submitted_at:new Date("2021-11-30"),
attachments:[{ filename:"notes.pdf", size_kb:140 }]
},
{
student_id:8,
course_code:"ME101",
semester:"2022-ODD",
rating:5,
comments:"Excellent practical sessions.",
tags:["lab","practical"],
submitted_at:new Date("2022-11-20"),
attachments:[{ filename:"labmanual.pdf", size_kb:300 }]
},
{
student_id:13,
course_code:"CS102",
semester:"2022-ODD",
rating:1,
comments:"Needs improvement.",
tags:["boring"],
submitted_at:new Date("2022-11-27"),
attachments:[{ filename:"review.pdf", size_kb:90}]
}
])


// QN 63: One document without attachments
db.feedback.insertOne([
{
student_id:12,
course_code:"CS103",
semester:"2022-ODD",
rating:4,
comments:"Nice course.",
tags:["coding","interesting"],
submitted_at:new Date("2022-11-29")
},
])

// QN 64: Verify Count

db.feedback.countDocuments()


// TASK 2: CRUD Operations

// QN 65 Finding rating 5 feedbacks
db.feedback.find({ rating:5 })


// QN 66 Finding feedbacks with course_code "CS101" and tag "challenging"
db.feedback.find({ course_code:"CS101",tags:"challenging"})


// QN 67 Finding student_id, course_code and rating of all feedbacks
db.feedback.find({},{ _id:0, student_id:1, course_code:1, rating:1 })


// QN 68 Finding feedbacks with rating less than 3 and updating them to add a new field "needs_review" with value true
db.feedback.updateMany({ rating: { $lt:3 }}, { $set: { needs_review:true }})


// QN 69 Finding feedbacks with "needs_review" field and adding a new tag "reviewed" to them
db.feedback.updateMany({needs_review:true},{$push:{tags:"reviewed"}})


// QN 70 Deleting all feedbacks with semester "2021-EVEN"
db.feedback.deleteMany({ semester:"2021-EVEN" })


// TASK 3: Aggregation Pipeline

// QN 71 Finding average rating and feedback count for each course in the semester "2022-ODD" and sorting them in descending order of average rating
db.feedback.aggregate([{$match:{semester:"2022-ODD"}},
{$group:{_id:"$course_code",avg_rating:{ $avg:"$rating"},
feedback_count:{$sum:1}}},{$sort:{avg_rating:-1}}])


// QN 72 Finding average rating and feedback count for each course in the semester "2022-ODD", rounding the average rating to 1 decimal place, and sorting them in descending order of average rating
db.feedback.aggregate([{$match:{semester:"2022-ODD"}},
{$group:{_id:"$course_code",avg_rating:{$avg:"$rating"},
feedback_count:{$sum:1}}},
{$project:{_id:0,course_code:"$_id",average_rating:
{ $round:["$avg_rating",1] },feedback_count:1}},
{ $sort: {average_rating:-1}}])


// QN 73 Finding the most common tags used in feedbacks and sorting them in descending order of their count

db.feedback.aggregate([{$unwind:"$tags"},
{ $group: {_id:"$tags",count:{$sum:1}}},
{ $sort:  {count:-1}}])


// QN 74 

// Creating an index on the "course_code" field to optimize queries that filter by course code
db.feedback.createIndex({course_code:1})

// Checking the execution stats of a query that filters by course code to see if the index is being used
db.feedback.find({course_code:"CS101"}).explain("executionStats")


