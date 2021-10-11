import pandas as pd
import matplotlib.pyplot as plt

# функція переведення футів і дюймів в метри
def parse_height(ht):
	ht_ = ht.split("-")
	ft_ = float(ht_[0])
	in_ = float(ht_[1])
	h_inch = ft_ * 12 + in_
	h_m = round(h_inch * 0.0254, 2)
	return h_m

# функція переведення фунтів в кілограми
def parse_weight(wt):
	w_kg = round(wt * 0.4536, 2)
	return w_kg

# зчитування даних з файлу сsv
nba = pd.read_csv('nba.csv')
print('NBA DataFrame:')
print(nba)

# дані де є NaN значення
nba_columns_NaN = nba.loc[:, nba.isnull().any()]
print('NBA DataFrame witn NaN:')
print(nba_columns_NaN)

# видалення рядків з NaN
nba_without_NaN = nba.dropna()
print('NBA DataFrame without NaN:')
print(nba_without_NaN)

# переведення росту та ваги
nba_without_NaN['Meters'] = nba_without_NaN['Height'].apply(lambda x:parse_height(x))
nba_without_NaN['Kilograms'] = nba_without_NaN['Weight'].apply(lambda x:parse_weight(x))
print('NBA DataFrame with meters and kilograms:')
print(nba_without_NaN)

# обрахунок суми по зарплаті
salary_sum = nba_without_NaN['Salary'].sum()
print('Sum of salary:')
print(salary_sum)

# обрахунок середнього значення по віку
age_mean = nba_without_NaN['Age'].mean()
print('Mean of age:')
print(age_mean)

# обрахунок медіани по вазі
weight_median = nba_without_NaN['Weight'].median()
print('Median of weight:')
print(weight_median)

# обрахунок мінімального значення росту
height_min = nba_without_NaN['Height'].min()
print('Min of height:')
print(height_min)

# обрахунок максимального значення росту
height_max = nba_without_NaN['Height'].max()
print('Max of height:')
print(height_max)

# сортування даних за віком
nba_sort_salary = nba_without_NaN.sort_values(by='Age', ascending=True)

# графік залежності ваги від віку
plt.plot(nba_sort_salary['Age'], nba_sort_salary['Weight'])
plt.xlabel('Age')
plt.ylabel('Weight')
plt.show()

# гістограма по віку
count = int(nba_sort_salary['Age'].max() - nba_sort_salary['Age'].min())
plt.hist(nba_sort_salary['Age'], bins = count, edgecolor='black')
plt.xlabel('Age')
plt.ylabel('Probability')
plt.show()

# стовпчикова діаграма залежності зарплати від команди
mean_salary_by_team = nba_without_NaN.groupby(['Team']).mean()
mean_salary_by_team = mean_salary_by_team.add_suffix('_Mean').reset_index()
print(mean_salary_by_team)
plt.barh(mean_salary_by_team['Team'], mean_salary_by_team['Salary_Mean'])
plt.xlabel('Salary')
plt.ylabel('Team')
plt.show()

# експорт даних в csv файл
nba_without_NaN.to_csv('export_nba.csv')
