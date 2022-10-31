import operator
#==============================================================================
def get_rel_matr(A, R):
    lis = sorted( list(A) )
    matr = []
    for i in range( len(lis) ):
        row = []
        for j in range( len(lis) ):
            row.append( R( lis[i], lis[j] ) )
        matr.append(row)
    return matr
#==============================================================================
def is_refl(matr):
    for x in range( len(matr) ):
        if not matr[x][x]:
            return False
    return True
#==============================================================================
def is_antisymm(matr):
    for x in range( len(matr) ):
        for y in range( x, len(matr) ):
            if matr[x][y] and matr[y][x]:
                if x != y:
                    return False
    return True
#==============================================================================
def is_transitive(matr):
    for x in range( len(matr) ):
        for y in range( len(matr) ):
            for z in range(len(matr)):
                if matr[x][y] and matr[y][z]:
                    if not matr[x][z]:
                        return False
    return True
#==============================================================================
def get_rel_prop(matr):
    res = ['Отношение обладает следующими свойствами:']
    res.append( ' рефлексивность,'    if is_refl(matr)          else '' )
    res.append(' антисимметричность,' if is_antisymm(matr)      else '' )
    res.append(' транзитивность,'     if is_transitive(matr)    else '' )
    s = ''.join( res )
    if s[-1] == ',':
        s = s[:-1] + '.'
    return s
#==============================================================================
A={3,3,3,3}
m = get_rel_matr( A, operator.le )
print(m)
print( get_rel_prop(m) )