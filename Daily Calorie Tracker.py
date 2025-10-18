
# Mini Project Assignment: Daily Calorie Tracker CLI
# Assignment Number: 01
# Assignment Title: Programming for Problem Solving using Python 
# Programme: B.Tech CSE CORE
# Section: A
# Sem: 01
# Roll No: 2501010169
# Name: Md Shahjad





from datetime import datetime

def print_welcome():
    print("=======================================")
    print("   Daily Calorie Tracker (Simple CLI)  ")
    print("=======================================")
    print("Quickly log meals and calories, see totals, and save a session.\n")

def get_int(prompt, allow_zero=False):
    # helper to get integer input safely
    while True:
        val = input(prompt).strip()
        try:
            n = int(val)
            if not allow_zero and n <= 0:
                print("Please enter a number greater than 0.")
                continue
            return n
        except ValueError:
            print("That's not a valid integer. Try again.")

def get_float(prompt):
    while True:
        val = input(prompt).strip()
        try:
            return float(val)
        except ValueError:
            print("Please enter a valid number (e.g., 350 or 350.5).")

def collect_meals():
    meals = []
    calories = []
    num = get_int("How many meals do you want to enter? ")
    for i in range(1, num+1):
        name = input(f"Enter meal #{i} name (e.g. Breakfast): ").strip()
        if name == "":
            name = f"Meal{i}"
        cal = get_float(f"Enter calories for '{name}': ")
        meals.append(name)
        calories.append(cal)
    return meals, calories

def compute_stats(calories):
    total = sum(calories)
    avg = total / len(calories) if calories else 0
    return total, avg

def print_report(meals, calories, total, avg, limit):
    print("\n----- Today's Calorie Summary -----")
    print(f"{'Meal Name':<15}\tCalories")
    print("-" * 34)
    for m, c in zip(meals, calories):
        # align to look hand-typed
        print(f"{m:<15}\t{c}")
    print("\n")
    print(f"{'Total:':<15}\t{total}")
    print(f"{'Average:':<15}\t{avg:.2f}\n")
    if limit is not None:
        if total > limit:
            print("⚠️  Warning: You have exceeded your daily calorie limit!")
            diff = total - limit
            print(f"You are over by {diff:.1f} calories.")
        else:
            print("✅ Good job — you're within your daily calorie limit.")
            spare = limit - total
            print(f"You have {spare:.1f} calories left for the day.")
    print("-----------------------------------\n")

def save_session(meals, calories, total, avg, limit):
    want = input("Do you want to save this session to a file? (y/n): ").strip().lower()
    if want not in ('y','yes'):
        print("Session not saved.")
        return None
    filename = input("Enter filename (or press Enter to use 'calorie_log.txt'): ").strip()
    if filename == "":
        filename = "calorie_log.txt"
    try:
        with open(filename, "a") as f:
            f.write("==== Calorie Session ====\n")
            f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            for m, c in zip(meals, calories):
                f.write(f"{m}\t{c}\n")
            f.write(f"Total:\t{total}\n")
            f.write(f"Average:\t{avg:.2f}\n")
            if limit is not None:
                status = "Exceeded" if total > limit else "Within limit"
                f.write(f"Limit:\t{limit}\n")
                f.write(f"Status:\t{status}\n")
            f.write("\n")
        print(f"Session saved to {filename}")
        return filename
    except Exception as e:
        print("Error saving file:", e)
        return None

def main():
    print_welcome()
    meals, calories = collect_meals()
    total, avg = compute_stats(calories)
    # ask for daily limit
    use_limit = input("Do you want to set a daily calorie limit? (y/n): ").strip().lower()
    if use_limit in ('y','yes'):
        limit = get_float("Enter your daily calorie limit: ")
    else:
        limit = None

    print_report(meals, calories, total, avg, limit)
    saved_file = save_session(meals, calories, total, avg, limit)

    # friendly note (human-like)
    print("\nNote: I copied simple formatting so it's easy to read. Replace the header name/date before submission.")
    print("Thanks for using Daily Calorie Tracker — have a healthy day!")

if __name__ == "__main__":
    main()
