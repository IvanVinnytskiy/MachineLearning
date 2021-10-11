import pandas as pd
import matplotlib.pyplot as plt

# зчитування даних з файлу сsv
employees = pd.read_csv('employees.csv')
print('Employees DataFrame:')
print(employees)

# дані де є NaN значення
employees_columns_NaN = employees.loc[:, employees.isnull().any()]
print('Employees DataFrame witn NaN:')
print(employees_columns_NaN)

# видалення рядків з NaN
employees_without_NaN = employees.dropna()
print('Employees DataFrame without NaN:')
print(employees_without_NaN)

# обрахунок суми по зарплаті
salary_sum = employees_without_NaN['Salary'].sum()
print('Sum of salary:')
print(salary_sum)

# обрахунок середнього значення по бонусу
bonus_mean = employees_without_NaN['Bonus %'].mean()
print('Mean of bonus:')
print(bonus_mean)

# обрахунок медіани по зарплаті
salary_median = employees_without_NaN['Salary'].median()
print('Median of salary:')
print(salary_median)

# обрахунок мінімального значення часу останнього входу
last_login_time_min = employees_without_NaN['Last Login Time'].min()
print('Min of last login time:')
print(last_login_time_min)

# обрахунок максимального значення часу останнього входу
last_login_time_max = employees_without_NaN['Last Login Time'].max()
print('Max of last login time:')
print(last_login_time_max)

# сортування даних за величиною зарплати
employees_sort_salary = employees_without_NaN.sort_values(by='Salary', ascending=True)

# графік залежності бонусів від зарплати
plt.plot(employees_sort_salary['Salary'], employees_sort_salary['Bonus %'])
plt.xlabel('Salary')
plt.ylabel('Bonus')
plt.show()

# гістограма по зарплаті
count = int((employees_sort_salary['Salary'].max() - employees_sort_salary['Salary'].min()) / employees_sort_salary['Salary'].count())
plt.hist(employees_sort_salary['Salary'], bins = count, edgecolor='black')
plt.xlabel('Salary')
plt.ylabel('Probability')
plt.show()

# стовпчикова діаграма залежності зарплати від команди
mean_salary_by_team = employees_without_NaN.groupby(['Team']).mean()
mean_salary_by_team = mean_salary_by_team.add_suffix('_Mean').reset_index()
print(mean_salary_by_team)
plt.barh(mean_salary_by_team['Team'], mean_salary_by_team['Salary_Mean'])
plt.xlabel('Salary')
plt.ylabel('Team')
plt.show()

# експорт даних в csv файл
employees_without_NaN.to_csv('export_employees.csv')

