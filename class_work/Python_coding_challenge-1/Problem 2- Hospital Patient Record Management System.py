# Problem 2: Hospital Patient Record Management System
# Problem Statement
# A hospital maintains patient details in a file named patients.txt.
# Sample Input/Data (patients.txt)
# P101,Anuj,Normal
# P102,Rahul,Critical
# P103,Priya,Stable
# P104,Neha,Critical
# P105,Amit,Stable
# P106,Sneha,Normal
# P107,Karan,Critical
# P108,Pooja,Stable
# P109,Rohit,Normal
# P110,Anjali,Stable
# Tasks
# 1. Display all patient records.
# 2. Display critical patients.
# 3. Count patients under each status.
# 4. Search patient details using Patient ID.
# 5. Save critical patient records to critical_patients.txt.
# Sample Output
# Critical Patients:
# Rahul
# Neha
# Karan
# Patient Count:
# Normal : 3
# Stable : 4
# Critical : 3
# Patient Found:
# P104,Neha,Critical
# Critical Patient Report Generated Successfully.


patient_record = 
{"P102":"Anuj":"Normal","P102":"Rahul":"Critical","P103":"Neha":"Critical","P105":"Sneha":"Normal","P107":"Karan":"Critical","P108":"Pooja":"Stable","P109":"Rohit":"Normal","P110":"Anjali":"Stable"}

print("all patients records are: "patient_record)

normal_patients == 0
critical_patients == 0
stable_patients == 0
for items in patient_record:
    if patient_record.values == normal:
        normal_patient += 1
    elif patient_record.values == critical:
        critical_patient += 1
    elif patient_record.values == stable
        stable_patient += 1
    else:
        pass
print("normal patients: ",normal_patient)
print("critical patients: ",critical_patient)
print("stable patients: ",stable_patient)

#Search patient details using Patient ID. 
