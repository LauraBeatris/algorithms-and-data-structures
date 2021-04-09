companiesList = ['twitter', 'spotify', 'tiktok', 'tinder', 'google']
companiesLargeList = ['twitter', 'facebook'] * 100000

def findTwitter(companies): 
    for company in companies:
        if company != 'twitter': continue 

        print('Found twitter')

findTwitter(companiesLargeList)

# 

"""
Big O Notation of findTwitter: O(n) - Linear time (Always based on the worst case scenario)

- Best case: Linear time 
- Average case: Linear time 
- Worst case: Linear time 

Why Linear time? 

Because the worst-case scenario would be, for instance, an array of one million items
and the number of operations executed would increase linearly according to the input size 

What's the Bio O Notation for Linear time? 

O(n)

What n represents in O(n) Notation? 

It presents the input size - So the amount of operations 
increase linearly with the input size 

Why the effiency of an algorithm can't be measure by how long it takes to run?

The runtime velocity measure in milliseconds can be really different depending on the computer CPU and also internet connectivity,
and that's why we don't measure code runtime efficiency based on milliseconds but instead, on the number of operations that the algorithm
will need to execute according to a certain input size
"""