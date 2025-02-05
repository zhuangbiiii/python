
import random


def _func_(playerNum):
    dnumbermin = 1
    dnumbermax = 1
    nnumbermax = 0
    while ((playerNum - dnumbermax - nnumbermax) / playerNum > 0.66):
        if ((dnumbermax - 1) > nnumbermax) :
            nnumbermax += 1
        else :
            dnumbermax += 1
    ducknum = random.randint(dnumbermax - 2,dnumbermax)
    neutralnum = random.randint(nnumbermax - 1,nnumbermax)
    CurrentDuckNum = CurrentGooseNum = CurrentNeutralNum = 0
    CurrentDuckNum += dnumbermin
    CurrentGooseNum += playerNum - ducknum - neutralnum - CurrentDuckNum - CurrentNeutralNum

    while (CurrentGooseNum + CurrentDuckNum + CurrentNeutralNum < playerNum):
        if (CurrentDuckNum < ducknum):
            CurrentDuckNum += 1
        elif (CurrentNeutralNum < neutralnum):
            CurrentNeutralNum += 1
        else:
            CurrentGooseNum += 1

    print(playerNum,CurrentGooseNum,CurrentDuckNum,CurrentNeutralNum)


def _Main_():
    print("Player team number generate test :\nGoose number, Duck number, Neutral number")
    for a in range(0,10):
        for b in range(2,16):
            _func_(b)

_Main_()