#!/usr/bin/env python3

# Check age and convert to number
def check_age(age: str) -> int:
    """Check AGE returns the age converted to number"""
    try:
        age = int(age)
        return age
    except:
        print("[-] ERROR: You haven't introduced a correct age format.")
        exit()

# Check sex of the person
def check_sex(sex: str) -> str:
    sex = sex.strip().replace(' ', '').lower()
    if sex == "f" or sex == "female" or sex == "m" or sex == "mujer":
        sex = "Female"
        return sex
    elif sex == "m" or sex == "male" or sex == "h" or sex == "hombre":
        sex = "Male"
        return sex
    else:
        print("[-] ERROR: You haven't introduced a correct sex format.")
        exit()

# Check phone number of the person:
def check_phone(phone: str) -> str:
    phone = phone.strip().replace(' ', '')
    if len(phone) > 6 and len(phone) < 15:
        return phone
    else:
        print(f"[-] ERROR: You have introduced an incorrect phone number length.")
        exit()

# Check email of the user:
def check_mail(mail: str) -> str:
    try:
        if mail.find("@") == -1:
            raise TypeError
        else:
            at = mail.split("@")[1]
            if at.find(".") == -1:
                raise NameError
            else:
                return mail
        
    except NameError:
        print("[-] ERROR: You haven't introduced a domain!")
        exit()
    except TypeError:
        print("[-] ERROR: You haven't introduced a correct email format.")
        exit()

# Main Function
def main():

    # Start empty person dict
    person = {}

    # Name of the person
    name = input("What's your name: ")
    person["name"] = name
    print(person)

    # Age of the person
    age = check_age(input("What's your age: "))
    person["age"] = age
    print(person)

    # Sex of the person
    sex = check_sex(input("What's your sex (female/male): "))
    person["sex"] = sex
    print(person)

    # Phone number of the person
    phone = check_phone(input("What's your phone number: "))
    person["phone"] = phone
    print(person)

    # Mail of the person
    mail = check_mail(input("What's your mail: "))
    person["mail"] = mail
    print(person)


# Start Program
if __name__ == '__main__':
    main()