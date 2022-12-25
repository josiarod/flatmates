from flat import Bill, Flatmate
from reports import PdfReport

amount = float(input("Hello user, enter the bill amount: "))
period = input("Please enter the corresponding period e.g. December 2022: ")

name1 = input("Please enter your name: ")
days_in_house1 = int(input(f"Enter days did {name1} stay in the house during the bill period: "))
name2 = input("Please enter the name of the second flatmate: ")
days_in_house2 = int(input(f"Enter days did {name2} stay in the house during the bill period: "))


the_bill = Bill(amount, period)
flatmate_one = Flatmate(name1, days_in_house1)
flatmate_two = Flatmate(name2, days_in_house2)
print(f"{flatmate_one.name} pays: ", flatmate_one.pays(the_bill, flatmate_two))
print(f"{flatmate_two.name} pays: ", flatmate_two.pays(the_bill, flatmate_one))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate_one, flatmate_two, the_bill)






