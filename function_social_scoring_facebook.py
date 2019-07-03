#dataset interpolasi
def interpolasi(X, kind):
    index=True
    if kind=='share':
        if X<102:
            x=[0,49,97.2,101]
            y=[0,17.5,26.2,26.6]
        elif X<200:
            x=[101,188.4,207,258.7]
            y=[26.6,32.6,33.1,34.1]
        elif X<536:
            x=[188.4,207,258.7,536]
            y=[32.6,33.1,34.1,35]
        else:
            Y=35
            index=False
            
    elif kind=='like':
        if X<52:
            x=[0,13.6,29.5,52.6]
            y=[0,1.1,2.2,3.6]
        elif X<82:
            y=[3.6,4.1,4.8,5]
            x=[52.6,62.7,76.4,82]
        elif X<140:
            x=[82,130.9,142,146.6]
            y=[5,6.7,7,7.1]
            
        elif X<210:
            x=[142,146.6,162.1,216.6]
            y=[7,7.1,7.5,8.4]            
            
        elif X<300:
            x=[162.1,216.6,282.9,323.8]
            y=[7.5,8.4,9.1,9.4]
            
        elif X<600:
            x=[323.8,394.7,429.4,600]
            y=[9.4,9.6,9.7,9.9]
            
        else:
            Y=10
            index=False 

    elif kind=='friend':
        if X<600:
            x=[0,205,484,573]
            y=[0,0.7,1.5,1.8]
        elif X<1000:
            x=[622,700,800,945]
            y=[1.9,2.3,2.7,2.9]
        elif X<2600:
            x=[1195,1370,2358,2557]
            y=[3.6,4.1,6.8,7.3]
        elif X<4000:
            x=[2700,3000,3500,4000]
            y=[7.5,8.1,9.2,11]
        elif X<9100:
            x=[4500,5555,7526,9070]
            y=[12,14,17.5,19.8]
        elif X<82526:
            x=[20094,21935,35129,82526]
            y=[29.5,30.4,33.6,35]
        else:
            Y=35
            index=False 
    if index==True:
        L0=(X-x[1])/(x[0]-x[1])*(X-x[2])/(x[0]-x[2])*(X-x[3])/(x[0]-x[3])*y[0]
        L1=(X-x[0])/(x[1]-x[0])*(X-x[2])/(x[1]-x[2])*(X-x[3])/(x[1]-x[3])*y[1]
        L2=(X-x[0])/(x[2]-x[0])*(X-x[1])/(x[2]-x[1])*(X-x[3])/(x[2]-x[3])*y[2]
        L3=(X-x[0])/(x[3]-x[0])*(X-x[1])/(x[3]-x[1])*(X-x[2])/(x[3]-x[2])*y[3]

        Y=L1+L0+L2+L3

    return Y

def result_SA(share,like,friend,page, group, sub=None):
    """Summary or Description of the Function

    Parameters:
    share (float)    : average shares
    like (float)     : average likes
    friend (int)     : friends count
    page (int)       : number of pages followed
    group (int)      : number of groups followed
    subscriber (int) : subscribers count, if None default = friends count*bobot
    
    Returns:
    float:Returning value in percent

   """
    
    friend=friend*16.6
    
    if sub==None:
        sub=friend
        
    group_page=page/20+group/20
    
    SA=interpolasi(share,'share')+interpolasi(like,'like')+\
        interpolasi(friend,'friend')/3.5+group_page+interpolasi(sub,'friend')
        
    return float("{:.2f}".format(SA))

#example
print(result_SA(1,1,2,3,4,5))