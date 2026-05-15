import os
os.system('color')  # 啟動 Windows 顏色支援

# 定義顏色與樣式變數
BOLD = '\033[1m'      # 加粗
GREEN = '\033[92m'     # 綠色 (適合 "Add" 或 "Success")
YELLOW = '\033[93m'    # 黃色 (適合 "Menu" 或 "Warning")
RED = '\033[91m'       # 紅色 (適合 "Delete" 或 "Exit")
CYAN = '\033[96m'      # 青色 (適合選單標題)
RESET = '\033[0m'      # 重置 (一定要加，不然之後的字都會變色)

ToDo_List = []

while True:
    print(" ")
    print(f"\n{BOLD}{CYAN}=== To Do List Menu ==={RESET}")
    print(" ")
    print("  1. Add a To-Do Item")
    print("  2. View To-Do Items")
    print("  3. Delete a To-Do Item")
    print("  4. Exit the App")
    print(" ")
    print(f"{BOLD}{CYAN}={RESET}"*23)
    print("  " * 10)

    while True:
        try:
            choice = int(
                input("Please enter a number to select the function:"))
            if choice > 4 or choice < 1:
                print(
                    f"{BOLD}{RED}Invalid input, please enter a number from 1 to 4{RESET}")
                continue
            break
        except ValueError:
            print(f"{BOLD}{RED}Please enter a number{RESET}")

    if choice == 1:
        print(f"\nSelected function: {choice}.Add a To-Do Item")
        while True:
            new_todo = input("Please enter a to-do item:")
            new_todo = new_todo.strip()
            if new_todo:
                ToDo_List.append(new_todo)
                print(
                    f"{BOLD}{GREEN}[{new_todo}] has been added to the list.{RESET}")
                break
            else:
                print(f"{BOLD}{RED}Cannot add an empty item{RESET}")
    elif choice == 2:
        if ToDo_List:
            list_num = 0
            for todo in ToDo_List:
                list_num += 1
                print(f"{list_num}.{BOLD}{GREEN}{todo}{RESET}")
        else:
            print(f"\n{BOLD}{RED}Your list is empty.{RESET}")

    elif choice == 3:
        print(f"\nSelected function: 3.Delete a To-Do Item")
        if not ToDo_List:
            print(f"{BOLD}{RED}Your list is empty. Nothing to delete.{RESET}")
            continue

        while True:
            try:
                Delete_number = int(
                    input(f"{BOLD}{YELLOW}Enter the item number to delete{RESET}(Enter 0 to exit):"))
                if Delete_number == 0:
                    break
                elif Delete_number > len(ToDo_List) or Delete_number < 0:
                    print(f"{BOLD}{RED}Item number not found.{RESET}")
                else:
                    removed_item = ToDo_List.pop(Delete_number - 1)
                    print(
                        f"{BOLD}{GREEN}Item {removed_item} has been removed{RESET}")
                    break

            except ValueError:
                print(f"{BOLD}{RED}Please enter a number{RESET}")

    elif choice == 4:
        print(f"\n{BOLD}{YELLOW}Exit the To-Do List{RESET}")
        print(f"{BOLD}{YELLOW}Goodbye!{RESET}")
        break
