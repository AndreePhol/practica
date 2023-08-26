print("=============================================> 1 <====================================================")
persona = {
 'first_name': 'Edem',
 'last_name': 'Terraza',
 'age': 31,
 'country': 'Peru',
 'is_married': True, #
 'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
 'address': {
 'street': 'Space street',
 'zipcode': '02210'
 }
}
print("--------------------------> a <-------------------------")
if "skills" in persona:
    if len(persona['skills'])%2!=0:
        print(persona['skills'][int((len(persona['skills'])-1)/2)])
else:
    print("n")
print("--------------------------> b <-------------------------")
if 'skills' in persona:
    if 'Python' in persona['skills']:
        print("si exsiste : python")
    else:
        print("no se encuentra python")
else:
    print("n")
print("--------------------------> c <-------------------------")
if 'JavaScript'and 'React'in persona['skills']:
    print("Él es un desarrollador frontend")
if 'Node'and'MongoDB'and 'Python' in persona['skills']:
    print("Él es un desarrollador backend")
if 'React'and 'Node'and 'MongoDB' in persona['skills']:
    print("Él es un desarrollador fullstalk")
else:
    print("titulo desconocido")

print("=============================================> 2 <====================================================")
import cd
print("--------------------------> a <-------------------------")
cd.nti()
print("--------------------------> b <-------------------------")
cd.dimh()
print("--------------------------> c <-------------------------")
cd.dpmp()