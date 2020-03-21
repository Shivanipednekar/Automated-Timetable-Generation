
import random
random.seed()
slots = 8
subjects = ['a','b','c','d']
def newEmptyDay():
    day = [None for x in range(slots)]
    slot = random.randint(0,slots-1)
    if slot == 3 or slot == 7:
            return assignPrac()    
    day[slot] = 'prac'
    day[slot + 1] = 'prac'
    return day


def isSubAssignable(day,sub):
    count = 0
    for x in day:
        if x == sub:
            count = count + 1
    if count < 2:
        return True
    else:
        return False


def getAssignableSub(day):
    subIndex = random.randint(0,len(subjects)-1)
    sub = subjects[subIndex]
    if(isSubAssignable(day,sub)):
        return sub
    else:
        return getAssignableSub(day)


def assignSlot(day,sub):
    slot = random.randint(0,slots-1)
    if day[slot]:
        return assignSlot(day,sub)
    else:
        day[slot] = sub
        return day

def newDay():
    day = newEmptyDay()
    for x in range(slots-2):
        day = assignSlot(day,getAssignableSub(day))
    return day

newDay()
