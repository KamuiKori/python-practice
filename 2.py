from functools import lru_cache
import itertools
import numpy_financial as nmp

# Компания осуществляет услуги по ремонту мобильных устройств для обычных людей

N = 8  # Срок реализации, количество периодов
r = 0.18  # Ставка дисконтирования
RZ = 300000  # Расходы за период
RD = 800000  # Доходы за период
PZ = 400000  # Первоначальные затраты


@lru_cache(maxsize=None)


def NPV(t, rate):
    return ((RD - RZ) / (1 + rate) ** t + NPV(t - 1, rate)) if t != 0 else -PZ

def DPP(t):
    NPVfirst = []
    NPVsecond = []
    n = 1
    m = 0
    for n in range(t+1):
        NPVfirst.append((RD - RZ)/(1 + r)**n)
        NPVfirst[0] = -1 * PZ
    print('NPV: ' + str(NPVfirst))
    NPVsecond = itertools.accumulate(NPVfirst)
    NPVSecondList = list(NPVsecond)
    print('NPV накопленный: ' + str(NPVSecondList))
    for x in NPVSecondList:
        if x < 0:
            m = NPVSecondList.index(x)
    NPVM = NPVfirst[m+1]
    NPVZAM = NPVSecondList[m]
    DPP = m + (abs(NPVZAM)/NPVM)
    return DPP

print('DPP проекта = ' + str(DPP(N)))
print('NPV проекта = ' + str(NPV(N, r)))