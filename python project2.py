def main():
    print("--- DecodeLabs Expense Tracker ---")

#1.Initial spent is = 0  
    total_spent = 0.0
    
# 2. CONTINUOUS LOOP: Keep running until the user explicitly wants to stop.
    while True:
        user_input = input("Enter an expense amount (or type 'exit' to stop): ")
        
# 3. EXIT TRIGGER: If the user types 'exit', immediately break out of the loop.
        if user_input == "exit":
            break
            
# 4. TRANSFORMATION: Converting the text input string into float.
        expense = float(user_input)
        
# 5. ACCUMULATION: Take the old total, add the new expense, and update our memory variable.
        total_spent = total_spent + expense
        
        print("Current Total Spent: Rs." + str(total_spent))

    # 6. Final Result:
    print("\n---------------------------------")
    print("FINAL REPORT: Total Spent = Rs." + str(total_spent))
    print("---------------------------------")

if __name__ == "__main__":
    main()
