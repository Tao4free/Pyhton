def epsilonSoft(numEpisode=1, visitmode="first", discount_rate=1.0, epsilon=0.1, policymode="off", weighted=False, drawpath=False):
    print("epsilonSoft")
    print(numEpisode)
    print(visitmode)

def learn(**kwarg):
    print("learn")
    epsilonSoft(**kwarg)

kwarg = dict(numEpisode=3)#, visitmode="first", discount_rate=1.0, epsilon=0.1, policymode="off", weighted=False, drawpath=False)
learn(**kwarg)
