import pandas as pd

# перший DataFrame
product=pd.DataFrame({
    'Product_ID':[101, 102, 103, 104, 105, 106, 107],
    'Product_name':['Milk', 'Banana', 'Tomato', 'Bread', 'Onion', 'Peach', 'IceCream'],
    'Category':['DairyProduct', 'Fruit', 'Vegetables','Bakery', 'Vegetables', 'Fruit', 'DaityProduct'],
    'Price':[24.0,46.30,47.40,13.0,24.50,90.0,51.0],
    'Seller_Shop':['Silpo','Silpo','Delikat','SviyMarket','Silpo','Blizenko','Delikat']
})

# другий DataFrame
customer=pd.DataFrame({
    'id':[1, 2, 3, 4, 5, 6, 7, 8, 9],
    'name':['Ivan', 'Andriy', 'Olga', 'Kostya', 'Nastya', 'Dmytro', 'Ira', 'Oksana', 'Oleg'],
    'age':[21, 26, 18, 20, 30, 28, 17, 18, 21],
    'Product_ID':[101, 0, 106, 0, 103, 104, 0, 0, 107],
    'Purchased_Product':['Milk', 'NA', 'Peach', 'NA', 'Tomato', 'Bread', 'NA', 'NA', 'IceCream'],
    'City':['Lviv', 'Kyiv', 'Cherkasy', 'Lviv', 'Poltava', 'Lviv', 'Odesa', 'Kyiv', 'Kyiv']
})

# виведення першого DataFrame
print("First DataFrame:")
print(product)

# виведення другого DataFrame
print("Second DataFrame:")
print(customer)

# inner join а колонкою Product_ID
inner_join = pd.merge(product, customer, on='Product_ID')
print("Inner Join:")
print(inner_join)

# outer join а колонкою Product_ID
outer_join = pd.merge(product, customer, on='Product_ID', how='outer', indicator=True)
print("Outer Join:")
print(outer_join)

# left join а колонкою Product_ID
left_join = pd.merge(product, customer, on='Product_ID', how='left')
print("Left Join:")
print(left_join)

# right join а колонкою Product_ID
right_join = pd.merge(product, customer, on='Product_ID', how='right')
print("Right Join:")
print(right_join)