import re

note = "award: Nobel Peace Prize"
position = note.find("Nobel")
word = note[position:position+5]

five_digit_zip = "98101"
nine_digit_zip = "98101-0003"
phone_number = "234-567-8901"
five_digit_expression = r"\d{3}+"
print(re.search(five_digit_expression, five_digit_zip))


def convertm_km (x): 
    print("The conversion in Km is:")
    return x *1.609344
    

