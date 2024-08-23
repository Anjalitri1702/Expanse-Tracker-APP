from expense import Expense
from datetime import datetime
import calendar


def main():
    print(f"running expense tracker 💰")
    budget = float(input("Enter your monthly budget: ₹"))
    expense_file_path="expenses.csv"
    
    # Get the remaining days in the current month
    remaining_days = get_remaining_days_in_month()
    print(f"Remaining days in the current month: {remaining_days} 📅")
    
    
    # get user input for expense
     #expense=get_user_expense()
    
    
    # Write their response into file
     #save_expense_to_file(expense,expense_file_path)
    
    # Read file and summarize expense
    summarize_expense(expense_file_path,budget)

def get_remaining_days_in_month():
    # Get the current date
    today = datetime.today()
    current_year = today.year
    current_month = today.month
    
    # Get the total number of days in the current month
    _, total_days_in_month = calendar.monthrange(current_year, current_month)
    
    # Calculate the remaining days
    remaining_days = total_days_in_month - today.day
    
    return remaining_days

def get_user_expense():
    print(f"Getting user expense") 
    expense_name=input("Enter expense name:")
    expense_amount=float(input("Enter expense amount :"))
    expense_categories=[
       "Food 🍲", 
        "Transportation 🚗",
        "Utilities 💡",
        "Personal expenses 🛍️",
        "Debt 💳",
        "Health Care 🏥",
        "Mortgage or Rent 🏠",
        "Miscellaneous expenses 🛠️",
        "Debt or Student Loan payment 🎓"
    ]
    while True:
       print("Select a category:")
       for i, category_name in enumerate(expense_categories):
           print(f"  {i + 1}. {category_name}")
    
       try:
          value_range = f"[1-{len(expense_categories)}]"
          selected_index = int(input(f"Enter a category number {value_range}:")) - 1
        
          if selected_index in range(len(expense_categories)):
            new_expense=Expense(
                name=expense_name,
                category=expense_categories[selected_index],
                amount=expense_amount
            )
            return new_expense
        
          else:
            print("Invalid category. Please try again!")
       except ValueError:
        print("Invalid input. Please enter a number.")
    
   
  
    
    
    
def save_expense_to_file(expense:Expense,expense_file_path):
    print(f"Saving user expense:{expense} to {expense_file_path}")
    with open (expense_file_path,"a")as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")

def summarize_expense(expense_file_path,budget):
    print(f"Summarizing user expense")
    expenses=[]
    
    with open (expense_file_path,"r")as f:
        lines=f.readlines()
        for line in lines:
            expense_name,expense_amount,expense_category=line.strip().split(",")
            line_expense=Expense(
                name=expense_name,
                amount=float(expense_amount),
                category=expense_category,
            )
            expenses.append(line_expense)
    
    amount_by_category={}
    for expense in expenses:
        key=expense.category
        if key in amount_by_category:
            amount_by_category[key]+=expense.amount
        else:
            amount_by_category[key]=expense.amount
             
    print("Expense_by_category:")
    for key, amount in amount_by_category.items():
        print(f"  {key} ₹{amount:.2f}") 
               
    total_Spent=sum([x.amount for x in expenses])
    print(f"you've spent: ₹{total_Spent:.2f} this month !")  
    
    remaining_budget=budget-total_Spent  
    if remaining_budget <budget:
        print(f"Budget Exceeded! You have spent ₹{abs(remaining_budget):.2f} more than your monthly budget.")
    else:
        print(f"Budget Remaining: ₹{remaining_budget:.2f}")
        
 
            
if __name__ == "__main__":
    main()
