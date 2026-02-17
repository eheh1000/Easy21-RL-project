import random
def draw_card() :
    tirage = random.randint(1,10)
    tirage_couleur = random.randint(1,3)
    if tirage_couleur == 1 :
        couleur = "rouge"
    else :
        couleur = "noire"
    return tirage, couleur
    

def step(state, action) :

    if state['dealer'] < 1 or state['player'] < 1 or state['dealer'] > 21 or state['player'] > 21 :
        print("Etat impossible")
        return next_state, 0, False
    
    tirage = 0
    couleur = 1
    next_state = state 
    reward = 0
    terminal = False
    score_croupier = state['dealer']

    if action == "stick" :
        terminal = True

        while score_croupier < 17 :
            tirage, couleur = draw_card()

            if couleur == "rouge" :
                score_croupier -= tirage
                print(score_croupier," - ", state['player'])
                if score_croupier < 1 :
                    "le coupier bust !!"
                    reward = 1
                    return next_state, reward, terminal
            
            else :
                score_croupier += tirage
                print(score_croupier," - ", state['player'])
                if score_croupier > 21 :
                    "le croupier bust !!"
                    reward = 1
                    return next_state, reward, terminal
    
        
        if score_croupier > state['player'] :
            print("Lose")
            reward = -1
        elif score_croupier == state['player'] :
            reward = 0
            print("Draw")
        else :
            print("Win")
            reward = 1
        return next_state, reward, terminal


    elif action == "hit" :

        tirage,couleur = draw_card()

        if couleur == "rouge" :  

            next_state['player'] -= tirage
            if next_state['player'] < 1 :
                terminal = True
                reward = -1
            return next_state, reward, terminal

        else :            

            next_state['player'] += tirage
            if next_state['player'] > 21 :
                terminal = True
                reward = -1
            return next_state, reward, terminal
        
    else :
        print("Action non valable")
        return next_state, 0, False
    
def init_game():
    state = {'dealer' : 0, 'player': 0}
    tirage = random.randint(1,10)
    state['dealer'] = tirage
    tirage = random.randint(1,10)
    state['player'] = tirage
    return state


state = init_game() 
terminal = False
reward = 0
print("Etat de départ",state)
while terminal == False :
    action = input()
    state, reward, terminal = step(state, action)
    print(state)
