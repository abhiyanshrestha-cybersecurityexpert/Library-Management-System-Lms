############################################
# Register

def register():
    print('Library Management System')
    print('Register')
    username = input('Enter Username: ')
    password = input('Enter New Password: ')
    usertype = input('Enter Usertype(Superadmin or Manager): ')
    
    with open('userdata.txt','a') as f:
        print(f'{username},{password},{usertype}\n')
        print('Registration Successful')

############################################
# Login
def login():
    print('Library Management System')
    print('Login')
    username = input('Enter Username: ')
    password = input('Enter Password: ')
    
    with open('userdata.txt','r') as f:
        for line in f:
            user_name,user_password,usertype = line.strip().split(',')
            if user_name == username and user_password == password:
                return usertype
            print('Welcome to Our Library Management System')
        else:
            print('Username or Password is wrong!')

############################################
# Add Books

def add_books():
    bookname = input('Enter Book Name: ')
    bookcategory = input('Enter Book Category: ')
    bookdescription = input('Enter Book Description: ')
    bookauthor = input('Enter Book Author Name: ')
    bookprice = int(input('Enter Book Price: '))
    
    with open('bookslist.txt','a') as f:
        f.write(f'{bookname},{bookcategory},{bookdescription},{bookauthor},{bookprice}\n')
        print('Book Added Successfully in System')

############################################
# View Book List

def view_booklist():
    try:
        with open('bookslist.txt','r') as f:
            print('Book Name\t\tBook Category\t\tBook Description\t\tBook Author\t\tBook Price')
            for line in f:
                try:
                    book_name,book_category,book_description,book_author,book_price = line.strip().split(',')
                    print(f'{book_name},{book_category},{book_description},{book_author},{book_price}\n')
                except ValueError:
                    print('Invalid Data!')
    except FileNotFoundError:
        print('File Not Found!')

############################################
# Book For Rent
import datetime

def book_forrent():
    customerid = int(input('Enter Id: '))
    customername = input('Enter Customer Name: ')
    bookname = input('Enter Book Name: ')
    bookcategory = input('Enter Book Category: ')
    numberofdays = input('Enter Number Of Days: ')
    
    # Get current date as taken date
    taken_date = datetime.date.today()

    # Calculate return date by adding the number of days to the taken date
    return_date = taken_date + datetime.timedelta(days=numberofdays)
    
    with open('bookforrent.txt','a') as f:
        f.write(f'{customerid},{customername},{bookname},{bookcategory},{numberofdays},{taken_date},{return_date}\n')                
        print('Successfully Added Customer Details For Rent.')

def view_bookforrent():
    try:
        with open('bookforrent.txt','r') as f:
            print('customer id\tcustomername\t\tbookname\t\tbookcategory\tnumber of days\ttaken date\t\treturn date')
            for line in f:
                try:
                    customer_id,customer_name,book_name,book_category,number_ofdays,takendate,returndate = line.strip().split(',')
                    print(f'{customer_id},{customer_name},{book_name},{book_category},{number_ofdays},{takendate},{returndate}\n')
                
                except ValueError:
                    print('Invalid Data!')
    except FileNotFoundError:
        print('File Not Found!')

############################################
# Delete Book List

def delete_booklist(book_name):
    
    """Deletes a book from the bookslist.txt file based on its name.

    Args:
        book_name (str): The name of the book to delete.
    """

    with open('bookslist.txt', 'r') as f:
        lines = f.readlines()

    with open('bookslist.txt', 'w') as f:
        for line in lines:
            book_data = line.strip().split(',')
            if book_data[0] != book_name:
                f.write(line)
        print('Book Deleted Successfully from System')
    

###########################################
# Main Program
def main():
    while True:
        print('Library Management System')
        print('Choices')
        Choice = input('1.Login\t\tq.Quit: ')
        
        if Choice == '1':
            usertype = login()
            
            if usertype:
                if usertype == 'superadmin':
                    while True:
                        Choice = input('1.View Book List 2.Add Books 3.Add Book For Rent 4.View Book For Rent 5. Add User 6.Delete Book List q.Logout: ')
                        
                        if Choice == '1':
                            view_booklist()
                        
                        elif Choice == '2':
                            add_books()
                        
                        elif Choice == '3':
                            book_forrent()
                        
                        elif Choice == '4':
                            view_bookforrent()
                        
                        elif Choice == '5':
                            register()
                        
                        elif Choice == '6':
                            delete_booklist()
                        
                        elif Choice == 'q':
                            break
                        else:
                            print('Invalid Choice!')
                else:
                    while True:
                        Choice == input('1.Book List 2.Add Books 3.Add Book For Rent 4.View Book For Rent q.Logout: ')
                        
                        if Choice == '1':
                            view_booklist()
                        
                        elif Choice == '2':
                            add_books()
                        
                        elif Choice == '3':
                            book_forrent()
                        
                        elif Choice == '4':
                            view_bookforrent()
                        
                        elif Choice == 'q':
                            break
                        
                        else:
                            print('Invalid Choice!')
                            
        
        elif Choice == 'q':
            break
        
        else:
            print('Invalid Input!')
        
            
main()   