verbose = False

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
    slot = random.randint(0,halfslot-1)
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


def assignSlot(day,sub,halfDay):
    slot = 0
    if halfDay:
        slot = random.randint(0,halfslot-1)
    else:
        slot = random.randint(0,slots-1)
    if day[slot]:
        return assignSlot(day,sub,halfDay)
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
        day = assignSlot(day,getAssignableSub(day),halfDay)
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
    if verbose:
        print(subjectCount) 
    for subject in subjectCount:
        if not subject == 'prac' and not subject == 'free':
            if subjectCount[subject] > maxSubWeek:
                return False
    return True

def newTimeTable():
    week = []
    loop = 1
    while len(week) < daysInWeek:
        if verbose:
            print("Current week: ")
            print(week)
        if(len(week) == 1):
            day = newDay(True)
        else:
            day = newDay()
        if verbose:
            print("Generated Day: ")
            print(day)
        if isDayValid(week,day):
            week.append(day)
        loop = loop + 1
        if loop > 100: #you have missed some rule (edge case) here because of which is goes in forever loop. This is to restart the process if that happens
            if verbose:
                print("Restarting because of infinite loop")
            return newTimeTable()
    return week

timetable = newTimeTable()
print('Generated timetable is:')
print(timetable)
