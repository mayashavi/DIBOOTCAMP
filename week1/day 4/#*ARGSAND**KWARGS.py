#*ARGS and **KWARGS = just arguments and keyword arguments

#*ARGS:
friends = ['Ross', 'Rachel', 'Monica', 'Joey','Chandler', 'Phoebe']

def how_you_doin(*args):
    if args:
        for name in args: 
            print(f'{name}, how you doin\'?')
        
print(how_you_doin('Ross', 'Rachel', 'Monica', 'Joey','Chandler', 'Phoebe'))

#**KWARGS:
def user_info(**kwargs):
    print(kwargs)

user_info(name = 'Ross', last_name = 'Geller', age = 35, has_children = True, cheat_on_Rachel = True)
