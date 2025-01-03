from rich.table import Table
from rich.console import Console

expenses = []

def table_creation():
  console = Console()
  table = Table(title='Expense Table')

  table.add_column('Type of Expense', justify="left", style="cyan")
  table.add_column('Amount Spent', justify="center", style="magenta")
  table.add_column('Note', justify="left", style="green")

  for expense in expenses:
    table.add_row(expense['type'], str(expense['cost']), expense['note'])

  console.print(table)

def expense_splitter():
    
    print('Welcome to the Expense Splitter.')
    a = True
    while a:
        print('1. Add an Expense\n2. View an Expense\n3. Edit an Expense\n4. Remove an Expense\n5. Split Expenses\n6. Exit')
        inp = input('Enter the choice(1/2/3/4/5): ')
        if inp == '1':
            type = input('Enter the type of expense: ').upper()
            cost = int(input('Enter the amount spent: '))
            note = input('Enter a note to describe the expense: ').lower()
            expenses.append({'type': type, 'cost': cost, 'note': note})
            print('Expense added successfully!')
        elif inp == '2':
            if len(expenses) == 0:
                print('There are no expenses to show.')
            else:
              table_creation()
        elif inp == '3':
            edit = input('Enter the expense to edit: ').upper()
            found = False
            for expense in expenses:
                if expense['type'] == edit:
                    expense['type'] = input('Enter the type of expense: ').upper()
                    expense['cost'] = int(input('Enter the amount spent: '))
                    expense['note'] = input('Enter a note to describe the expense: ').lower()
                    print('Expense edited successfully!')

                    table_creation()

                    found = True
                    break
            if not found:
                print('The item was not found.')
        elif inp == '4':
            remove = input('Enter the expense to remove: ').upper()
            found = False
            for exp in expenses:
                if exp['type'] == remove:
                    expenses.remove(exp)
                    print('Expense removed successfully!')

                    table_creation()

                    found = True
                    break
            if not found:
                print('The item was not found.')
        elif inp == '5':
            total = sum(ex['cost'] for ex in expenses)
            print(f'Total Expenses: ${total}')
            number = int(input('Enter the number of persons to split: '))
            print(f'Each person should pay ${total / number:.2f}')
        elif inp == '6':
            print('Thanks for using our Expense Splitter!')
            a = False
        else:
            print('Enter a valid choice.')

expense_splitter()
