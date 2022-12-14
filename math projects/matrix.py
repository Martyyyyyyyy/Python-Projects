import operator
import random
m = int(input('Введіть к-сть рядків = '))
n = int(input('Введіть к-сть стовпців = '))
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
    res = ['Матриця має такі властивості:']
    res.append(' рефлексивність,'    if is_refl(matr)          else '' )
    res.append(' антисимметричність,' if is_antisymm(matr)      else '' )
    res.append(' транзитивність,'     if is_transitive(matr)    else '' )
    s = ''.join( res )
    if s[-1] == ',':
        s = s[:-1] + '.'
    return s
   
#==============================================================================
Matrix = [ [ random.randint(1, 11) for j in range(n)] for i in range(m) ]
print('Matrix:')
for i in range(m):
    print(Matrix[i])
A={3,3,3,3}
m = get_rel_matr( A, operator.le )
print(m)
print( get_rel_prop(m) )
print('Матриця є частковим порядком')