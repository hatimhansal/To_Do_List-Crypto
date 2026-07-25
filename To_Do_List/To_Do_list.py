import json



def AfficheTitre():
    print(' ___TO__DO___LIST____')

def getTableau():
    with open('notes.json','r') as file :
        data=json.load(file)
    return data
def AjouterList(new_list):
    with open('notes.json','w') as file:
        json.dump(new_list,file,indent=4)


def IF_notfound():
    list=getTableau()
    if len(list) == 0 :
        lisr_Aleatoire()
    
    else :
        print('ok')
def lisr_Aleatoire():
    with open('notes.json','w') as file :
        new_id=len(notes) + 1 
        new_AL_list=notes.append({
        'id':new_id,
        'title':'test',
        'body':"body_test",
        'status':True
        })
        json.dump(new_AL_list,file,indent=4)




notes =getTableau()


def Add(notes) :
    body = input("Body: ")
    title = input("Title: ")
    new_id=len(notes) + 1 
    notes.append({
        'id':new_id,
        'title':title,
        'body':body,
        'status':False
    })
    AjouterList(notes)
        

def Show(notes) :
    IF_notfound()
    AfficheTitre()
    print('__id__Title__body__starus__')
    for n in notes :
        print(f"__{n['id']}__{n['title']}__{n['body']}__{n['status']}__")

def Remove(notes) :
    Show(notes)
    Rid=int(input('choiser the id you delete :'))
    for n in notes :
        if  int(n['id']) == Rid :
            notes.remove(n)
            AjouterList(notes)
            break



while True :
    choix=input('Open (Show-(s)/Remove-(r)/Add-(a)/Exits-(e)) (default Show) :')
    if choix.lower() == 'show' or choix.lower() == 's': 
        Show(notes)
    elif  choix.lower() =='remove'  or choix.lower() == 'r':
        Remove(notes)
    elif choix.lower()=='add'  or choix.lower() == 'a':
        Add(notes)
    
    elif choix == '':
        Show(notes)
    elif choix.lower == 'exit'  or choix.lower() == 'e':
        break
    else :
        print('invalid choix')






