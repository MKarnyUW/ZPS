import numpy as np
import matplotlib.pyplot as plt

def tr_new(t1,r1,t2,r2):
    return t1*t2/(1+np.conjugate(r1)*r2*t1/np.conjugate(t1)),r1+t1*t1*r2/(1+np.conjugate(r1)*r2*t1/np.conjugate(t1))

def transmitance(tm,rm,pos):
    dist=[]
    for i in range(len(pos)-1):
        dist.append(pos[i+1]-pos[i])
    def T(k):
        t,r=tm,rm
        for l in dist:
            t,r=tr_new(t,r,np.exp(l*k*1j),0)
            t,r=tr_new(t,r,tm,rm)
        return abs(t)**2
    return T

def plot(t,r,pos,kmin,kmax):
    T=transmitance(t,r,pos)
    kspace=np.linspace(kmin,kmax,250)
    Tspace=[]
    for k in kspace:
        Tspace.append(T(k))
    plt.figure(dpi=200)
    plt.plot(kspace,Tspace,color='r',linestyle='-',linewidth=1)
    plt.show()

plot(1/np.sqrt(2),1/np.sqrt(2),[0,1,np.sqrt(2)],0,10)