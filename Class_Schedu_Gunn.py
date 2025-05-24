
print("Course information")


room_num = { 
    "CS101": "3004",
     "CS102": "4501",
     "CS103": "6755",
     "NT110": "1244",
     "CM241": "1411"
}

room_prof = { 
    "CS101": "Haynes",
     "CS102": "Alvarado",
     "CS103": "Rich",
     "NT110": "Burke",
     "CM241": "Lee"
}


room_time = { 
    "CS101": "8:00am",
     "CS102": "9:00am",
     "CS103": "10:00am",
     "NT110": "11:00am",
     "CM241": "1:00pm"
}
num = input("Please enter course number: ")
print(f"Room number: {room_num[num]} \nProfessor: {room_prof[num]} \nClass Time: {room_time[num]}")