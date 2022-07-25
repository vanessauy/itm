#!/usr/bin/env python
# coding: utf-8

# In[3]:


def shift_letter(letter, shift):
    '''Shift Letter. 
    5 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    if letter == " ":
        return letter
    else:
        #Determine the number of letters from 'A' to 'Z'
        letter_count = ord('Z') - ord('A') + 1
        #Get the effective distance of the resulting character (after shift) from A
        #The % operator takes into consideration the wrapping
        eff_distance_from_A = (ord(letter) + shift - ord('A')) % letter_count
        #Get the corresponding character code
        char_code = ord('A') + eff_distance_from_A
        #Convert back to the actual character
        return chr(char_code)


# In[7]:


def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    10 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    hidden_message = ''
    
    for char in message:
        if char == " ":
            hidden_message += char
        else:
            
            #Determine the number of letters from 'A' to 'Z'
            letter_count = ord('Z') - ord('A') + 1
            #Get the effective distance of the resulting character (after shift) from A
            #The % operator takes into consideration the wrapping
            eff_distance_from_A = (ord(char) + shift - ord('A')) % letter_count
            #Get the corresponding character code
            char_code = ord('A') + eff_distance_from_A
            
            #Convert to the actual character and append
            hidden_message += chr(char_code)
        
    return hidden_message


# In[10]:


def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    10 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    if letter == " ":
        return letter
    else:
        shift = ord(letter_shift) - ord('A') #Convert the 'letter_shift' variable to the actual number of shift
            
        #Determine the number of letters from 'A' to 'Z'
        letter_count = ord('Z') - ord('A') + 1
        #Get the effective distance of the resulting character (after shift) from A
        #The % operator takes into consideration the wrapping
        eff_distance_from_A = (ord(letter) + shift - ord('A')) % letter_count
        #Get the corresponding character code
        char_code = ord('A') + eff_distance_from_A
        #Convert back to the actual character
        return chr(char_code)


# In[14]:


def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    15 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    #extend the key (if applicable)
   
    #Determine the number of times the key will be repeated
    key_frequency = len(message) // len(key)
    
    #Determine nunber of extra characters needed to match the length of 'message'
    length_of_extra_characters = len(message) % len(key)
   
    #Extend the key
    extended_key = key * key_frequency + key[:length_of_extra_characters]
    
    hidden_message = ''
    
    #For every character in the message, shift by corresponding character in the extended key
    for i in range(len(message)):
        if message[i] == " ":
            hidden_message += message[i]
        else:
            shift = ord(extended_key[i]) - ord('A') #convert letter to actual shift
                        
            #Determine the number of letters from 'A' to 'Z'
            letter_count = ord('Z') - ord('A') + 1
            #Get the effective distance of the resulting character (after shift) from A
            #The % operator takes into consideration the wrapping
            eff_distance_from_A = (ord(message[i]) + shift - ord('A')) % letter_count
            #Get the corresponding character code
            char_code = ord('A') + eff_distance_from_A
            #Convert back to the actual character
            
            hidden_message += chr(char_code)

    return hidden_message


# In[16]:


def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.
    
    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of 
        parchment that contained a string of apparent gibberish. The parchment, 
        when read using the scytale, would reveal a message due to every nth 
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number. 
        For this example, we will use "INFORMATION_AGE" as 
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of 
        the shift. If it is not, add additional underscores 
        to the end of the message until it is. 
        In this example, "INFORMATION_AGE" is already a multiple of 3, 
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message. 
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message. 
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case, 
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    # Check if shift value is a multiple of the length of the message
    # Otherwise, add underscores until it is already a multiple
    
    remainder = len(message) % shift
    multiplier = shift - remainder
    
    #Add additional underscores to make it a multiple
    extended_message = message if remainder == 0 else message + (multiplier * '_')
   
    hidden_message = ''    
    
    #For each index, apply the formula in item 3

    for i in range(len(extended_message)):
        char = extended_message[(i // shift) + (len(extended_message) // shift) * (i % shift)]
        hidden_message += char
        
    return hidden_message 


# In[23]:


def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.
    
    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message
        
    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    n = len(message)
    orig_message = ['*'] * n
    
    for i in range(n):
        orig_message[(i // shift) + (n // shift) * (i % shift)] = message[i]
    
    return ''.join(orig_message)

