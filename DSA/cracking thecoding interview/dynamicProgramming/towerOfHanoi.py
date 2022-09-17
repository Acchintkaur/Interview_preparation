def Towers_Of_Hanoi(numdisks, frm_disc, to_disc, aux_disc):
    if numdisks == 1:
        print("Move disk [1] from rod [",frm_disc, "] to rod {", to_disc, '}')
        return
    Towers_Of_Hanoi(numdisks-1, frm_disc, aux_disc, to_disc)
    print("Move disk ["+str(numdisks) + "] from rod [",str(frm_disc)+" ] to rod {", to_disc, '}')
    Towers_Of_Hanoi(numdisks-1, aux_disc, to_disc, frm_disc)


numdisks = 4
Towers_Of_Hanoi(numdisks, 'A', 'C', 'B')

# A C B
# A B C
# B C A