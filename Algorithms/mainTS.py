from MPK import MKP
import numpy as np

pb = 1
mkp = MKP(pb)
# print(mkp.profit, mkp.weight, mkp.cap)
idx_best = mkp.initsol()
for i in range(len(idx_best)):
    idx_best[i] = list(map(int, idx_best[i, :]))
it_idx_best = idx_best
weight_best, best, x_best = 0, 0, 0
tabu = [[None]]
it, stopcrit = 0, 0
tenure = 10
lim_it = 500
n_best = 0

while stopcrit == 0:
    it += 1
    it_best = 0
    sols = mkp.neighbors(it_idx_best)
    shp = np.shape(sols)
    for x, s in enumerate(sols):
        istabu = 0
        for tab in tabu:
            if (s == tab).all():
                print('TABU')
                break
            elif mkp.objfun(s, 't')[0] > it_best:
                it_best, it_best_weight = mkp.objfun(s, 't')
                it_idx_best = s
                it_x_best = x
                if it_best > best:
                    n_best = it
                    best = it_best
                    idx_best = it_idx_best
                    weight_best = it_best_weight

    if len(tabu) > tenure:
        del tabu[0:shp[0]]
    tabu.append(s for s, x in enumerate(sols) if x != it_x_best)

    print('It', it, ', Best', best)
    # if best > .9 * mkp.sol:
    if it == lim_it:
        # print(tabu)
        stopcrit = 1
        print('\nFinal Profit -', best)
        print('Optimal Profit -', mkp.sol)
        print('\nFinal Weight -', weight_best)
        print('Maximum Weight -', sum(mkp.cap))
        print('\nFinal Solution - it ', n_best, ':\n', idx_best)
    # if :
    #    stopcrit = 1
    #    print('90% of optimal solution achieved')
    #    print('Final Profit - ', best)
    #    print('Final Weight - ', weight_best)
