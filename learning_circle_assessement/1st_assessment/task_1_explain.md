# Explain how you intend to represent this data in a table and how the events are related.

Taking a look at one of the json files from the each of **cards** and **users**, we get a structure as such:
 For cards;
 ```json
 {
   "payload": {
     "id": 2079,
     "user_id": 745,
     "created_by_name": "Troy Rosario",
     "updated_at": "2023-10-23 23:18:15",
     "created_at": "2023-10-23 23:16:17",
     "active": true
   },
   "metadata": {
     "type": "card",
     "event_at": "2023-10-23 23:18:15",
     "event_id": "0a4d29d2-b6dd-42a9-88af-840ead26202f"
   }
 }

 And for Users;
 ```json
 {
   "metadata": {
     "type": "user",
     "event_at": "2023-10-23 22:55:01",
     "event_id": "ffeba865-5a59-4320-8f27-c40f204d1bc2"
   },
   "payload": {
     "id": 403,
     "name": "Cassidy Hubbard",
     "address": "8518 Melissa Parks Suite 843\nWest Suzanne, OH 98208",
     "job": "Accountant, chartered certified",
     "score": 0.3899413405342961
   }
 }

From the json structure above i can draw that for every user





