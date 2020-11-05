def optimal(array):
    max_return=0
    max_f=0
    for f in range(100):
        HPR_array=1
        for each in array:
            HPR_array*=1+((f+1)/100)*(-each/min(array))
        if HPR_array>max_return:
            max_return = HPR_array
            max_f=f+1

    print("Best %: "+str(max_f))
    print("Expected total return rate: "+str(max_return))
    print("expoential average rate per trade: "+str(max_return**(1/len(array))))
optimal([18,8,-7,10,-11,-5,-3,20,12,-15])
#optimal([1.2,-1])
def kelly(array):
    win=0
    lose=0
    total_win=0
    total_lose=0
    for i in array:
        if i>0:
            win+=1
            total_win+=i
        elif i<0:
            lose+=1
            total_lose+=i
            
    winrate=win/(win+lose)
    
    ratio=total_win/-total_lose
    print("Best %: "+str((winrate*(1+ratio)-1)/ratio*100))
    
#kelly([19,8,-7,10,-11,-5,-3,20,12,-15])
def prob_kelly(p,b):
    print((p*(1+b)-1)/b*100)
#prob_kelly(0.8,1.25)
