#!/usr/bin/env python3

months = {
  "01": "January",
  "02": "February",
  "03": "March",
  "04": "April",
  "05": "May",
  "06": "June",
  "07": "July",
  "08": "August",
  "09": "September",
  "10": "October",
  "11": "November",
  "12": "December"
}

# Check Date Input
def check_date(date: str) -> (list | bool):
    try:
        date = date.split("/")

        # If you haven't introduced 3 values
        if len(date) != 3:
            return False

        # If you have introduced 3 values
        else:
            # Check if each value introduced is a nuumber or not
            for i in (date):
                i = int(i)

            # Check if corrected format for each date value
            dd = date[0]
            mm = date[1]
            aaaa = date[2]

            if len(dd) == 2 and len(mm) == 2 and len(aaaa) == 4:
                mm = months.get(mm)
                return (dd, mm, aaaa)
            else:
                return False
    except:
        return False

def main():
    date_input = input("Introduce a date in this format (dd/mm/aaaa): ")
    date = check_date(date_input)
    if date:
        print(f"{date[1]} {date[0]}, {date[2]}")
    else:
        print("[-] ERROR: You haven't introduced a correct date format.")

if __name__ == '__main__':
    main()