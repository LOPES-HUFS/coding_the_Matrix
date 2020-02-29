d={'thank you':'merci', 'goodbye':'au revoir'}

#문제 1.8.4.
def inv_dict(d):
    k={ j:i for i,j in d.items()}
    print(k)
