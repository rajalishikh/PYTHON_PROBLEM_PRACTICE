# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
list_of_subject=["python","jaa",'c++',"jaascript","jaa","python","c++","c"]
list_of_subject=list(set(list_of_subject)) 
print("Total class room need for students are ",len(list_of_subject))