"""
DecodeLabs Industrial Training Kit
Project 1: The To-Do List Engine (Backend Data Management)
Batch: 2026
"""

# STORAGE: Initialize the volatile container in dynamic memory (The Heap)
# The list acts as a Full Database Table, holding individual row references.
my_tasks = []
def display_menu():
    print("\n" + "="*40)
    print("      DECODELABS TO-DO ENGINE v1.1      ")
    print("="*40)
    print("1. [PROCESS] Insert New Task Row")
    print("2. [DISPLAY] Execute Read Operation")
    print("3. [SYSTEM]  Shutdown Engine (Clear RAM)")
    print("="*40)
def main():
    while True:
        display_menu()
        choice = input("Select an operation system code (1-3): ").strip()

        if choice == '1':
            print("\n--- OPERATION: INSERT INTO TABLE ---")
            task_description = input("Enter the task description: ").strip()
            
            if not task_description:
                print("Validation Error: Task description cannot be empty.")
                continue

            # Logic: Use a dictionary to define a task row (Schema: ID, Description, Status)
            # The row ID acts as an auto-incrementing Primary Key.
            task_id = len(my_tasks) + 1
            task_row = {
                "id": task_id,
                "description": task_description,
                "status": "Pending"
            }

            # Amortized O(1) Append operation to push the pointer to the Heap array
            my_tasks.append(task_row)
            print(f"Success: Task ID {task_id} successfully committed to volatile storage.")

        elif choice == '2':
            print("\n--- OPERATION: VIEW DATA SYSTEM ---")
            
            # Iterator Protocol: Creates a temporary view of the system's state
            if not my_tasks:
                print("System State Notice: The database table container is currently empty.")
            else:
                print(f"{'ID':<5} | {'TASK DESCRIPTION':<35} | {'STATUS':<10}")
                print("-" * 56)
                for row in my_tasks:
                    print(f"{row['id']:<5} | {row['description']:<35} | {row['status']:<10}")
                print(f"\n[Total Records Extracted: {len(my_tasks)}]")

        elif choice == '3':
            print("\nShutting down backend engine...")
            print("System Alert: Volatile memory container (RAM) flushed. Data has cleared.")
            break

        else:
            print("\nExecution Error: Invalid instruction. Please check your logic skeleton.")

if __name__ == "__main__":
    main()
