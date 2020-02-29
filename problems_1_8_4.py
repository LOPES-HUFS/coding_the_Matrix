L=[2,3,4,5]
A=((1,3),(4,5))
B=((10,20),(30,40))
d={'thank you':'merci', 'goodbye':'au revoir'}

#문제 1.8.4.
def inv_dict(d):
    k={ j:i for i,j in d.items()}
    print(k)
