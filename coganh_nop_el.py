import copy
def move(board,player):
    des=[]
    scores=[]
    thecomo=False
    m=-1
    n=-1
    score=-17
    for i in range(5):
        for j in range(5):
            if board[i][j]==player:
                b=copy.deepcopy(board)
                if (i+j)%2==0:
                    
                    score,m,n,thecomo=testmove(b,player,i,j,tam=True)
                    
                else:
                    score,m,n,thecomo=testmove(b,player,i,j,tam=False)
                if thecomo==True:
                    return ((i,j),(m,n))
                des.append(((i,j),(m,n)))
                scores.append(score)
    max_score=scores[0]
    result=des[0]
    for k in range(1,len(scores)):
        if scores[k]>max_score:
            max_score=scores[k]
            result=des[k]
    return result
def testmove(b,player,i,j,tam): #thu di chuyen ra xung quanh vi tri i,j
    if tam==True:
        des=des8(i,j)
    else:
        des=des4(i,j)
    scores=[]
    thecomo=False
    des_=[]
    for d in des:
        m=d[0]
        n=d[1]
        if b[m][n]==0:
            des_.append(d)
    for d in des_:
        
        b_=copy.deepcopy(b)
        m=d[0]
        n=d[1]
       
        b_[m][n]=b_[i][j]
        b_[i][j]=0
        b1=copy.deepcopy(b_)
        b2=copy.deepcopy(b_)
        value_ganh=check_ganh(b1,m,n,player) #m,n la vi tri quan di chuyen vao
        value_vay = check_vay(b2,m,n,player) #m,n la bi tri quan di chuyen vao
        if value_ganh==0 and value_vay==0:
            b3=copy.deepcopy(b_)
            thecomo=check_the_co_mo(b3,i,j,player) #i,j la vi tri bo trong sau khi di chuyen quan
        if thecomo==True:
            return -1,m,n,thecomo
        if value_ganh>=value_vay:
            scores.append(value_ganh)
        else:
            scores.append(value_vay)
   
    score=0
    if len(scores)!=0:
        max_score=scores[0]
        m=des_[0][0]
        n=des_[0][1]
        for k in range(1,len(scores)):
            if scores[k]>max_score:
                max_score=scores[k]
                m=des_[k][0]
                n=des_[k][1]
        score=max_score
    return score,m,n,thecomo
def des8(i,j):
    des=[]
    for m in range(i-1,i+2):
        for n in range(j-1,j+2):
            if checkOnBoard(m,n)==True and (m!=i or n!=j):
                des.append((m,n))
    return des
def des4(i,j):
    des=[]
    
    for d in [(i-1,j),(i,j-1),(i,j+1),(i+1,j)]:
        if checkOnBoard(d[0],d[1])==True:
            des.append(d)
    return des



def check_ganh(s,i,j,player):
    e=eval(s,player)
    k=i-1
    for m in range(j-1,j+2): # xet truong hop Ganh
        if checkOnBoard(k,m) and checkOnBoard(i*2-k,j*2-m):
            if s[k][m]==s[i*2-k][j*2-m]==-s[i][j]:
                s[k][m]=s[i][j]
                s[i*2-k][j*2-m]=s[i][j]
                
    if checkOnBoard(i,j-1) and checkOnBoard(i,j+1):
        if s[i][j-1]==s[i][j+1]==-s[i][j]:
            s[i][j-1]=s[i][j]
            s[i][j+1]=s[i][j]

    return eval(s,player) -e 
def check_vay(b_vay,i,j,player):
    
    e=eval(b_vay,player)
    if (i+j)%2==0:
        des=des8(i,j)
    else:
        des=des4(i,j)
    for d in des: #cac diem co the bi vay la o xung quanh o di chuyen den
        m=d[0]
        n=d[1]
        dk=True
        if b_vay[m][n]!=-player:
            continue
        if (m+n)%2==0:
            des_=des8(m,n)
        else:
            des_=des4(m,n)
        for d_ in des_:
            x=d_[0]
            y=d_[1]
            if b_vay[x][y]==player:
                continue
            else:
                dk=False
                break
        if dk==True:
            b_vay[m][n]=player
    return eval(b_vay,player)-e
        



def check_the_co_mo(b_mo,i,j,player): #i,j la vi tri trong
    doithu=-player
    if (i+j)%2==0:
        des=des8(i,j)
    else:
        des=des4(i,j)
    for d in des:
        m=d[0]
        n=d[1]
        if b_mo[m][n]==player or b_mo[m][n]==0:
            continue
        b_mo[m][n]=0
        b_mo[i][j]=doithu
        e=check_ganh(b_mo,i,j,player)
        if e!=0:
            return True
    return False
        

def checkOnBoard(x,y): #kiem tra xem co nam trong bang hay khong 
    return 0<=x<5 and 0<=y<5
def eval(board,player):
    eval_player=0
    eval_p=0
    for i in range(5):
        for j in range(5):
            if board[i][j]==player: eval_player+=1
            elif board[i][j]==-player: eval_p+=1
    return eval_player-eval_p
