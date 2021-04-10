companiesList = ['twitter', 'spotify', 'tiktok', 'tinder', 'google']
companiesLargeList = ['facebook'] * 100000
companiesLargeList.append('twitter')

def findTwitter(companies): 
    for company in companies:
        if company != 'twitter': continue 

        print('Found twitter')
        break # Breaking the loop doesn't matter for the worst case scenario because it's already the last loop

findTwitter(companiesLargeList)

"""
Big O Notation of findTwitter: O(n) - Linear time 

=== What's the Bio O Notation for Linear time? === 

O(n)

=== What n represents in O(n) Notation? ===  

It presents the input size - So the amount of operations 
increase linearly with the input size 

=== Why the efficacy of an algorithm can't be measure by how long it takes to run? === 

The runtime velocity measure in milliseconds can be really different depending on the computer CPU and also internet connectivity,
and that's why we don't measure code runtime efficiency based on milliseconds but instead, on the number of operations that the algorithm
will need to execute according to a certain input size
"""