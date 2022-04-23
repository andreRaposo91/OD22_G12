from loadfiles import load
import sys
import numpy as np
import random as rd

sys.path.append(r"C:\Users\Andre Raposo\Documents\Andre\Universidade"
                r"\4º Ano - 2º Semestre\OD\Project\OD22_G12")


class MKP:
    def __init__(self, pb):
        [c, w, p, s] = load(pb)
        self.cap = np.asarray(c)
        self.weight = np.asarray(w)
        self.profit = np.asarray(p)
        if pb == 3 or pb == 4:
            self.sol = s
        else:
            self.sol = self.objfun(np.asarray(s), 't')[0]
        self.wi, self.ci = rd.randint(0, len(w[1])-1), rd.randint(0, len(c)-1)
        # self.wi, self.ci = 0, 0

    def initsol(self):
        return np.zeros((len(self.cap), len(self.weight[0])))

    def objfun(self, idx, flag):
        kprofit, kweight = [None] * len(self.cap), [None] * len(self.cap)
        for i in range(len(self.cap)):
            kprofit[i] = sum(np.multiply(idx[i], self.profit))
            kweight[i] = sum(np.multiply(idx[i], self.weight[i]))
        if flag == 'i':
            return kprofit, kweight
        elif flag == 't':
            total_profit = sum(kprofit)
            total_weight = sum(kweight)
            return total_profit, total_weight

    def neighbors(self, idxi):
        sols = []
        if self.wi == len(self.weight[0]): self.wi = 0
        if self.ci == len(self.cap): self.ci = 0
        for cc in range(self.ci, len(self.cap)):
            for ww in range(self.wi, len(self.weight[0])):
                idx = idxi
                if any(self.objfun(idx, 'i')[1] > self.cap):
                    dx = 0
                else: dx = 1
                if self.weight[cc, ww] == 0 or self.weight[cc, ww] == 1e6:
                    idx[cc, ww] = 0
                else: idx[cc, ww] = dx
                met = self.objfun(idx, 'i')
                checkw = []
                for tw, kw in zip(met[1], self.cap):
                    checkw.append(tw < kw)
                if sum(idx[:, ww]) < 2 and all(checkw) is True:
                    sols.append(idx)

        self.wi += 1
        self.ci += 1
        return sols
