###############################################################################################################################################
#   CSE 231
#   Project 7
#
#   Algorithm
#
#   function open_file()
#        prompt for a file_name
#        while loop to repeatedly prompt for a file_name:
#           use try-except method to prevent the program from running errors
#           try :
#               break from the loop if a file is successfully opened
#           except:
#               print Invalid filename  and prompt for a file name
#               go back to the while loop to start from the beginning
#              
#        return file_pointer
#
#
#   function convert_data(lst):
#       make a new_lst
#        
#        for loop through the list:
#            remove commas from data
#            append the updated data to new list
#            
#        for loop through the new_lst:
#            replace all empty data or datat with period with 0
#            assign 3 items in a list as int
#            assign the 4th item as float
#            
#        return new_lst
#
#
#   function read_file(fp)
#
#        create reader file
#        skip the first 3 rows
#        create master_list = []
#        create residential_list, rsd_lst
#        create commercial_list,cm_lst
#        create ind_lst, industrial_list
#        create tran_lst, transportation_list
#        
#        for loop through reader file:
#            
#            create a list with 4 elements that need to be called by convert_data function
#            assign the returned list by the function from convert_data function
#            
#        for loop through assigned list:
#            append the items from the assigned list to real list (For ex: residential_list) as a list of tuple
#        
#        do the same method for commercial_list, industrial_list and transportation_list
#        
#        append all these lists of tuples to master_list
#
#
#   function get_year_or_state_data(L, index, value)
#
#           create a new_lst []
#        
#           for loop through the list from the parameter:
#            
#            if index is 0:
#                if i[0] == values:
#                    
#                    append all the elements of that tuple to new_lst
#                    
#            elif index is 1:
#                if i[1] == value:
#                    
#                    append all the elements of that tuple to new_lst
#                    
#            return new_lst
#
#   
#   function display_year_or_state_data(L,index,title)
#
#            if index is  0 :
#               print the format directed by the project
#            
#           for loop through the list from the parameter:
#            
#               print the format directed by the project in remove the element that represents state
#        
#            else:
#            
#               print the format directed by the project
#            
#               for loop through the list from the parameter:
#            
#                   print the format directed by the project and remove the element that represents year 
#   
#           
#   function get_totals(master_list):
#
#           create total_list[]
#    
#           create variables to store total values of total revenue, sales, customer,and price
#    
#           for loop through the Residential list of tuple :
#               add the values to the variables
#        
#           append the total variables to total_list[]
#    
#           repeat this for commercial list, industrial list and transportation_list
#    
#           append the total variables tot total_list[]
#
#
#   function display_totals(L):
#            print the headers directed by the project
#        
#        
#           create count = 0
#           for loop through the list from the parameter of the function:
#            
#            add 1 to count everytime i goes to next list
#            if count = 1 :
#                name = "Residential"
#            if count = 2:
#                name = "Commercial"
#            if count is 3 , then name is industrial
#            if count is 4, then name is transportation
#                
#                print the format directed by the project and insert name in the format(names changes when i goes to the next line)
#
#   function main():
#
#       print(BANNER) and print(MENU)
#       call open file and read_file()
#       assign the list returned by the read_file() function as master_list
#
#       prompt user to pick an option, assign that variable as option
#       
#       while option != 4:
#           while option != 1,2,3,4:
#               print ("Invalid"), print (Menu),prompt user to pick an option 
#               continue until the user types valid input
#
#           if option =1
#               prompt for category and convert it to title case
#               create a list of CATEGORIES, create a while loop until user types right category
#               create a while loop, for prompting the user which year to enter
#                   do try except method untile user types the right year
#
#               if category == "Residential"
#               print the header directed by the project
#               call get_year_or_state_data() function and assign the returned list as argument to the display_year_or_state_data() function
#               do the same for other categories
#
#           if option = 2
#               do the same method as option 1 but instead of year prompt for state
#               after printing all the revenue and sales, prompt the user if the user wants to plot the data
#               if yes, call the state_plots function with returned list and state as argument returned by the get_year_or_state_data() function 
#           if option = 3
#               call get_totals() function and assign the returned list as argument to the display_totals() function
#
#        print("Thank you for using this program!")
#
############################################################################################################################################################


import csv
import matplotlib.pyplot as plt


CATEGORIES = ["Residential", "Commercial", "Industrial", "Transportation"]
STATES = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

def open_file():
    ''' 
        prompt for a file_name
        while loop to repeatedly prompt for a file_name:
            use try-except method to prevent the program from running errors
            try :
                break from the loop if a file is successfully opened
            except:
                print Invalid filename  and prompt for a file name
                go back to the while loop to start from the beginning
                
        return file_pointer
    
    
    '''
    
    file_name = input("Enter filename: ")
    check = True
    
    while check == True:
        try:
            filepointer = open(file_name)
            break
        except FileNotFoundError:
            print("The file cannot be found! Please Try Again!!!")
            file_name = input("Enter filename: ")
            continue
    
    return filepointer

def convert_data(lst):
    ''' 
        make a new_lst
        
        for loop through the list:
            remove commas from data
            append the updated data to new list
            
        for loop through the new_lst:
            replace all empty data or datat with period with 0
            assign 3 items in a list as int
            assign the 4th item as float
            
        return new_lst

    
    '''
    
    new_lst = []
    for i in lst:
        
        i = i.replace(",", "")
        new_lst.append(i)
    
    for i in range(len(new_lst)):
        
        if new_lst[i] == "" or new_lst[i] == ".":
            new_lst[i] = 0
        if i < 3:
            new_lst[i] = int(new_lst[i])
        if i == 3:
            new_lst[i] = float(new_lst[i])
    
    return new_lst
       
     
   
    
def read_file(fp):
    ''' 
        create reader file
        skip the first 3 rows
        create master_list = []
        create residential_list, rsd_lst
        create commercial_list,cm_lst
        create ind_lst, industrial_list
        create tran_lst, transportation_list
        
        for loop through reader file:
            
            create a list with 4 elements that need to be called by convert_data function
            assign the returned list by the function from convert_data function
            
        for loop through assigned list:
            append the items from the assigned list to real list (For ex: residential_list) as a list of tuple
        
        do the same method for commercial_list, industrial_list and transportation_list
        
        append all these lists of tuples to master_list

    
    '''
    
    reader = csv.reader(fp)   
    fp.readline()
    fp.readline()
    fp.readline()
    master_list = []
    
    residential_list = []
    rsd_lst = []
    
    cm_lst = []
    commercial_list = []
    
    ind_lst = []
    industrial_list = []
    
    tran_lst = []
    transportation_list = []
    
    for line in reader:
        
        rd_lst = [line[3],line[4],line[5],line[6]]
        rsd_lst = convert_data(rd_lst)
        
        cmc_lst = [line[7],line[8],line[9],line[10]]
        cm_lst = convert_data(cmc_lst)
        
        in_lst = [line[11],line[12],line[13],line[14]]
        ind_lst = convert_data(in_lst)
        
        tr_lst = [line[15],line[16],line[17],line[18]]
        tran_lst = convert_data(tr_lst)
        
        
        for i in range(len(rsd_lst)):
            
            residential_list.append((int(line[0]),line[1], rsd_lst[0],rsd_lst[1], rsd_lst[2], rsd_lst[3]))
            break
        
        for j in range(len(cm_lst)):
            
            commercial_list.append((int(line[0]),line[1], cm_lst[0],cm_lst[1],cm_lst[2],cm_lst[3]))
            break
        
        for c in range(len(ind_lst)):
            
            industrial_list.append((int(line[0]),line[1],ind_lst[0],ind_lst[1],ind_lst[2],ind_lst[3]))
            break
        
        for w in range(len(tran_lst)):
            
            transportation_list.append((int(line[0]),line[1], tran_lst[0],tran_lst[1],tran_lst[2],tran_lst[3]))
            break
        
   
    master_list.append(residential_list)
    master_list.append(commercial_list)
    master_list.append(industrial_list)
    master_list.append(transportation_list)
    
        
    return(master_list)
        

def get_year_or_state_data(L, index, value):
    ''' 
    
        create a new_lst []
        
        for loop through the list from the parameter:
            
            if index is 0:
                if i[0] == values:
                    
                    append all the elements of that tuple to new_lst
                    
            elif index is 1:
                if i[1] == value:
                    
                    append all the elements of that tuple to new_lst
                    
        return new_lst
    
    '''
    
    new_lst = []
    
    for i in L:
        
        
    
        if index == 0:
            if i[0] == value:
                
                new_lst.append((i[0],i[1],i[2],i[3],i[4],i[5]))
                
        elif index == 1:
            
            if i[1] == value:
                
                new_lst.append((i[0],i[1],i[2],i[3],i[4],i[5]))
   
    
    return(new_lst)
        

def display_year_or_state_data(L,index,title):
    ''' 
    
        if index is  0 :
            print the format directed by the project
            
        for loop through the list from the parameter:
            
            print the format directed by the project in remove the element that represents state
        
        else:
            
            print the format directed by the project
            
            for loop through the list from the parameter:
            
                print the format directed by the project and remove the element that represents year 
    
    '''

    

   
    
    if index == 0:
        
    
        print("{:>5s}{:>18s}{:>18s}{:>22s}{:>14s}".format("Year","Revenue","Sales","Number of Customers","Price"))
        
        print("{:>5s}{:>18s}{:>18s}{:>22s}{:>14s}".format("","(in Thousands)","(MWh)","","(Cents/kWh)"))
        
        
        for i in L:
            
            print("{:>5}{:18,d}{:18,d}{:22,d}{:14,.2f}".format(i[0],i[2],i[3],i[4],i[5]))
    
    else:
        
        
        
        print("{:>5s}{:>18s}{:>18s}{:>22s}{:>14s}".format("State","Revenue","Sales","Number of Customers","Price"))
        
        print("{:>5s}{:>18s}{:>18s}{:>22s}{:>14s}".format("","(in Thousands)","(MWh)","","(Cents/kWh)"))
        
        for i in L:
            
            print("{:>5s}{:18,d}{:18,d}{:22,d}{:14,.2f}".format(i[1],i[2],i[3],i[4],i[5]))
        
        
        
        

def get_totals(master_list):
    ''' 
    create total_list[]
    
    create variables to store total values of total revenue, sales, customer,and price
    
    for loop through the Residential list of tuple :
        add the values to the variables
        
    append the total variables to total_list[]
    
    repeat this for commercial list, industrial list and transportation_list
    
    append the total variables tot total_list[]
    
    
    '''
    
    
   
    total_list = []
    
    
    total_rev = 0
    total_sal = 0
    total_cust = 0
    total_avg = 0
    count = 0
    for i in master_list[0]:
        
        total_rev += i[2]
        total_sal += i[3]
        total_cust += i[4]
        total_avg += i[5]
        count += 1
    
    total_list.append([total_rev,total_sal,total_cust,round(total_avg/count,2)])
    
    
    total_rev = 0
    total_sal = 0
    total_cust = 0
    total_avg = 0
    count = 0
    for i in master_list[1]:
        
        total_rev += i[2]
        total_sal += i[3]
        total_cust += i[4]
        total_avg += i[5]
        count += 1
    
    total_list.append([total_rev,total_sal,total_cust,round(total_avg/count,2)])
    
    
    total_rev = 0
    total_sal = 0
    total_cust = 0
    total_avg = 0
    count = 0
    for i in master_list[2]:
        
        total_rev += i[2]
        total_sal += i[3]
        total_cust += i[4]
        total_avg += i[5]
        count += 1
    
    total_list.append([total_rev,total_sal,total_cust,round(total_avg/count,2)])
    
   
    total_rev = 0
    total_sal = 0
    total_cust = 0
    total_avg = 0
    count = 0
    for i in master_list[3]:
        
        total_rev += i[2]
        total_sal += i[3]
        total_cust += i[4]
        total_avg += i[5]
        count += 1
    
    total_list.append([total_rev,total_sal,total_cust,round(total_avg/count,2)])
    
   
    
    return(total_list)
   

def display_totals(L):
    ''' 
        print the headers directed by the project
        
        
        create count = 0
        for loop through the list from the parameter of the function:
            
            add 1 to count everytime i goes to next list
            if count = 1 :
                name = "Residential"
            if count = 2:
                name = "Commercial"
            if count is 3 , then name is industrial
            if count is 4, then name is transportation
                
                print the format directed by the project and insert name in the format(names changes when i goes to the next line)

    
    '''
    
    print("{:^80s}".format("Revenue/Sales total for each category"))
    print("{:>15s}{:>18s}{:>18s}{:>22s}{:>14s}".format("Category","Revenue","Sales","Number of Customers","Price"))
    print("{:>15s}{:>18s}{:>18s}{:>22s}{:>14s}".format("","(in Thousands)","(MWh)","","(Cents/kWh)"))
    
    count = 0
    for i in L:
        
        count += 1
        if count == 1:
            name = "Residential"
        elif count == 2:
            name = "Commercial"
        elif count == 3:
            name = "Industrial"
        elif count == 4:
            name = "Transportation"
        
        print("{:>15s}{:18,d}{:18,d}{:22,d}{:14,.2f}".format(name,i[0],i[1],i[2],i[3]))
        
    
    

def state_plots(data,label):
    '''
        DO NOT MODIFY/DELETE THIS FUNCTION! 
        
        This function generates the plots for each column for a single area across
        every year for a single state.
        
        Parameters:
            data (list): The list of tuples with the sales/revenue tuples.
            label (str): State value for the tuples in data.
            
        Returns:
            None
    '''

    index = 0
    x_label = "year"
    
    x_labels = [str(y[index]) for y in data]
    revenue = [y[2] for y in data]
    sales = [y[3] for y in data]
    customers = [y[4] for y in data]
    price = [y[5] for y in data]
    
    form = "{} in {}".format("years",label)
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(15,15))

    
    #Plot the revenue and the sales in different y axes
    title = "Revenue and Sales per " + form
    y1_label = "Revenue (In Thousands)"
    y2_label = "Sales (MWh)"
    plot_line(axes[0],x_labels, [revenue,sales], title,[y1_label,y2_label],["Revenue","Sales"])
    axes[0].xaxis.set_ticklabels([])
    
    #Plot the number of customer and prices in different y axes
    title = "Number of customer and prices per " + form
    y3_label = "Number of customers"
    y4_label = "Price (Cents/kWh)"
    plot_line(axes[1],x_labels, [customers,price], title,[y3_label,y4_label],["Customer","Price"])
    axes[1].set_xlabel(x_label)

    fig.tight_layout()#automatically adjusts the positions of the axes so that
                  #there is no overlapping content:
    plt.show()
    


def plot_line(ax,x, y, title, y_label,legend):
    '''
        DO NOT MODIFY/DELETE THIS FUNCTION! 
        
        This function generates a line plot.
        
        Parameters:
            ax (matplotlib.axes._subplots.AxesSubplot): handle for figure axes
            x (list): List of x value strings for the line plot
            y (list): List of list of y values for the two Y-axes
            title (str): the title for the graph
            x_label (str): Name of the x-axis
            y_label (list): List of Names of the y-axis
            legend (list): List of names of the curves
            
            
        Returns:
            None
    '''
    
    ax.plot(x, y[0],label = legend[0],color="blue") #lw is line width
    ax.set_ylabel(y_label[0])
    ax.set_title(title)
    ax.legend(loc='upper left')
    ax.xaxis.set_ticklabels([])    
    for labels in ax.get_yticklabels():
        labels.set_color("blue")
        
    ax2 = ax.twinx()
    ax2.plot(x, y[1],label = legend[1],color="red")
    ax2.set_ylabel(y_label[1])    
    ax2.legend(loc='upper right')

    for labels in ax2.get_yticklabels():
        labels.set_color("red")

def main():
    
    BANNER = ''' Revenue/Sales data of Electricity in the United States across different areas: 
        Residential, Commercial, Industrial, and Transportation.'''
    print(BANNER)
    
    fp = open_file()
    master_list = read_file(fp)
    
    # Menu of the program
    MENU = '''Menu
    
    1. Display Revenue/Sales in a year
    2. Display Revenue/Sales in a state
    3. Display Total Revenue/Sales per category
    4. Stop the program    '''
    
    print(MENU)
    option = input("    Enter your option: ")
    
    
    
    while option != "4":
        
        while option != "1" and option != "2" and option != "3" and option != "4":
            
            print("Invalid option!")
            print(MENU)
            option = input("    Enter your option: ")
            continue
            
        
        option = int(option)
        
        if option == 1:
            
            category = input("Enter category: ")
            category = category.title()
            
            CATEGORIES = ["Residential","Commercial","Industrial", "Transportation"]
            
            while category not in CATEGORIES:
                print("Invalid category!")
                category = input("Enter category: ")
                category = category.title()
            
            
            year = input("Enter year (2007-2020): ")
            check = True
            while check == True:
                try:
                    
                    year = int(year)
                    if 2007 <= year <= 2020:
                        check = False
                        break
                    else:
                        print("Incorrect year! The year has to be between 2007 and 2020!")
                        year = int(input("Enter year (2007-2020): "))
                        continue
                except ValueError:
                
                    print("Incorrect year! The year has to be between 2007 and 2020!")
                    year = int(input("Enter year (2007-2020): "))
                    continue
                
                
                    
                    
                
            
            if category == "Residential":
                
                print("{:^80s}".format(category + " revenue/sales in " + str(year)))
                year = int(year)
                year_state_lst = (get_year_or_state_data(master_list[0], 0, year))
                display_year_or_state_data(year_state_lst, 0, year)
            
            elif category == "Commercial":
                
                print("{:^80s}".format(category + " revenue/sales in " + str(year)))
                year = int(year)
                year_state_lst = (get_year_or_state_data(master_list[1], 0, year))
                display_year_or_state_data(year_state_lst, 0, year)
                
                
            elif category == "Industrial":
                
                print("{:^80s}".format(category + " revenue/sales in " + str(year)))
                year = int(year)
                year_state_lst = (get_year_or_state_data(master_list[2], 0, year))
                display_year_or_state_data(year_state_lst, 0, year)
            
            elif category == "Transportation":
                
                print("{:^80s}".format(category + " revenue/sales in " + str(year)))
                year = int(year)
                year_state_lst = (get_year_or_state_data(master_list[3], 0, year))
                display_year_or_state_data(year_state_lst, 0, year)
    
        elif option == 2:
                  
            category = input("Enter category: ")
            category = category.title()
            
            CATEGORIES = ["Residential","Commercial","Industrial", "Transportation"]
            
            while category not in CATEGORIES:
                print("Invalid category!")
                category = input("Enter category: ")
                category = category.title()
                
    
            state = input("Enter state: ")
            
            check = True
            while check == True:
                try:
                    
                    state = str(state)
                    for i in master_list[0]:
                        if state == i[1]: 
                            check = False
                            break
                    else:
                        print("Invalid state!")
                        state = input("Enter state: ")
                        continue
                except ValueError:
                
                    print("Invalid state!")
                    state = input("Enter state: ")
                    continue
            
            
            
            if category == "Residential":
                
                print("{:^80s}".format(category + " revenue/sales in " + state))
                
                year_state_lst = (get_year_or_state_data(master_list[0], 1, state))
                display_year_or_state_data(year_state_lst, 1, state)
                
                answer = input("Do you want to plot (y/n)?")
                if answer == "y":
                    
                    state_plots(year_state_lst, state)
        
            elif category == "Commercial":
                
                print("{:^80s}".format(category + " revenue/sales in " + state))
                
                year_state_lst = (get_year_or_state_data(master_list[1], 1, state))
                display_year_or_state_data(year_state_lst, 1, state)
                
                answer = input("Do you want to plot (y/n)?")
                
                if answer == "y":
                    
                    state_plots(year_state_lst, state)
                  
        
            elif category == "Industrial":
                
                print("{:^80s}".format(category + " revenue/sales in " + state))
                
                year_state_lst = (get_year_or_state_data(master_list[2], 1, state))
                display_year_or_state_data(year_state_lst, 1, state)
                
                answer = input("Do you want to plot (y/n)?")
                if answer == "y":
                    
                    state_plots(year_state_lst, state)
                
            elif category == "Transportation":
                
                print("{:^80s}".format(category + " revenue/sales in " + state))
                
                year_state_lst = (get_year_or_state_data(master_list[3], 1, state))
                display_year_or_state_data(year_state_lst, 1, state)
                
                answer = input("Do you want to plot (y/n)?")
                if answer == "y":
                    
                    state_plots(year_state_lst, state)
            
            
        elif option == 3:
            L = get_totals(master_list)
            display_totals(L)
        
        elif option == 4:
            break
        
        print(MENU)
        option = input("    Enter your option: ")
        option = str(option)
        
    print("Thank you for using this program!")
        
    

# DO NOT DELETE THESE TWO LINES
if __name__ == "__main__":
    main()
    
