print('Welcome to the budget calculator')
print('----------------------------------------------')
print('Income')
income = float(input('Enter your monthly post-tax income (CAD):'))
additional_income = float(input('Enter any additional income(CAD):'))

total_income = income + additional_income

print('Total income will be:' + str(total_income))
print('----------------------------------------------')
print('Expenses')

def gatherExpenses():
    mortgage = float(input('Enter your monthly mortgage expense (CAD):'))
    utilities = float(input('Enter your monthly utilities expense (CAD):'))
    grocery = float(input('Enter your monthly grocery expense (CAD):'))
    misc = float(input('Enter your monthly misc. expense (CAD):'))
    electric = float(input('Enter your monthly electric expense (CAD):'))
    water = float(input('Enter your monthly water expense (CAD):'))
    gas = float(input('Enter your monthly gas expense (CAD):'))
    holliday = float(input('Enter your monthly holliday expense (CAD):'))
    insurance = float(input('Enter your monthly insurance expense (CAD):'))
    maintenance = float(input('Enter your monthly maintenance expense (CAD):'))
    property_tax = float(input('Enter your monthly property tax expense (CAD):'))
    communication_bundle = float(input('Enter your monthly communication bundle expense (CAD):'))
    clothes = float(input('Enter your monthly clothes expense (CAD):'))
    total_expenses = mortgage + utilities + grocery + misc + electric + water + gas + holliday + insurance + maintenance + property_tax + communication_bundle + clothes 
    
    return total_expenses

total_expenses = gatherExpenses()
print('Total expenses will be:' + str(total_expenses))
print('----------------------------------------------')
margin = total_income - total_expenses

if margin >= 0:
    print('Total surplus will be:' + str(margin))
else: 
    print('You will come up $' + str(margin) + 'negative!')
    
print('End')        
    
    
    
    
    
    
    
    
    
    
