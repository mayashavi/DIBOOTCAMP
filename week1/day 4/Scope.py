#Scopes: global & local
fav_movie = 'Heathers' #global scope

def movie_reccommendations(fav_movie):
    recommend = 'Mean Girls' #local scope
    print(recommend)
    return recommend

print(movie_reccommendations(fav_movie))

#gloval variables can be consulted from the local scope, but not changed

savings = 500

def buy_stuff(amount):
    global savings
    savings -= 100
    if amount <= savings:
        return True
    else:
        return False
    
print(buy_stuff(400))
