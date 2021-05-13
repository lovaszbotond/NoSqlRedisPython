from Studio import Studiosztaly

rf = Studiosztaly()

print('takaritottunk')
#rf.clean()

rf.uj_film('Alkonyattól pirkadatig', 'horror')
rf.uj_film('Ponyvaregény', 'horror')
rf.uj_rendezo('abcs@gmail','asd123','Quentin_Tarantino')
rf.uj_rendezo('abcd@gmail','asdc123','Guy Ritchie')


print('A jelenlegi film_lista ')
print(rf.film_lista())
print('film_leker ')
print(rf.film_leker('c435e824-9a96-42a7-bca9-4a319b145dce'))
print(rf.film_leker('707b2031-e50f-4dca-acf1-8b37cfff0f1d'))
print('rendezo_lista')
print(rf.rendezo_lista())
print('rendezo_leker')
print(rf.rendezo_leker('abcs@gmail'))
print('film_hossz')
print(rf.film_hossz('c435e824-9a96-42a7-bca9-4a319b145dce'))
print('efilm')
rf.efilm('abcd@gmail','c435e824-9a96-42a7-bca9-4a319b145dce')

print('rendezett_filmek')
print(rf.rendezett_filmek('abcd@gmail'))
print('ki_rendezte')
print(rf.ki_rendezo('abcd@gmail'))
print('rendezo_leker')
print(rf.rendezo_leker('abcs@gmail'))
print('filmazon_lekercim')
print(rf.filmazon_lekercim('Ponyvaregény'))
print('email_kiir')
print(rf.email_kiir('Quentin_Tarantino'))
print('elfelejtett_jelszo')
print(rf.elfelejtett_jelszo('abcs@gmail'))
print('nyugdijba kuldes utan fennmaradt rendezők')
rf.rendezo_nyugdij('abcd@gmail')
print(rf.rendezo_lista())







