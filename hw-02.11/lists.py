# 1
# animals = []

# 2
# animals = ['cow', 'pig', 'monkey', 'horse', 'cat', 'dog' ,'eagle']

# 3
# animals = ['cow', 'pig', 'monkey', 'horse', 'cat', 'dog' ,'eagle']
# print(len(animals))

# 4
# animals = ['cow', 'pig', 'monkey', 'horse', 'cat', 'dog' ,'eagle']
# item1,*rest, item3, item6 = animals
# print(item1)
# print(item3)
# print(item6)

# 5
# mixed_datd_types = ['yasemin', '16', '173', 'good', 'london_street']

# 6
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 7
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# print(it_companies)

# 8
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# print(len(it_companies))

# 9
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# item1,*rest, item3, item6 = it_companies
# print(item1)
# print(item3)
# print(item6)

# 10
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# it_companies[3] = 'Disk'
# print(it_companies)

# 11
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# it_companies.append('IT_company')
# print(it_companies)

# 12
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# it_companies[3] = 'Instagram'
# print(it_companies)


# 13
# IT = ['Face-book', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# print(IT.title())

# 14
IT = ['Face-book', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 15
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# does_exist = 'Google' in it_companies
# print(does_exist)

# 16
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# print(sorted(it_companies))

# 17
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# it_companies = sorted(it_companies,reverse=True)
# print(it_companies)

# 18
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# print(it_companies[0:3])

# 19
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# print(it_companies[-3:])

# 20
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# 25
# it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
# it_companies.clear()
# print(it_companies)

# 26
# font_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
# back_end = ['Node', 'Express', 'MongoDB']
# font_end.extend(back_end)
# print(font_end)
# print(back_end)


26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
27
full_stack = front_end + back_end
print(full_stack)
full_stack.insert(2, 'Python')
full_stack.insert(4, 'SQL')
full_stack.insert(5,'Redux')
print(full_stack)