"""
By: Khor Jun Yong
StudentID: 32429975
Email: jkho0038@student.monash.edu
"""

def counting_sort_score(lst):  
    """
    This function sort the list of matches according to their score 
    Reference: The ideas of implementing counting sort is refered from the recording
            "FIT2004 2022sem02 Lecture02 p4 Sorting CountingSort" by Dr Ian. 

    Input   
             lst  : A list of matches.
    Output: 
             lst  : The list of matches is sorted in descending order acccording to score.
    Time complexity:
           Worst  : O(N+H), where N is the length of list and H is the highes score
    Space Complexity:
        Auxiliary : O(H), where H is the maximum score from the list
    
    """

    # Find the largest score to create an counting array, O(N) where N represent the length of list
    highest_score = lst[0][2]
    for i in range(len(lst)):
        if lst[i][2] > highest_score:
            highest_score = lst[i][2]

    # intitialise count array
    count_array = [None]* (highest_score +1)
    for i in range(len(count_array)):
        count_array[i] = []
 
    # Store the items from input list into count_array          
    for item in lst:
        position = item[2]                                     
        count_array[position].append(item)

    #update input array according to score in descending order
    index=0
    for j in range(len(count_array)-1, -1 ,-1):
        if count_array[j] != []:
            item = count_array[j]
            frequency = len(count_array[j])

            for k in range(frequency):
                lst[index] = item[k]
                index +=1
    
    return lst

def counting_sort_char(team, roster):
    """
    This function is used to sort the characters in a team  

    Input: 
        team  : A team in string
        roster: Integer that represent a character set
    Output:
        lst   : The alphabets of team is sorted in ascending order. 
    Time Complexity:
        Worst: O(N), where N is the length of team
    Space Complexity:
        Aux: O(1), assuming roster is a constant
    """
    # initialise count array
    char_countArray = [0]*roster

    # update count array
    for char in team:
        position = ord(char)-65   # A starts from index 0
        char_countArray[position] += 1
    
    # update input string
    index =0
    res = "" # Create a new string to store the sorted team as string is immutable.
    for i in range(len(char_countArray)):
        frequency = char_countArray[i]
        character = chr(i+65)

        for j in range(frequency):
            res += character
     
    return res

def counting_sort_teams(lst, roaster, target, _col, begin, end): 
    """
    This function is used in radix sort to sort the team according to the column(from right to left)

    Input:
        lst   : The list of matches
        roster: Integer that represent a character set
        target: An integer that represent team1 or team2 in the list of match
        _col  : Indicate the position to be sorted from rightmost to leftmost character
        begin : The start position where the scores is same between match
        end   : The end position where the scores becomes different.
    Output:
        lst   : The team is sorted according to _col
    Time Complexity:
        Worst: O(N), where N is the length of list 
    Space Complexity:
        Aux: O(N), where N is the length of list
    """

    size = len(lst[0][0])

    #initialise count array
    count_array = [None]* roaster   

    for i in range(len(count_array)):
        count_array[i] = []

    # Store the items from input list into count_array      
    for i in range(begin, end):
        item = lst[i]
        team = lst[i][target]
        position = (ord(team[size-1-_col])) - 65
        count_array[position].append(item) 

    # Update the list
    index= begin
    for j in range(len(count_array)):   # Its complexity is O(n) as the number of items in count_array the same
        if count_array[j] != []:        #   as the number of items in input list    
            item = count_array[j]
            frequency = len(count_array[j])
            for k in range(frequency):
                lst[index] = item[k]
                index +=1
    return lst

def find_range(lst, seach_team2: bool):
    """
    This function find the range of the list with the same score
    
    Input: 
        lst         : A sorted list arranged in descending order of score
        seach_team2 : A boolean that indicate to search in either team2 or team1
    Output:
        _ranges     : A list of list that indicate the range of the matches  
                      with the same score
    Time Complexity:
        Worst: O(N), where N is the length of list
    Space Complexity:
        Aux: O(S), where S represent the number of ranges of matches with same score  
    """

    _ranges = []
    counter1 = 0
    
    if seach_team2 == False:  
        # Complexity of O(N), where N is the length of list
        while counter1 < len(lst)-1:    
            # Once matches with same score is found, counter1 will representnthe start position 
            if lst[counter1][2] == lst[counter1 +1][2]:
                for counter2 in range(counter1+1, len(lst)):
                    if lst[counter2][2] != lst[counter1][2]:  
                        _ranges.append([counter1,counter2]) # counter2 represent the end position where the score are different
                        break

                    # To capture cases where the score at the last element is equal to its previous one
                    if counter2==len(lst)-1 and lst[counter2][2] == lst[counter1][2]:
                        counter2+=1
                        _ranges.append([counter1,counter2]) 
                counter1 = counter2 
            else:
                counter1+=1
    
    elif seach_team2 == True:   # Check both team1 and the score
        while counter1 < len(lst)-1:
            # team1 condition and score is checked at this loop
            if lst[counter1][2] == lst[counter1 +1][2] and lst[counter1][0] == lst[counter1 +1][0]:
                for counter2 in range(counter1+1, len(lst)):
                    if lst[counter2][2] != lst[counter1][2]:  
                        _ranges.append([counter1,counter2]) # counter2 is the position where the score are different
                        break

                    # To capture cases where the score is equal at the last element
                    if counter2==len(lst)-1 and lst[counter2][2] == lst[counter1][2]:
                        counter2+=1
                        _ranges.append([counter1,counter2])
                counter1 = counter2 
            else:
                counter1+=1
    return _ranges  

def radix_sort(lst,roster):
    """
    This function sort the teams in matches of the same score in ascending order.
    
    Input: 
        lst    : A sorted list arranged in descending order of score
        roster : Integer that represent a character set 
    Output:
        lst    : A list that teams in mataches of the same score is sorted in ascending order

    Time Complexity:
        Worst: O(NM), where N is the length of list, and M is the length of character in teams
    Space Complexity:
        Aux: O(N + S), where N is the length of list and S represent the number of ranges of matches with same score 
    """
    #Sort the lst in descending order from rightest to leftest character.
   
    # ranges
    _ranges = find_range(lst, False)

    # Sort for team1
    for i in _ranges:
        begin = i[0]
        end = i[1]
        for col in range(len(lst[0][0])):
            lst = counting_sort_teams(lst, roster, 0, col, begin, end)

    # Now for team 2
    _ranges = find_range(lst, True)

    # Sort for team2
    for i in _ranges:
        begin = i[0]
        end = i[1]
        for col in range(len(lst[0][0])):
            lst = counting_sort_teams(lst, roster, 1, col, begin, end)
    return lst

def matches_binary_search(lst, key):
    """
    This function search for matches with the score that matched the key

    Input: 
        lst    : A sorted list arranged in descending order of score
        key    : An Integer that represent the target to be searched 
    Output:
        searchedmatches: A list of matches with score that is equal to the key
    Time Complexity:
        Average : O(log N), where N is the length of the list
        Worst   : O(N), if all matches has a score equal to the key
    Space Complexity:
        Aux: O(S), where S represent the number of matches with score same as key
    """
    searchedmatches = []

    low = len(lst)
    high = 0

    while high < low-1: # O(log N), where N is the length of list
        mid = (low+high)//2
        if key > lst[mid][2]:
            low = mid
        elif key < lst[mid][2]:
            high = mid
        else:
            searchedmatches.append(lst[mid])
            break

    if lst[mid][2] == key:  # O(N) if all the matches in list has the same score as key
        # check if there exist same score on right side
        for i in range(mid+1, len(lst)):
            if lst[i][2] != key:
                break
            else:
                searchedmatches.append(lst[i])
        # check if there exist same score on left side 
        for j in range(mid-1, -1,-1):
            if lst[j][2] != key:
                break
            else:
                searchedmatches.append(lst[j])

    # If no match is found, find a match with higher score from the middle to the left 
    else:   
        for k in range(mid,-1,-1):  # O(log N) as it search from the mid provided by binary search above
            if lst[k][2] > key:
                searchedmatches.append(lst[high])
                break
    return searchedmatches

def analyze(results, roster, score):
    """
    This functions analyse the result by returning the top 10 matches and matches that
    has the same score as score

    Input: 
        results: A list of list
        roster : Integer that represent a character set 
        score  : A target score to be find in the matches.
    Output:
        res    : Return a nested list of top 10 matches, and a nested list of searchedmatches
                 with the same score as score 
    Time Complexity:
        Worst   : O(NM), where N is the length of list, and M is the length of character in teams
    Space Complexity:
        Aux: O(N +S + H), where N is the length of list, S represent the number of matches with score same as key
                        and H representing the highest score in the matches
    """
    res = []
    size = len(results)
    for i in range(size):
        opposite_team = [results[i][1],results[i][0],(100-results[i][2])]
        results.append(opposite_team)

    results = counting_sort_score(results)

    #Sort characters in team1 
    for j in range(len(results)):
        results[j][0] = counting_sort_char(results[j][0], roster)

    #Sort characters for team 2
    for j in range(len(results)):
        results[j][1] = counting_sort_char(results[j][1], roster)

    # Remove duplicate 
    sorted_list = []
    for j in range(len(results)-1):
        if results[j][2] == results[j+1][2]: #check the score before comparing the whole list
        
            if results[j] != results[j+1]:
                sorted_list.append(results[j])

        # Capture the last element in the lst        
        elif j+1 == len(results)-1:
            sorted_list.append(results[j+1])

        else:
            sorted_list.append(results[j])

    sorted_list = radix_sort(sorted_list, roster)

    if len(sorted_list) < 10:
        top_10_match = sorted_list
    else:
        top_10_match = sorted_list[:10]
    res.append(top_10_match)

    # Find team with similar score as score
    matchedscore = matches_binary_search(sorted_list, score)
    res.append(matchedscore)

    print(res)
    return res

"""
Driver 
"""
if __name__ == "__main__":
    # a roster of 2 characters
    roster = 2
    # results with 20 matches
    results = [
        ['AAB', 'AAB', 35], ['AAB', 'BBA', 49], ['BAB', 'BAB', 42],
        ['AAA', 'AAA', 38], ['BAB', 'BAB', 36], ['BAB', 'BAB', 36],
        ['ABA', 'BBA', 57], ['BBB', 'BBA', 32], ['BBA', 'BBB', 49],
        ['BBA', 'ABB', 55], ['AAB', 'AAA', 58], ['ABA', 'AAA', 46],
        ['ABA', 'ABB', 44], ['BBB', 'BAB', 32], ['AAA', 'AAB', 36],
        ['ABA', 'BBB', 48], ['BBB', 'ABA', 33], ['AAB', 'BBA', 30],
        ['ABB', 'BBB', 68], ['BAB', 'BBB', 52]
        ]
    # looking for a score of 64
    score = 64
    # running the function
    analyze(results, roster, score)
