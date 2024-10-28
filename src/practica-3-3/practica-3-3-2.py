#!/usr/bin/env python3

# ───────────────────────────────────────────────────────────────────────────────────────────────────

# Get unique students in primary and secundary
def get_unique_students(primary_students: list, secondary_students: list):
    print("──────────────────────────────────────────────────────────────────")
    print("        GET UNIQUE FIRST NAME OF PRIMARY AND SECUNDARY")
    print("──────────────────────────────────────────────────────────────────")

    students = primary_students + secondary_students
    unique_students = []
    for student in students:
        if student not in unique_students:
            unique_students.append(student)

    unique_students = tuple(unique_students)
    for u_student in unique_students:
        print(f"- {u_student}")

# Get repeated students in primary and secundary
def repeated_students(primary_students: list, secondary_students: list):
    print("──────────────────────────────────────────────────────────────────")
    print("        GET UNIQUE FIRST NAME OF PRIMARY AND SECUNDARY")
    print("──────────────────────────────────────────────────────────────────")

    students = primary_students + secondary_students
    repeated_students = []
    for student in students:
        if student not in repeated_students:
            if students.count(student) > 1:
                repeated_students.append(student)

    repeated_students = tuple(repeated_students)
    for r_student in repeated_students:
        print(f"- {r_student}")

def unique_primary_students_not_in_secundary(primary_students: list, secondary_students: list):
    print("──────────────────────────────────────────────────────────────────")
    print("      GET UNIQUE PRIMARY STUDENTS NOT REPEATED IN SECUNDARY")
    print("──────────────────────────────────────────────────────────────────")

    # Get unique primary students not repeated in secundary
    primary_students = list(primary_students)
    secondary_students = list(secondary_students)
    new_primary_students = primary_students.copy()

    for p_student in primary_students:
        for s_student in secondary_students:
            if p_student == s_student:
                new_primary_students.remove(p_student)

    # Remove duplicate primary students
    unique_students = []
    for student in new_primary_students:
        if student not in unique_students:
            unique_students.append(student)


    new_primary_students = tuple(new_primary_students)
    if new_primary_students:
        for u_p_student in new_primary_students:
            print(f"- {u_p_student}")
    else:
        print("- There is no unique primary students not repeated in secundary.")

# Show if all the primary students name are included in secondary
def show_if_p_students_are_in_s_students(primary_students: list, secondary_students: list):
    print("──────────────────────────────────────────────────────────────────")
    print("    SHOW IF ALL THE PRIMARY STUDENTS ARE INCLUDED IN SECUNDARY")
    print("──────────────────────────────────────────────────────────────────")
    all_included = True
    for p_student in primary_students:
        if p_student not in secondary_students:
            all_included = False
            break

    if all_included:
        print("- [+] All primary students are included in secondary")
    else:
        print("- [-] All primary students are not included in secondary")

# ───────────────────────────────────────────────────────────────────────────────────────────────────

# Get primary students
def input_primary_students() -> list:
    input_status = True
    primary_students = []

    print("Introduce the first name of your primary students (finish with 'x'):")

    while input_status:
        first_name = input("[+] First name: ").strip().lower()

        if first_name.replace(' ', '') == 'x':
            input_status = False
            print()
        else:
            primary_students.append(first_name.title())

    primary_students = tuple(primary_students)
    return primary_students

# Get secondary students
def input_secondary_students() -> list:
    input_status = True
    secondary_students = []

    print("Introduce the first name of your secondary students (finish with 'x'):")

    while input_status:
        first_name = input("[+] First name: ").strip().lower()
        if first_name.replace(' ', '') == 'x':
            input_status = False
            print()
        else:
            secondary_students.append(first_name.title())

    secondary_students = tuple(secondary_students)
    return secondary_students

# ───────────────────────────────────────────────────────────────────────────────────────────────────

# Main function
def main():
    primary_students = input_primary_students()
    secondary_students = input_secondary_students()

    get_unique_students(primary_students, secondary_students)
    repeated_students(primary_students, secondary_students)
    unique_primary_students_not_in_secundary(primary_students, secondary_students)
    show_if_p_students_are_in_s_students(primary_students, secondary_students)


# Program starts
if __name__ == '__main__':
    main()