# Project 2: Expense Tracker
### DecodeLabs Intern Training Track (Batch 2026)

A straightforward, user-friendly Python command-line application designed to continuously track financial transactions and maintain a running balance in real-time.

---

## << Project Overview >>

The Expense Tracker simulates a basic cash register or a real-time ledger engine. Instead of taking a single number, calculating it, and immediately closing down, this program creates a continuous data loop. It accepts user transaction inputs one after another, transforms raw keyboard text into true mathematical decimals, and continuously adds them to an accumulated grand total. The program runs indefinitely until the operator enters the designated command to safely exit and view a final financial summary report.

---

## >> Key Features <<

* **Continuous Accumulation:** Dynamically tracks and updates a single grand total across multiple entries without losing data.
* **Interactive Command-Line Interface:** Runs on a continuous user input loop, creating a smooth and interactive experience in the terminal.
* **Safe Exit Trigger (Sentinel Control):** Includes an explicit keyword trigger (`exit`) that hands shutdown authority over to the user, closing the loop cleanly.
* **Final Financial Reporting:** Automatically prints a structured summary screen detailing the final total expenditure as soon as tracking concludes.

---

## <<Technologies & Concepts Used >>

This application is built natively in **Python 3** and showcases four core backend programming building blocks:

* **Variables & State Management:** Used to create the memory variable (`total_spent`). By initializing it outside the loop, the application safely remembers data over time.
* **While Loops (`while True`):** Used to construct an ongoing execution pathway so the user can keep inputting costs indefinitely.
* **Data Type Conversion (`float()`):** Converts raw text entries from the keyboard (strings) into true decimal numbers so the computer can perform accurate financial math.
* **Conditional Logic (`if` statements):** Evaluates user inputs in real-time to check if the user wants to keep calculating or break out of the script.

---

##  >> Real-Life Advantages of This Approach <<

* **Prevents Memory Amnesia (State Preservation):** By carefully managing where variables are placed, the program doesn't clear out its history after every turn. In real-life applications like banking, this logic ensures your bank account doesn't reset to $0 every time you swipe a card.
* **Scalable Data Ingest:** The script isn't hardcoded to only accept 3 or 5 transactions. It can seamlessly ingest 10 entries or 10,000 entries in a single session without breaking.
* **Data Transformation Guardrail:** It ensures the application performs true financial math ($100 + $50 = $150$) instead of experiencing a "string addition catastrophe" where text values just stitch together words incorrectly ($'100' + '50' = '10050'$).
* **Foundation for Robust Backend Logic:** Keeping the code clean and well-structured makes it incredibly easy to add security shields later on—such as error handlers (`try-except`) that prevent accidental letter typos from crashing the software system.

---
*Developed as part of the DecodeLabs Quality Verification Standards.*
