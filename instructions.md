Write some code that randomly assigns a user_id to one of N groups based on a percentage, and remembers which group a user is in after initial assignment. 
Your code should handle assigning a group to new users and returning the assigned group for existing users. 

You may use any language you feel most comfortable with.
Please include test cases.

The desired groups and their percentages are given as JSON in the attached file. 

userGroupPercentages.json
{
    "groupA": 0.4,
    "groupB": 0.1,
    "groupC": 0.5
}

For example, if we have 10 users, each with a string user_id, you should see something approximately like the following output. 
getUserGroup("user1") --> "groupC"
getUserGroup("user2") --> "groupA"
getUserGroup("user3") --> "groupB"
getUserGroup("user4") --> "groupC"
getUserGroup("user5") --> "groupC"
getUserGroup("user6") --> "groupA"
getUserGroup("user7") --> "groupA"
getUserGroup("user8") --> "groupC"
getUserGroup("user9") --> "groupA"
getUserGroup("user10") --> "groupC"

Notice there are four users in "groupA", one user in "groupB", and five users in group "groupC".
The distribution might not match exactly in some cases, but it should be as close as possible.

If you call the function again with the same user id, you should receive the same group value each time
getUserGroup("user9") --> "groupA"
getUserGroup("user9") --> "groupA"
getUserGroup("user9") --> "groupA"

Feel free to reach out to us with any questions. Happy coding!
