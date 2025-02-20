'''
Name: Garrett Kolenbrander
Date: 21/2/25
Program Description: Kattis problem bijele:
https://open.kattis.com/problems/bijele
Algorithm Steps:
    Input 6 numbers separated by a space
    Set varibles for # pieces there are supposed to be
    Write 6 line, one for each set of pieces, 
        taking the difference between actual pieces and pieces required
'''

def solution(dif1, dif2, dif3, dif4, dif5, dif6):
    print(dif1, dif2, dif3, dif4, dif5, dif6)


king, queen, rooks, bishops, knights, pawns = map(int, input().split())

req_king = 1
req_queen = 1
req_rooks = 2
req_bishops = 2
req_knights = 2
req_pawns = 8
#FIXED3,4

dif1 = req_king - king
dif2 = req_queen - queen
dif3 = req_rooks - rooks
dif4 = req_bishops - bishops
dif5 = req_knights - knights
dif6 = req_pawns - pawns
#FIXED5,6

solution(dif1, dif2, dif3, dif4, dif5, dif6)


