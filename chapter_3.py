#Python installation virtual enviroment
#command: python3 -m venv "myhouse"

'''
Python installation of packages
python3 -m pip install "packagename"
pip install "packagename"
pip install -r requirements.txt
pip freeze > requirements.txt
'''
#Using different base like base2, base16
print("Base2(0b11001)")
print(0b11001)
print('------------------------------------------------------------------')
print("Base16(0x28b98f)")
print(0x28b98f)
#Manipulating values of a string
word = 'Devnet'
print('------------------------------------------------------------------')
print(word[0])
print(word[4])
print(word[:3])
print('------------------------------------------------------------------')
print(word * 5)
print(word + ' Cisco')
print(str.upper(word))
print('------------------------------------------------------------------')
#Data type (Lists)
print("List, tuples, dictionaries")
kids = ['Eddu', 'Miguel', 'Jose']
print(kids)
print('My youngest brother is: ', kids[1])
print("Reversing order string")
print(list.sort(kids))
#Data type (Tuples)
person = (2012, 'Mike', 'CCNA')
print(person)
#Data type (Dictionary)
cabinet = {"score": (98,76,95), "name": "Chris", "company": "Cisco"}
print(cabinet)
print("print company name: " + cabinet["company"])
#Data type(Sets)
numbs = {1, 2, 4, 5, 6, 8, 10}
odds = {1, 3, 5, 7, 9}
print("Joining two sets numbs = {1, 2, 4, 6, 8, 10} odds = {1, 3, 5, 7, 9}")
print(numbs | odds)
print('------------------------------------------------------------------')
#Use type() to find the data type
print("Use type() to find the data type")
print(type(word))