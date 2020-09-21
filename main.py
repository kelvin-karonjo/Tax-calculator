def tax_calculator(): 
   dependency_exemption=3000
   gross_income = float(input('What is your gross_income in KSH: '))

   children = float(input('number of children: '))
   taxpayers_net_income = (gross_income- children*dependency_exemption)


   print('your net income is KSH: ',taxpayers_net_income)

   if  (taxpayers_net_income >= 0) and (taxpayers_net_income <= 50000):
            tax_due = (0.15*taxpayers_net_income)
            print('Your due tax is KSH: ',tax_due)
   elif (taxpayers_net_income >= 50001) and (taxpayers_net_income <= 100000):
            tax_due = (0.20 *taxpayers_net_income)
            print('Your due tax is KSH: ',tax_due)
   else: 
            tax_due = (0.30 *taxpayers_net_income)
            print('Your due tax is KSH: ',tax_due)         
          
tax_calculator()