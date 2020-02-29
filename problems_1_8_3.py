L=[2,3,4,5]
A=((1,3),(4,5))
B=((10,20),(30,40))
d={'thank you':'merci', 'goodbye':'au revoir'}

#문제 1.8.3.
def tuple_sum(A,B):
    k=[A[i]+B[i] for i in list(range(len(A)))]
    print(k)
