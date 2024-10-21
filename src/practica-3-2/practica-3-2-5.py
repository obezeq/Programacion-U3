#!/usr/bin/env python3

# Function to get each credit for each subject.
def get_credits(subjects: list) -> int:
    try:
        total = 0
        for s in subjects:
            credits = subjects[s]
            total += credits
            print(f"- {s} has {credits} credits.")

        return total
        
    except Exception as e:
        print(f"[-] ERROR: {e}")

# Main Function
def main():
    subjects = {
        "Matemáticas": 6,
        "Física": 4,
        "Química": 5,
    }

    total_credits = get_credits(subjects)
    print(f"[+] The total of credits for all your credits is {total_credits}")

# Start Program
if __name__ == '__main__':
    main()