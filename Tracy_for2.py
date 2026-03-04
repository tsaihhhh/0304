#
# Tracy, 2026/03/04
# Tracy_for2.py
# To test for loop and print each items
#

# range() generates a sequence of numbers
# range(start, stop, step)  — stop is exclusive
print("Sales Report — Q1 Weeks")
for week in range(1, 53):          # weeks 1 through 12
    weekly_target = 50_000
    print(f"  Week {week:>2}: Target = ${weekly_target:,}")