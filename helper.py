
def rook_mean(lst):       # will allow me to pull the first three entries for each player. The 'rookie' statistics
    return lst[:3].mean()


def fourth_year(lst):     # will allow me to pull the fourth entry of a players info. 
    if len(lst) >= 4:     # will be used on salary to determine
        return lst[3]
    else:
        return 0
    
    
def scaler(x):
    # credit to stereopickle
    mean = x.mean()
    std = x.std()
    return (x-mean)/std

def df_scaler(df, cols):
    # credit to stereopickle
    df0 = df.copy()
    for c in cols:
        df0[f"{c}_sc"] = scaler(df0[c])
        df0 = df0.drop(c, axis = 1)
    return df0