def BLACKJACK():
    from IPython.display import clear_output
    deck1 = ['Ace of spades','Ace of clubs','Ace of hearts','Ace of diamonds','2 of spades','2 of clubs','2 of hearts','2 of diamonds','3 of spades','3 of clubs','3 of hearts','3 of diamonds','4 of spades','4 of clubs','4 of hearts','4 of diamonds','5 of spades','5 of clubs','5 of hearts','5 of diamonds','6 of spades','6 of clubs','6 of hearts','6 of diamonds','7 of spades','7 of clubs','7 of hearts','7 of diamonds','8 of spades','8 of clubs','8 of hearts','8 of diamonds','9 of spades','9 of clubs','9 of hearts','9 of diamonds','10 of spades','10 of clubs','10 of hearts','10 of diamonds','Jack of spades','Jack of clubs','Jack of hearts','Jack of diamonds','Queen of spades','Queen of clubs','Queen of hearts','Queen of diamonds','King of spades','King of clubs','King of hearts','King of diamonds'] 
    deck2 = ['Ace of spades','Ace of clubs','Ace of hearts','Ace of diamonds','2 of spades','2 of clubs','2 of hearts','2 of diamonds','3 of spades','3 of clubs','3 of hearts','3 of diamonds','4 of spades','4 of clubs','4 of hearts','4 of diamonds','5 of spades','5 of clubs','5 of hearts','5 of diamonds','6 of spades','6 of clubs','6 of hearts','6 of diamonds','7 of spades','7 of clubs','7 of hearts','7 of diamonds','8 of spades','8 of clubs','8 of hearts','8 of diamonds','9 of spades','9 of clubs','9 of hearts','9 of diamonds','10 of spades','10 of clubs','10 of hearts','10 of diamonds','Jack of spades','Jack of clubs','Jack of hearts','Jack of diamonds','Queen of spades','Queen of clubs','Queen of hearts','Queen of diamonds','King of spades','King of clubs','King of hearts','King of diamonds']
    deck3 = ['Ace of spades','Ace of clubs','Ace of hearts','Ace of diamonds','2 of spades','2 of clubs','2 of hearts','2 of diamonds','3 of spades','3 of clubs','3 of hearts','3 of diamonds','4 of spades','4 of clubs','4 of hearts','4 of diamonds','5 of spades','5 of clubs','5 of hearts','5 of diamonds','6 of spades','6 of clubs','6 of hearts','6 of diamonds','7 of spades','7 of clubs','7 of hearts','7 of diamonds','8 of spades','8 of clubs','8 of hearts','8 of diamonds','9 of spades','9 of clubs','9 of hearts','9 of diamonds','10 of spades','10 of clubs','10 of hearts','10 of diamonds','Jack of spades','Jack of clubs','Jack of hearts','Jack of diamonds','Queen of spades','Queen of clubs','Queen of hearts','Queen of diamonds','King of spades','King of clubs','King of hearts','King of diamonds'] 
    deck4 = ['Ace of spades','Ace of clubs','Ace of hearts','Ace of diamonds','2 of spades','2 of clubs','2 of hearts','2 of diamonds','3 of spades','3 of clubs','3 of hearts','3 of diamonds','4 of spades','4 of clubs','4 of hearts','4 of diamonds','5 of spades','5 of clubs','5 of hearts','5 of diamonds','6 of spades','6 of clubs','6 of hearts','6 of diamonds','7 of spades','7 of clubs','7 of hearts','7 of diamonds','8 of spades','8 of clubs','8 of hearts','8 of diamonds','9 of spades','9 of clubs','9 of hearts','9 of diamonds','10 of spades','10 of clubs','10 of hearts','10 of diamonds','Jack of spades','Jack of clubs','Jack of hearts','Jack of diamonds','Queen of spades','Queen of clubs','Queen of hearts','Queen of diamonds','King of spades','King of clubs','King of hearts','King of diamonds'] 
    deck5 = ['Ace of spades','Ace of clubs','Ace of hearts','Ace of diamonds','2 of spades','2 of clubs','2 of hearts','2 of diamonds','3 of spades','3 of clubs','3 of hearts','3 of diamonds','4 of spades','4 of clubs','4 of hearts','4 of diamonds','5 of spades','5 of clubs','5 of hearts','5 of diamonds','6 of spades','6 of clubs','6 of hearts','6 of diamonds','7 of spades','7 of clubs','7 of hearts','7 of diamonds','8 of spades','8 of clubs','8 of hearts','8 of diamonds','9 of spades','9 of clubs','9 of hearts','9 of diamonds','10 of spades','10 of clubs','10 of hearts','10 of diamonds','Jack of spades','Jack of clubs','Jack of hearts','Jack of diamonds','Queen of spades','Queen of clubs','Queen of hearts','Queen of diamonds','King of spades','King of clubs','King of hearts','King of diamonds'] 
    deck6 = ['Ace of spades','Ace of clubs','Ace of hearts','Ace of diamonds','2 of spades','2 of clubs','2 of hearts','2 of diamonds','3 of spades','3 of clubs','3 of hearts','3 of diamonds','4 of spades','4 of clubs','4 of hearts','4 of diamonds','5 of spades','5 of clubs','5 of hearts','5 of diamonds','6 of spades','6 of clubs','6 of hearts','6 of diamonds','7 of spades','7 of clubs','7 of hearts','7 of diamonds','8 of spades','8 of clubs','8 of hearts','8 of diamonds','9 of spades','9 of clubs','9 of hearts','9 of diamonds','10 of spades','10 of clubs','10 of hearts','10 of diamonds','Jack of spades','Jack of clubs','Jack of hearts','Jack of diamonds','Queen of spades','Queen of clubs','Queen of hearts','Queen of diamonds','King of spades','King of clubs','King of hearts','King of diamonds'] 
    ################################################################

    class Account:
        def __init__(self,owner,balance):
            self.owner = owner
            self.balance = balance

            print (f'Hi {owner}, welcome to Banco De Maretima! You have a balance of {balance}.')


        def dep(self,amt):
            self.balance = self.balance + amt
            print(f'Thanks for your deposit of {amt}, {self.owner}.Your current balance is {self.balance}')

        def withd(self,amt):
            if amt < self.balance:
                self.balance = self.balance - amt
                print (f'Hi {self.owner}. You have made a withdrawal of {amt}, your new balance is {self.balance}')
            else:
                print ('Call yo mama, you outta money!')
        def currbal(self):
            self.balance
            print (self.balance)

        def __int__(self):
             return self.balance
        def reset(self):
            self.balance = 0

    playerName = input('enter your name please:')
    playerAcct = Account(playerName,1000)
    playerBal = playerAcct.__int__()
    p1=[]
    p1value=[]
    dealer=[]
    dealervalue=[]
    bets=[100]
    betreturn=[]
    usedbox = []

    def gameboardclear():
        p1.clear()
        p1value.clear()
        dealer.clear()
        dealervalue.clear()
        bets.clear()
        bets.append(100)
        betreturn.clear()
        for r in range(len(usedbox)):
            cut = usedbox[r].replace(usedbox[r][-1],'')
            if int(usedbox[r][-1]) == 1:
                deck1.append(cut)
            elif int(usedbox[r][-1]) == 2:
                deck2.append(cut)
            elif int(usedbox[r][-1]) == 3:
                deck3.append(cut)            
            elif int(usedbox[r][-1]) == 4:
                deck4.append(cut)         
            elif int(usedbox[r][-1]) == 5:
                deck5.append(cut)
            elif int(usedbox[r][-1]) == 6:
                deck6.append(cut) 

    def resetgame():
        gameboardclear()
        reseter = str((input('would you like to play again y/n?'))).lower()
        if reseter == 'y':
            playerBal = playerAcct.__int__()
            print(playerBal)
            if playerBal < 100:
                print('call yo mama for some money you do not have enuff! Hang your head in shame and Start A new identity!')
                BLACKJACK()
            else:
                gamestart()
        elif reseter == 'n':
            print('See you later!')
        else:
            print('y or n dude!')
            resetgame()


    def staycheck():
        if sum(dealervalue) == 21:
            print('House Wins')
            resetgame()
        elif sum(dealervalue) >21:
            print('XXXBust!XXX Player wins')
            playerAcct.dep(sum(bets))
            resetgame()
        elif sum(p1value) > sum(dealervalue):
            print(f'{playerName} Wins!')
            playerAcct.dep(sum(bets))
            resetgame()
        elif sum(p1value) < sum(dealervalue):
            print('House Wins')
            resetgame()
        elif sum(p1value) == sum(dealervalue):
            print("push!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            playerAcct.dep(sum(betreturn))
            resetgame()

    def dealerLOGIC():
        if sum(dealervalue) == 20:
            staycheck()
        elif sum(dealervalue)>sum(p1value):
            staycheck()
        elif sum(dealervalue)<sum(p1value):
            Dcarddeal()

    def wincheck():
        if sum(p1value) == 21:
            print(f'{playerName} Wins!')
            playerAcct.dep(sum(bets)+(sum(bets)*1.5))
            resetgame()
        elif sum(p1value) >21:
            print('XXXBust!XXX House Wins')
            resetgame()
        else:
            PlayerHitStay()



    def p1stay():
        p1.append('stay')
        print(f'You have {p1}')


    def PlayerHitStay():
        playerBal = playerAcct.__int__()
        try:
            hitstay = int(input("type 1 for hit or 2 for stay"))
            if hitstay == 1:
                carddeal()
            elif hitstay ==2:
                while True:
                    try:
                        betmore = int(input("type additional bet amt"))
                        if betmore > 0 and betmore < playerBal:
                            bets.append(betmore)
                            betreturn.append(betmore)
                            newbet = sum(bets)
                            bets.clear()
                            bets.append(newbet)
                            playerAcct.withd(betmore)
                            print(f'You have now placed a ${bets} bet')
                            p1stay()
                            Dcarddeal()
                            break
                        elif betmore == 0:
                            p1stay()
                            print(f'Your bet remains at ${bets}.')
                            Dcarddeal()
                            break
                        else:
                            print('error bet range')
                    except ValueError:
                        print("Noinput is not a number. It's a string")
            elif hitstay>2 or hitstay<1:
                PlayerHitStay()
            else:
                p1stay()
                print(f'Your bet remains at ${bets}.')
                Dcarddeal()
        except ValueError:
            print("Noinput is not a number. It's a string")
            PlayerHitStay()

    def carddeal():
        clear_output()
        import random
        decknum = random.randint(1,6)
        if decknum == 1:
            deck = deck1
        elif decknum == 2:
            deck = deck2
        elif decknum == 3:
            deck = deck3
        elif decknum == 4:
            deck = deck4
        elif decknum == 5:
            deck = deck5
        elif decknum == 6:
            deck = deck6
        pick = random.randint(0,len(deck)-1)
        print(f'{len(deck)} cards remain in deck{decknum}')
        print(f'{pick} is the random intgr.')
        usedbox.append(deck[pick]+str(decknum))
        print(usedbox)
        print(deck[pick].replace(deck[pick][-1],''))
        p1.append(deck[pick].replace(deck[pick][-1],''))
        if(deck[pick][0]) == "A":
            if sum(p1value)<11:
                p1value.append(11)
            else:
                p1value.append(1)
        elif(deck[pick][0]) == "1":
            p1value.append(10)    
        elif(deck[pick][0]) == "J":
            p1value.append(10)
        elif(deck[pick][0]) == "Q":
            p1value.append(10)
        elif(deck[pick][0]) == "K":
            p1value.append(10)
        else:
            try:
                v=int(deck[pick][0])
                p1value.append(v)
            except:
                print('no v')
        print(f'{playerName},You have {p1} that is {sum(p1value)} for {playerName}')
        deck.pop(pick)
        print(f'That card was picked from deck - {decknum}')    
        print(f'Dealer has{dealer} that is {sum(dealervalue)} for the Dealer')
        wincheck()


    def carddealStart():
        import random
        decknum = random.randint(1,6)
        if decknum == 1:
            deck = deck1
        elif decknum == 2:
            deck = deck2
        elif decknum == 3:
            deck = deck3
        elif decknum == 4:
            deck = deck4
        elif decknum == 5:
            deck = deck5
        elif decknum == 6:
            deck = deck6
        pick = random.randint(0,len(deck)-1)
        print(len(deck))
        print(pick)
        usedbox.append(deck[pick]+str(decknum))
        print(deck[pick])
        p1.append(deck[pick])
        if(deck[pick][0]) == "A":
            if sum(p1value)<11:
                p1value.append(11)
            else:
                p1value.append(1)
        elif(deck[pick][0]) == "1":
            p1value.append(10)    
        elif(deck[pick][0]) == "J":
            p1value.append(10)
        elif(deck[pick][0]) == "Q":
            p1value.append(10)
        elif(deck[pick][0]) == "K":
            p1value.append(10)
        else:
            try:
                v=int(deck[pick][0])
                p1value.append(v)
            except:
                print('no v')
        print(f'{playerName},You have {p1} that is {sum(p1value)} for {playerName}')
        deck.pop(pick)
        print(decknum)    

        import random
        decknumA = random.randint(1,6)
        if decknumA == 1:
            deckA = deck1
        elif decknumA == 2:
            deckA = deck2
        elif decknumA == 3:
            deckA = deck3
        elif decknumA == 4:
            deckA = deck4
        elif decknumA == 5:
            deckA = deck5
        elif decknumA == 6:
            deckA = deck6
        pickA = random.randint(0,len(deckA)-1)
        print(len(deckA))
        print(decknumA)
        usedbox.append(deckA[pickA]+str(decknumA))
        print(deckA[pickA])
        dealer.append(deckA[pickA])
        if(deckA[pickA][0]) == "A":
            if sum(dealervalue)<11:
                dealervalue.append(11)
            else:
                dealervalue.append(1)
        elif(deckA[pickA][0]) == "1":
            dealervalue.append(10)    
        elif(deckA[pickA][0]) == "J":
            dealervalue.append(10)
        elif(deckA[pickA][0]) == "Q":
            dealervalue.append(10)
        elif(deckA[pickA][0]) == "K":
            dealervalue.append(10)
        else:
            try:
                v=int(deckA[pickA][0])
                dealervalue.append(v)
            except:
                print('no v')
        print(f'Dealer has{dealer} that is {sum(dealervalue)} for the Dealer')
        deckA.pop(pickA)
        print(decknumA)    
        wincheck()


    def Dcarddeal():
        clear_output()
        import random
        decknum = random.randint(1,6)
        if decknum == 1:
            deck = deck1
        elif decknum == 2:
            deck = deck2
        elif decknum == 3:
            deck = deck3
        elif decknum == 4:
            deck = deck4
        elif decknum == 5:
            deck = deck5
        elif decknum == 6:
            deck = deck6
        pick = random.randint(0,len(deck)-1)
        print(len(deck))
        print(decknum)
        usedbox.append(deck[pick]+str(decknum))
        print(deck[pick])
        dealer.append(deck[pick])
        if(deck[pick][0]) == "A":
            if sum(dealervalue)<11:
                dealervalue.append(11)
            else:
                dealervalue.append(1)
        elif(deck[pick][0]) == "1":
            dealervalue.append(10)    
        elif(deck[pick][0]) == "J":
            dealervalue.append(10)
        elif(deck[pick][0]) == "Q":
            dealervalue.append(10)
        elif(deck[pick][0]) == "K":
            dealervalue.append(10)
        else:
            try:
                v=int(deck[pick][0])
                dealervalue.append(v)
            except:
                print('no v')
        print(f'{playerName},You have {p1} that is {sum(p1value)} for {playerName}')
        print(f'Dealer has{dealer} that is {sum(dealervalue)} for the Dealer')
        deck.pop(pick)
        print(decknum)
        dealerLOGIC()


    def gamestart():
        while True:
            try:
                p1bet = int(input("place your Bet:"))
                playerBal = playerAcct.__int__()
                if p1bet > 99 and p1bet < playerBal:
                    bets.append(p1bet)
                    betreturn.append(p1bet)
                    print(bets)
                    playerAcct.withd(p1bet)
                    print(f"{playerName} has placed a bet of {p1bet}")
                    print(playerBal)
                    carddealStart()
                    break
                else:
                    print("error bet range")
            except ValueError:
                print("Noinput is not a number. It's a string")



    gamestart()

BLACKJACK()