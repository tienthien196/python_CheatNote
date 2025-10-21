# This dataset represents three students.

# The features are: [Hours Studied, Hours of Sleep]

# The label is the last element: "pass" or "fail"


student_data = [

    [8, 7, "pass"],  # Student 1: 8 hrs study, 7 hrs sleep, passed.

    [4, 5, "fail"],  # Student 2: 4 hrs study, 5 hrs sleep, failed.

    [7, 8, "pass"]   # Student 3: 7 hrs study, 8 hrs sleep, passed.

]

l = [3,54,6,5,4]
# We can access the data for the first student (at index 0).

first_student = student_data[0]


# Now we can separate the features from the label for that student.

# In Python, slicing with [:-1] means "get everything except the last element".

student_features = first_student[:-1]


# Slicing with [-1] means "get the very last element".

student_label = first_student[-1]


print(f"Data for first student: {first_student}")

print(f"Features: {student_features}")

print(f"Label: {student_label}")