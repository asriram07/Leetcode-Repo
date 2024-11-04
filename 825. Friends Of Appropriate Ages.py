"""
825. Friends Of Appropriate Ages
Solved
Medium
Topics
Companies
There are n persons on a social media website. You are given an integer array ages where ages[i] is the age of the ith person.

A Person x will not send a friend request to a person y (x != y) if any of the following conditions is true:

age[y] <= 0.5 * age[x] + 7
age[y] > age[x]
age[y] > 100 && age[x] < 100
Otherwise, x will send a friend request to y.

Note that if x sends a request to y, y will not necessarily send a request to x. Also, a person will not send a friend request to themself.

Return the total number of friend requests made."""

Idea : Use binary search to search for lower and higher bounds

class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages
        ages.sort()
        n = len(ages)
        i = n - 1
        count = 0
        d1 = Counter(ages)
        #print(ages)
        while(i>=1):
            low = bisect.bisect_left(ages, (ages[i]//2 + 8))
            
            #print(low, i , count)
            if(i>low):
                count = count + i - low
            if(ages[i]>(0.5*ages[i] + 7)):
                count+=(d1[ages[i]]-1)
                d1[ages[i]]-=1
            i-=1
        
        return count
    
"""
Progression : 

Step - 1: 
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()
        n = len(ages)
        i = n - 1
        count = 0
        d1 = Counter(ages)
        while(i>=1):
            for j in range(i-1,-1,-1):
                if(ages[i]>100 and ages[j]<100):
                    break
                if(ages[j]<=(0.5*ages[i] + 7)):
                    break
                count+=1
            count+=(d1[ages[i]]-1)
            i-=1
        return count
Step - 2 
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages
        ages.sort()
        n = len(ages)
        i = n - 1
        count = 0
        d1 = Counter(ages)
        print(ages)
        while(i>=1):
            for j in range(i-1,-1,-1):
                #print(i-1, j, ages[j])
                # if(ages[i]>100 and ages[j]<100):
                #     break
                if(ages[j]<=(0.5*ages[i] + 7)):
                    break
                count+=1
            count+=(d1[ages[i]]-1)
            d1[ages[i]]-=1
            #print(ages[i],count)
            i-=1
        return count
Step - 3 :
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages
        ages.sort()
        n = len(ages)
        i = n - 1
        count = 0
        d1 = Counter(ages)
        print(ages)
        while(i>=1):
            for j in range(i-1,-1,-1):
                if(ages[j]<=(0.5*ages[i] + 7)):
                    break
                count+=1
            if(ages[i]>(0.5*ages[i] + 7)):
                count+=(d1[ages[i]]-1)
                d1[ages[i]]-=1
            i-=1
        return count

"""
