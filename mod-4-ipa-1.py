#!/usr/bin/env python
# coding: utf-8

# In[1]:


'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #Check the people followed by from_member
    from_member_following = social_graph[from_member]['following']
    
    #Check the people followed by toMember
    to_member_following = social_graph[to_member]['following']

    #Check if the user is in the list of the 'following' of the other user (and vice versa)
    fromMember_follows_toMember = to_member in from_member_following
    toMember_follows_fromMember = from_member in to_member_following
    
    result = ''
    
    if fromMember_follows_toMember and toMember_follows_fromMember:
        result = 'friends'
    elif fromMember_follows_toMember and not toMember_follows_fromMember:
        result = 'follower'
    elif not fromMember_follows_toMember and toMember_follows_fromMember:
        result = 'followed by'
    else:
        result = 'no relationship'
    
    return result


# In[2]:


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    25 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #Board was assumed to have two unique symbols at one time. Symbols other than 'X' and 'O' is allowed.
    #Check every row in the board
    for row in board: 
        #Check if all the symbols in the row are the same
        is_same = all([row[0] ==symbol and symbol != '' for symbol in row])
        if is_same:
            return row [0] 
    
    #Check every column in the board
    for column in zip(*board):
        #Check if all the symbols in the column are the same
        is_same = all([column[0] ==symbol and symbol != '' for symbol in column])
        if is_same:
            return column [0]
    
    #n x n board
    n = len(board)
    
    #Check the up-down main diagonal
    up_down_symbols = [board[i][i] for i in range(n)]
    up_down_same = all([up_down_symbols[0] ==symbol and symbol != '' for symbol in up_down_symbols])
    if up_down_same:
        return up_down_symbols[0]
    
    #Check the down-up main diagonal
    down_up_symbols = [board[n - 1 - i][i] for i in range(n)]
    down_up_same = all([down_up_symbols[0] ==symbol and symbol != '' for symbol in down_up_symbols])
    if down_up_same:
        return down_up_symbols[0]

    #If no uniform symbols can be found across rows, columns, main diagonals, simply return 'NO WINNER'
    return 'NO WINNER'


# In[3]:


def eta(first_stop, second_stop, route_map):
    '''ETA. 
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    try:
        #Create a key for the dictionary
        tuple_key = (first_stop, second_stop)

        #Get the value in the dictionary to determine the travel
        travel_time = legs[tuple_key]['travel_time_mins']
    except:
        print('One of the inputs is invalid.')
        return None
    
    return travel_time

