userData=input('Enter first name, second name and year of birth (separated with \',\'): ')
data = userData.split(',')
if len(data) == 3:
    firstName = data[0]
    secondName = data[1]
    birthYear = data[2]
