import chess
import chess.engine
import os

def numextract(x):
    start = x.index("(",11)
    end = x.index(')')
    return x[start+1:end]
movelist=[]
evallist=[]

#here we assume the engine file is in same folder as our python script
path = r'C:\Users\kwanv\Desktop\Programming\Projects\Chess Risk'
#Let's try our code with the starting position of chess:
fen = 'r1bqkb1r/ppp2ppp/2pn4/4P3/8/5N2/PPP2PPP/RNBQ1RK1 b kq - 0 7'
board = chess.Board(fen)
#Now make sure you give the correct location for your stockfish engine file
#...in the line that follows by correctly defining path
engine = chess.engine.SimpleEngine.popen_uci(path+'/'+'stockfish_20011801_x64')



whitewinning=0
blackwinning=0
draw = 0


for lm in board.legal_moves:
    info = engine.analyse(board, chess.engine.Limit(depth=20), root_moves=[lm])
    
    t = str(info["score"])#check for mate?

    ceval=int(numextract(t))
    if board.turn == False:
        ceval *= -1
    if (ceval>0):
        whitewinning+= 1
    elif ceval == 0:
        draw += 1
    else:
        blackwinning+= 1
    print(str(board.san(lm)),"\t eval = ", ceval)

print('white winning = ',whitewinning)
print('black winning = ',blackwinning)
print('draw = ',draw)

#[x for _,x in sorted(zip(Y,X))]

engine.quit()
