#cap 06
pessoa = {
	'first_name': 'Deusi', 
	'last_name': 'Nascimento',
	'age': 35, 
	'city': 'Belford Roxo'
		}
print(pessoa)

user_0 = {
	'username': 'efermi',
	'first':'enrico',
	'last': 'fermi'
}
print(user_0['username'])
print("\n\nmais exemplos\n\n")

favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
	}
for name, language in favorite_languages.items():
	print(name.title() + "'s favorite language is " +
language.title() + ".")

print("\n\nmais exemplos\n\n")

for name in favorite_languages.keys():
	print(name.title())

print("\n\nmais exemplos\n\n")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
if name in friends:
	print("Hi " + name.title() +
	", I see your favorite language is " +
	favorite_languages[name].title() + "!")

print("\n\nmais exemplos\n\n")

for name in sorted(favorite_languages.keys()):
	print(name.title() + ", tank you for taking the poll.")

print("\n\nmais exemplos\n\n")

for language in favorite_languages.values():
	print(language.title())

print("\n\nmais exemplos\n\n")

for language in set(favorite_languages.values()):
	print(language.title())
print("\n\nmais exemplos\n\n")
favorite_languages = {
'jen': ['python', 'ruby'], 'sarah': ['c'], 'edward': ['ruby', 'go'],
'phil': ['python', 'haskell'], }
for name, languages in favorite_languages.items(): 
	print("\n" + name.title() + 
	"'s favorite languages are:") 
for language in languages: 
	print("\t" + language.title())
