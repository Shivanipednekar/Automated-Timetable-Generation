
import random
random.seed()
slots = 8
halfslot = 4
subjects = ['a','b','c','d','free']
maxSubWeek = 4
daysInWeek = 4
def newEmptyDay():
    day = [None for x in range(slots)]
    slot = random.randint(0,slots-1)
    if slot == 3 or slot == 7:
            return newEmptyDay()    
    day[slot] = 'prac'
    day[slot + 1] = 'prac'
    return day

def newHalfDay():
    day = [None for x in range(slots)]
    for x in list(range(halfslot,slots)):
        day[x] = 'free'
    slot = random.randint(0,halfslot)
    if slot == 3:
            return newHalfDay()
    day[slot] = 'prac'
    day[slot + 1] = 'prac'
    return day


def isDupSubjectPresent(day):
    for subject in subjects:
        count = 0
        for daySub in day:
            if subject == daySub:
                count = count + 1
        if count > 1:
            return subject
    return False
            

def isSubAssignable(day,sub):
    if isDupSubjectPresent(day):
        maxCount = 1
    else:
        maxCount = 2
    count = 0
    for x in day:
        if x == sub:
            count = count + 1
    if count < maxCount:
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

def newDay(halfDay = False):
    random.seed()
    if halfDay:
        day = newHalfDay()
        lecs = halfslot - 2
    else:
        day = newEmptyDay()
        lecs = slots-2
    for x in range(lecs):
        day = assignSlot(day,getAssignableSub(day))
    return day

def isDayValid(week,day):
    subjectCount = {'prac':0, 'free':0}
    for x in subjects:
        subjectCount[x] = 0
    tempWeek = []
    for weekday in week:
        tempWeek.append(weekday)
    tempWeek.append(day)
    for weekday in tempWeek:
        for subject in weekday:
            subjectCount[subject] = subjectCount[subject] + 1
    for subject in subjectCount:
        if not subject == 'prac' and not subject == 'free':
            if subjectCount[subject] > maxSubWeek:
                return False
    return True

def newTimeTable():
    week = []
    while len(week) < daysInWeek:
        if(len(week) == 1):
            day = newDay(True)
        else:
            day = newDay()
        if isDayValid(week,day):
            week.append(day)
    return week

print(newTimeTable())
