# number of obs 
obs_u = titanic.loc[titanic.d == 0].shape[0] # for control group (non first class)
obs_t = titanic.loc[titanic.d == 1].shape[0] # for treatment group (first class)
obs = titanic.shape[0]

def weighted_avg_effect(df, effect = 'ate'):
    
    diff = df[df.d==1].survived_d.mean() - df[df.d==0].survived_d.mean()
    
    if effect == 'ate':
        weight = df.shape[0]/obs
    elif effect == 'att':
        weight = df[df.d==1].shape[0]/obs_t
    elif effect == 'atu':
        weight = df[df.d==0].shape[0]/obs_u
        
    return diff*weight

wate = titanic.groupby('s').apply(lambda x: weighted_avg_effect(x, 'ate')).sum()
watt = titanic.groupby('s').apply(lambda x: weighted_avg_effect(x, 'att')).sum()
watu = titanic.groupby('s').apply(lambda x: weighted_avg_effect(x, 'atu')).sum()

print("The weigthted average treatment effect estimate is {:.2%}".format(wate))
print("The weigthted average treatment effect on the treated estimate is {:.2%}".format(watt))
print("The weigthted average treatment effect on the untreated estimate is {:.2%}".format(watu))