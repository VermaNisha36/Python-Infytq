#Care hospital wants to know the medical speciality visited by the maximum number of patients. Assume that the patient id of the patient along with the medical speciality visited by the patient is stored in a list. The details of the medical specialities are stored in a dictionary as follows:
{
"P":"Pediatrics",
"O":"Orthopedics",
"E":"ENT"
} 
#Write a function to find the medical speciality visited by the maximum number of patients and return the name of the speciality.
#Note: Assume that there is always only one medical speciality which is visited by maximum number of patients.
#Perform case sensitive string comparison wherever necessary.
#Sample Input: [101,P,102,O,302,P,305,P]
#Expected Output: Pediatrics

#PROGRAM

def max_visited_speciality(patient_medical_speciality_list,medical_speciality):
    # write your logic here
    count_P=patient_medical_speciality_list.count("P")
    count_O=patient_medical_speciality_list.count("O")
    count_E=patient_medical_speciality_list.count("E")
    if count_P>count_E and count_P>count_O:
        speciality=medical_speciality["P"]
    elif count_E>count_P and count_E>count_O:
        speciality=medical_speciality["E"]
    else:
        speciality=medical_speciality["O"]
    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
