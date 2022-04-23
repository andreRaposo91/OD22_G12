from os.path import abspath
import numpy as np


def load(pb):
    if pb == 1 or pb == 2:
        path = r"C:\Users\Andre Raposo\Documents\Andre\Universidade\4º Ano - 2º Semestre\OD\Project\OD22_G12\Problems\site\p0" \
               + str(pb)
        with open(path + '_c.txt', 'r') as cp:
            cf = cp.read()

        with open(path + '_w.txt', 'r') as wp:
            wf = wp.read()

        with open(path + '_p.txt', 'r') as pp:
            pf = pp.read()

        with open(path + '_s.txt', 'r') as sp:
            sf = sp.read()

        c = list(map(int, cf.split()))
        w = [None] * len(c)
        for i in range(len(c)):
            w[i] = list(map(int, wf.split()))
        p = list(map(int, pf.split()))
        s = np.zeros((len(c), len(w[0])))
        for i in range(len(c)):
            s[i, :] = list(map(int, sf.split()))[i::len(c)]

        return c, w, p, s

    elif pb == 3 or pb == 4:
        path = r"C:\Users\Andre Raposo\Documents\Andre\Universidade" \
            r"\4º Ano - 2º Semestre\OD\Project\OD22_G12\Problems\sac94-suite"
        print(path)
        if pb == 3: path += r'\FLEI.DAT'
        elif pb == 4: path += r'\SENTO1.DAT'

        file = open(path, 'r')
        fid = file.read()
        lines = fid.split('\n')
        n_c, n_p = int(lines[0].split()[0]), int(lines[0].split()[1])
        n_r = len(lines[1].split())
        if n_c % n_r == 0:
            n_lc = int(n_c/n_r)
        else: n_lc = int(n_c/n_r) + 1
        if n_p % n_r == 0:
            stp = int(n_p/n_r)
        else: stp = int(n_p/n_r) + 1
        p = []
        for i in range(1,stp+1):
            p.extend(list(map(int, lines[i].split())))
        c = []
        if n_c % n_r == 0:
            n_lc = int(n_c/n_r)
        else: n_lc = int(n_c/n_r)+1
        for i in range(stp+1, stp+n_lc+1):
            c.extend(list(map(int, lines[i].split())))
        w = [[None] * n_p] * n_c
        for cc in range(n_c):
            ww = []
            for i in range(n_lc+stp*(cc+1)+1, n_lc+stp*(cc+2)+1):
                ww.extend(list(map(int, lines[i].split())))
            for wi in range(len(ww)):
                if ww[wi] == 0:
                    ww[wi] = 1e6
            w[cc] = ww
        s = list(map(int, lines[1+stp+n_lc+stp*n_c+1].split()))

        return c, w, p, s

    else:
        ValueError('Problem does not exist, choose 1 or 2 for a small problem,'
            '3 or 4 for a large problem')
