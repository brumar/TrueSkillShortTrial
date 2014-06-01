x = np.linspace(2,48,100)
bruno, jerem = Rating(25), Rating(25)  # assign  ratings
env=TrueSkill(draw_probability=0)
TrueSkill.DRAW_PROBABILITY=0x = np.linspace(2,48,100)
bruno, jerem = Rating(25), Rating(25)  # assign  ratings
env=TrueSkill(draw_probability=0)
TrueSkill.DRAW_PROBABILITY=0

def Pwin(rA=Rating(), rB=Rating()):
    deltaMu = rA.mu - rB.mu
    rsss = sqrt(rA.sigma**2 + rB.sigma**2)
    return TrueSkill().cdf(deltaMu/rsss)

def updateRatingsAndPrint(jeremVictoryList):
    global bruno
    global jerem
    for victoire in jeremVictoryList:
        if(victoire):
            jerem,bruno   = rate_1vs1(jerem, bruno,env=env)
        else:
            bruno, jerem = rate_1vs1(bruno, jerem,env=env)
    print(jerem,bruno)
    p1=plt.plot(x,mlab.normpdf(x,bruno.mu,bruno.sigma),color='r')
    p2=plt.plot(x,mlab.normpdf(x,jerem.mu,jerem.sigma),color='b')
    plt.show()
    print( "niveau de bruno en rouge \nniveau de jerem en bleu")
    print('Estimation à {:.1%} de chance pour jerem de gagner ses prochains matchs'.format(Pwin(jerem,bruno)))