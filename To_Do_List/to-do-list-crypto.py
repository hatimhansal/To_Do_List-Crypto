import os
from cryptography.fernet import Fernet


option_seen_the_localisation = ''

value1= option_seen_the_localisation

def localisation(value1):
    if value1 == 'y':
        n = os.listdir('.')
        print(f"hello this is folder i themes ",n)

localisation(value1)

#option_seen_the_localisation = input("do you want to see the localisation of the file ? (y/n) : ")

#################################################################################################




# function 

def afficherTableau():
    aff=input('afficher y/n :')
    if aff == "y":
        print('______id_______title________body______status')
    for n in note :
        print(f"___{n['id']}_____{n['title']}_____{n['body']}____{n['status']}")
    else : 
        print('')

def choixALl(choix,note):
    if  choix.lower() == 'afficher'  or choix == '1' :
        afficherTableau()
        reppeat()
    elif choix.lower() == 'add'or choix == '2' :
        body=input('the thing you do :')
        title =input('Title name (default Title = no/n ):')
        reppeat()
        if title == 'no' or title == 'n' or title == '':
                title = body.split()[0]
                new_id = len(note) + 1
                
                note.append({
                'id':new_id,
                'title':title,
                'body':body,
                'status':False
                    })
        else :
            new_id = len(note) + 1
                
            note.append({
            'id':new_id,
            'title':title,
            'body':body,
            'status':False
                })
        #key = Fernet.generate_key()
        print(' Ajouter avec success')
        afficherTableau()
        reppeat()
   
    elif choix.lower() == 'delete'  or choix == '3':
        destroy=int(input("number the column"))
        for n in note :
            if  destroy == int(n['id']) :
                note.remove(n)
                print('complete')

            else :
                print('not found')
        afficherTableau()
        reppeat()


def reppeat():
    while True :
        exits =input('Exits (default No/non) :')
        if exits == '' or exits == 'non' or exits == 'No' :
            choix = input("what wana do ('Afficher/Add'/'Delete'/Update) or write (1,2,3,4) ? :")
        else :
            break
            




choix = input("what wana do ('Afficher/Add'/'Delete'/Update) or write (1,2,3,4) ? :")

note=[{'id':1,"title":" make lunch ","body":" 2h do lunch ", "status":True}]



choixALl(choix,note)