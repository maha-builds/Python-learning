book_name=input("Enter the book name: ")
author_name=input("Enter the author name: ")
book_availability=input("Enter the book availability yes or no: ")

if book_availability == "yes":
    print("Book is available")
else:
    print("Book is not available")


books=["python","Java","c programming","data science"]

search=input("Enter book to search")
if search in books:
    print("book found")
else:
    print("book not found")


book_issue=input("Enter the book issue: ")
if book_issue=='yes' and book_availability=="yes":
    print("Book issued successfully")
elif book_issue=='yes' and book_availability=="no":
    print("Book cannot be issued")
else:
    print("no issue")
