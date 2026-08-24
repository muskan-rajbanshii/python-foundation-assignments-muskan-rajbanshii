monthly_sales = [85000, 120000, 95000, 140000, 75000, 160000]

#1
sorted_list = sorted(monthly_sales,reverse = True)
print(sorted_list)
#2
values_above = [i for i in monthly_sales if i > 100000]
print(values_above)

#3
amount_with_tax = [(i + (13/100)*i) for i in monthly_sales ]
print(amount_with_tax)

#4
total_sales_amount = sum(monthly_sales)
print(f"Total sales amount : {total_sales_amount}")

#5
average_sales_amount = total_sales_amount / len(monthly_sales)
print(f"Average sales amount : {average_sales_amount}")