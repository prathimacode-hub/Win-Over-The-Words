from dictionary import load_words

DICTIONARY = load_words()

ALPHABET = [
    'A',
    'B',
    'C',
    'D',
    'E',
    'F',
    'G',
    'H',
    'I',
    'J',
    'K',
    'L',
    'M',
    'N',
    'O',
    'P',
    'Q',
    'R',
    'S',
    'T',
    'U',
    'V',
    'W',
    'X',
    'Y',
    'Z'
]

LETTER_VALUES = {
    'A': 1,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 4,
    'G': 3,
    'H': 3,
    'I': 1,
    'J': 10,
    'K': 5,
    'L': 2,
    'M': 4,
    'N': 2,
    'O': 1,
    'P': 4,
    'Q': 10,
    'R': 1,
    'S': 1,
    'T': 1,
    'U': 2,
    'V': 5,
    'W': 4,
    'X': 8,
    'Y': 3,
    'Z': 10,
    '?': 0
}

GAME_BOARD_BONUSES = [
    ['  ', '  ', '  ', 'TW', '  ', '  ', 'TL', '  ', 'TL', '  ', '  ', 'TW', '  ', '  ', '  '],
    ['  ', '  ', 'DL', '  ', '  ', 'DW', '  ', '  ', '  ', 'DW', '  ', '  ', 'DL', '  ', '  '],
    ['  ', 'DL', '  ', '  ', 'DL', '  ', '  ', '  ', '  ', '  ', 'DL', '  ', '  ', 'DL', '  '],
    ['TW', '  ', '  ', 'TL', '  ', '  ', '  ', 'DW', '  ', '  ', '  ', 'TL', '  ', '  ', 'TW'],
    ['  ', '  ', 'DL', '  ', '  ', '  ', 'DL', '  ', 'DL', '  ', '  ', '  ', 'DL', '  ', '  '],
    ['  ', 'DW', '  ', '  ', '  ', 'TL', '  ', '  ', '  ', 'TL', '  ', '  ', '  ', 'DW', '  '],
    ['TL', '  ', '  ', '  ', 'DL', '  ', '  ', '  ', '  ', '  ', 'DL', '  ', '  ', '  ', 'TL'],
    ['  ', '  ', '  ', 'DW', '  ', '  ', '  ', '  ', '  ', '  ', '  ', 'DW', '  ', '  ', '  '],
    ['TL', '  ', '  ', '  ', 'DL', '  ', '  ', '  ', '  ', '  ', 'DL', '  ', '  ', '  ', 'TL'],
    ['  ', 'DW', '  ', '  ', '  ', 'TL', '  ', '  ', '  ', 'TL', '  ', '  ', '  ', 'DW', '  '],
    ['  ', '  ', 'DL', '  ', '  ', '  ', 'DL', '  ', 'DL', '  ', '  ', '  ', 'DL', '  ', '  '],
    ['TW', '  ', '  ', 'TL', '  ', '  ', '  ', 'DW', '  ', '  ', '  ', 'TL', '  ', '  ', 'TW'],
    ['  ', 'DL', '  ', '  ', 'DL', '  ', '  ', '  ', '  ', '  ', 'DL', '  ', '  ', 'DL', '  '],
    ['  ', '  ', 'DL', '  ', '  ', 'DW', '  ', '  ', '  ', 'DW', '  ', '  ', 'DL', '  ', '  '],
    ['  ', '  ', '  ', 'TW', '  ', '  ', 'TL', '  ', 'TL', '  ', '  ', 'TW', '  ', '  ', '  '],
]

def compute_across_cross_checks(game_board):
    '''
    Given the game board, this function determines which letters can fit in each
    cell of a row and form a valid down word. This returns the letter matrix for
    each row as to which characters are valid for each cell.

    Parameter {Array<Array<str>>} game_board the game board letter matrix.
    Returns {Array<Array<str>>} the cross check letter matrix.
    '''

    cross_checks = []

    # Iterate over the rows.
    for row in range(15):
        row_cross_checks = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

        for i in range(15): # Iterate over the columns.
            # The cell isn't empty.
            if game_board[row][i] != ' ':
                row_cross_checks[i].append(game_board[row][i])
                continue

            # Find the words above and below (if applicable).
            word_above = ''
            word_below = ''

            j = row - 1
            while j != -1 and game_board[j][i] != ' ':
                word_above = game_board[j][i] + word_above
                j -= 1

            j = row + 1
            while j != 15 and game_board[j][i] != ' ':
                word_below =  word_below + game_board[j][i]
                j += 1

            # Find which (if any) letters in the alphabet form a valid cross word.
            for letter in range(26):
                # Word above and below.
                if word_above and word_below:
                    if (word_above + ALPHABET[letter] + word_below).lower() in DICTIONARY:
                        row_cross_checks[i].append(ALPHABET[letter])
                # Only word above.
                elif word_above:
                    if (word_above + ALPHABET[letter]).lower() in DICTIONARY:
                        row_cross_checks[i].append(ALPHABET[letter])
                # Only word below.
                elif word_below:
                    if (ALPHABET[letter] + word_below).lower() in DICTIONARY:
                        row_cross_checks[i].append(ALPHABET[letter])
                # No word above or below.
                else:
                    row_cross_checks[i].append(ALPHABET[letter])
        
        cross_checks.append(row_cross_checks)
    
    return cross_checks


def compute_down_cross_checks(game_board):
    '''
    Given the game board, this function determines which letters can fit in each
    cell of a column and form a valid across word. This returns the letter matrix for
    each column as to which characters are valid for each cell.

    Parameter {Array<Array<str>>} game_board the game board letter matrix.
    Returns {Array<Array<str>>} the cross check letter matrix.
    '''

    cross_checks = []

    # Iterate over the columns.
    for column in range(15):
        column_cross_checks = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

        for i in range(15): # Iterate over the rows.
            # The cell isn't empty.
            if game_board[i][column] != ' ':
                column_cross_checks[i].append(game_board[i][column])
                continue

            # Find the words left and right (if applicable).
            word_left = ''
            word_right = ''

            j = column - 1
            while j != -1 and game_board[i][j] != ' ':
                word_left = game_board[i][j] + word_left
                j -= 1

            j = column + 1
            while j != 15 and game_board[i][j] != ' ':
                word_right =  word_right + game_board[i][j]
                j += 1

            # Find which (if any) letters in the alphabet form a valid cross word.
            for letter in range(26):
                # Word left and right.
                if word_left and word_right:
                    if (word_left + ALPHABET[letter] + word_right).lower() in DICTIONARY:
                        column_cross_checks[i].append(ALPHABET[letter])
                # Only word left.
                elif word_left:
                    if (word_left + ALPHABET[letter]).lower() in DICTIONARY:
                        column_cross_checks[i].append(ALPHABET[letter])
                # Only word right.
                elif word_right:
                    if (ALPHABET[letter] + word_right).lower() in DICTIONARY:
                        column_cross_checks[i].append(ALPHABET[letter])
                # No word left or right.
                else:
                    column_cross_checks[i].append(ALPHABET[letter])
        
        cross_checks.append(column_cross_checks)
    
    return cross_checks

def compute_anchors(game_board):
    '''
    An anchor is defined an empty cell with an adjacent (horizontal or vertical)
    non-empty cell. This returns the binary matrix, where a zero is a non-anchor
    and a one is an anchor. If there are no anchors, indicating an empty game board,
    index [7, 7] is set as the only anchor.

    Parameter {Array<Array<str>>} game_board the game board letter matrix.
    Returns {Array<Array<int>>} the anchor matrix.
    '''

    no_anchors = True
    anchors = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

    for i in range(15):
        for j in range(15):
            if game_board[i][j] == ' ':                     # Empty cell.
                if j != 0 and game_board[i][j - 1] != ' ':  # Letter to the left.
                    no_anchors = False
                    anchors[i].append(1)
                    continue
                if j != 14 and game_board[i][j + 1] != ' ': # Letter to the right.
                    no_anchors = False
                    anchors[i].append(1)
                    continue
                if i != 0 and game_board[i - 1][j] != ' ':  # Letter above.
                    no_anchors = False
                    anchors[i].append(1)
                    continue
                if i != 14 and game_board[i + 1][j] != ' ': # Letter below.
                    no_anchors = False
                    anchors[i].append(1)
                    continue
            anchors[i].append(0)

    if no_anchors:
        anchors[7][7] = 1

    return anchors

def populate_game_board(letters):
    '''
    Given an letters with their corresponding indices, create the 15x15
    WWF game board.

    Parameter {Array<dict>} letters the game letters with letter and index
    key-value pairs.
    Returns {Array<Array<str>>} the 2d populated gameboard.
    '''

    game_board = []

    # Create an empty 15x15 game board.
    for i in range(15):
        row = []

        for i in range(15):
            row += ' '
        
        game_board += [row]

    # Populate the letters given into the game board.
    for letter in letters:
        i = int(letter['index'] / 15)
        j = letter['index'] % 15
        letter = letter['letter']

        game_board[i][j] = letter

    return game_board

def intersection(lst1, lst2):
    '''
    Given two lists, return the values that are in both lists, i.e. the intersection.

    Parameter {Array<any>} lst1 the first list.
    Parameter {Array<any>} lst2 the second list.
    Returns {Array}
    '''

    return [value for value in lst1 if value in lst2]

def compute(json_data):
    '''
    Given game board letters, and the user's letter rack, compute the best
    possible move.

    Parameter {dict} json_data request data with the game board letters and the
    user's letter rack.
    Returns {dict} data containing the best possible move information.
    '''

    # Populate the user's letter rack and the game board.
    RACK = json_data['userLetters']
    GAME_BOARD = populate_game_board(json_data['gameLetters'])

    # Compute the anchors and cross checks.
    anchors = compute_anchors(GAME_BOARD)
    across_cross_checks = compute_across_cross_checks(GAME_BOARD)
    down_cross_checks = compute_down_cross_checks(GAME_BOARD)

    # Compute the highest scoring across word.
    best_across_word = {
        'last_letter_index': [-1, -1],
        'word': '',
        'score': 0,
        'direction': 'across'
    }

    def filter_rack(rack, letter):
        '''
        Removes a letter from the rack and returns it.

        Parameter {Array<str>} rack the rack of letters to filter.
        Returns {Arrary<str>} the filtered rack.
        '''

        letter_removed = False
        new_rack = []

        for current_letter in rack:
            # Same letter, hasn't been removed.
            if current_letter == letter and not letter_removed:
                letter_removed = True
            # Different letter or letter already removed, add it to the new rack.
            else:
                new_rack += current_letter

        return new_rack

    def score_word_across(word, last_index, rack_letter_indices):
        '''
        Given a word played across, compute it's score.

        Parameter {str} word the word to compute the score of.
        Parameter {list<int>} last_index the coordinates of the last letter
        of the word on the board.
        Parameter {list<int>} rack_letter_indices the indices of letters
        played from the rack.
        Returns {int} the score of the word.
        '''

        # Extract the last letter index.
        i, j = last_index

        # Keep up with the number of double and triple word cells played.
        dw = 0
        tw = 0

        # Compute the across word point value.
        across_word_score = 0
        for letter in word:
            across_word_score += LETTER_VALUES[letter]

        # Compute cross word point values.
        cross_words_scores = []
        for letter in word:
            cross_words_scores.append(0)

        for k in range(len(word)):
            if [i, j - k] in rack_letter_indices:
                if i != 0 and GAME_BOARD[i - 1][j - k] != ' ':
                    l = i - 1
                    while l > -1 and GAME_BOARD[l][j - k] != ' ':
                        cross_words_scores[k] += LETTER_VALUES[GAME_BOARD[l][j - k]]
                        l -= 1
                if i != 14 and GAME_BOARD[i + 1][j - k] != ' ':
                    l = i + 1
                    while l < 15 and GAME_BOARD[l][j - k] != ' ':
                        cross_words_scores[k] += LETTER_VALUES[GAME_BOARD[l][j - k]]
                        l += 1
                
                if (
                    i != 0 and GAME_BOARD[i - 1][j - k] != ' ' or
                    i != 14 and GAME_BOARD[i + 1][j - k] != ' '
                ):
                    cross_words_scores[k] += LETTER_VALUES[word[len(word) - k - 1]]

                # Compute bonus scores.
                # Double Letter.
                if GAME_BOARD_BONUSES[i][j - k] == 'DL':
                    across_word_score += LETTER_VALUES[word[len(word) - k - 1]]

                    if (
                        i != 0 and GAME_BOARD[i - 1][j - k] != ' ' or
                        i != 14 and GAME_BOARD[i + 1][j - k] != ' '
                    ):
                        cross_words_scores[k] += LETTER_VALUES[word[len(word) - k - 1]]
                # Triple Letter.
                elif GAME_BOARD_BONUSES[i][j - k] == 'TL':
                    across_word_score += LETTER_VALUES[word[len(word) - k - 1]] * 2

                    if (
                        i != 0 and GAME_BOARD[i - 1][j - k] != ' ' or
                        i != 14 and GAME_BOARD[i + 1][j - k] != ' '
                    ):
                        cross_words_scores[k] += LETTER_VALUES[word[len(word) - k - 1]] * 2
                # Double Word.
                elif GAME_BOARD_BONUSES[i][j - k] == 'DW':
                    dw += 1

                    cross_words_scores[k] *= 2
                # Triple Word.
                elif GAME_BOARD_BONUSES[i][j - k] == 'TW':
                    tw += 1

                    cross_words_scores[k] *= 3

        # Factor in double and triple words for the across word.
        for k in range(dw):
            across_word_score *= 2

        for k in range(tw):
            across_word_score *= 3

        # If the full rack is played, add 35 to the across word score.
        if len(rack_letter_indices) == 7:
            across_word_score += 35

        # Add cross word values to the across word value, and return it.
        for score in cross_words_scores:
            across_word_score += score

        return across_word_score

    def extend_right(index, rack, current_word, rack_played_incides):
        '''
        Given an anchor position, recursively compute possible across word plays by
        extending right on the board. For each word, compute its point value, and update
        the best_across_word score accordingly.

        Parameter {Array<int>} index the i, j index of the current position on the board.
        Parameter {Array<str>} rack the user's letter rack.
        Parameter {str} current_word the current permutation of the word.
        Parameter {Array<Array<int>>} rack_played_incides a list of the indices of letters played
        from the rack while extending right. 
        '''

        # Extract the gameboard coordinates.
        i, j = index

        # Base Case - no common letters or out of the gameboard bounds.
        if j > 14 or (GAME_BOARD[i][j] == ' ' and not intersection(rack, across_cross_checks[i][j])):
            return

        # For the current coordinate, find common letters between the rack and cross checks.
        common_letters = intersection(rack, across_cross_checks[i][j])

        # Case 1: empty cell.
        if GAME_BOARD[i][j] == ' ':
            for letter in common_letters:
                # Score the current word, if it's in the dictionary.
                if (current_word + letter).lower() in DICTIONARY:
                    if (j + 1 < 15 and GAME_BOARD[i][j + 1] == ' ') or j == 14:
                        word = current_word + letter
                        score = score_word_across(word, [i, j], rack_played_incides + [[i, j]])

                        # Update the best across word, if the score of the current word is better.
                        if score > best_across_word['score']:
                            best_across_word['last_letter_index'] = [i, j]
                            best_across_word['word'] = word
                            best_across_word['score'] = score
                
                # Keep extending right to form words.
                extend_right(
                    [i, j + 1],
                    filter_rack(rack, letter),
                    current_word + letter,
                    rack_played_incides + [[i, j]]
                )

        # Case 2: occupied cell.
        else:
            # Score the current word, if it's in the dictionary.
            if (current_word + GAME_BOARD[i][j]).lower() in DICTIONARY:
                if (j + 1 < 15 and GAME_BOARD[i][j + 1] == ' ') or j == 14:
                    word = current_word + GAME_BOARD[i][j]
                    score = score_word_across(word, [i, j], rack_played_incides)

                    # Update the best across word, if the score of the current word is better.
                    if score > best_across_word['score']:
                        best_across_word['last_letter_index'] = [i, j]
                        best_across_word['word'] = word
                        best_across_word['score'] = score

            # Keep extending right to form words.
            extend_right(
                [i, j + 1],
                rack,
                current_word + GAME_BOARD[i][j],
                rack_played_incides
            )

    def extend_right_with_left_part(index, rack, left_part):
        '''
        Given a position to the left of an anchor, recursively compute possible across word
        plays by extending left before extending right on the board. For each word, compute 
        its point value, and update he best_across_word score accordingly.

        Parameter {Array<int>} index the i, j index of the current position on the board.
        Parameter {Array<str>} rack the user's letter rack.
        Parameter {str} left_part the current left_part of the word.
        '''

        # Extract the gameboard coordinates.
        i, j = index

        # Base Case - no common letters or out of the gameboard bounds.
        if j < 0 or not intersection(rack, across_cross_checks[i][j]):
            return

        # For the current coordinate, find common letters between the rack and cross checks.
        common_letters = intersection(rack, across_cross_checks[i][j])

        # Case 1: the cell to the left of the current index is empty, or j = 0.
        if j == 0 or GAME_BOARD[i][j - 1] == ' ':
            for letter in common_letters:
                word = letter + left_part
                rack_played_incides = []

                for k in range(len(word)):
                    rack_played_incides += [[i, j + k]]

                # Extend right to form words.
                extend_right(
                    [i, j + len(word)],
                    filter_rack(rack, letter),
                    word,
                    rack_played_incides
                )

                # Keep extending left.
                extend_right_with_left_part(
                    [i, j - 1],
                    filter_rack(rack, letter),
                    word
                )
        # Case 2: the cell to the left of the current index is occupied.
        else:
            pass

    for i in range(15):
        for j in range(15):
            if anchors[i][j]:
                # Case 1: cell to the left of the anchor is empty.
                if j != 0 and GAME_BOARD[i][j - 1] == ' ':
                    extend_right(
                        [i, j],
                        RACK,
                        '',
                        []
                    )

                    extend_right_with_left_part(
                        [i, j - 1],
                        RACK,
                        ''
                    )
                # Case 2: cell to the left of the anchor is occupied.
                else:
                    # Grab the word to the left of the anchor, if there is one.
                    word = ''
                    k = j - 1
                    while k != -1 and GAME_BOARD[i][k] != ' ':
                        word = GAME_BOARD[i][k] + word
                        k -= 1
                    
                    # Compute possible words extending right of the anchor.
                    extend_right(
                        [i, j],
                        RACK,
                        word,
                        []
                    )

    # Compute the highest scoring down word.
    best_down_word = {
        'last_letter_index': [-1, -1],
        'word': '',
        'score': 0,
        'direction': 'down'
    }

    def score_word_down(word, last_index, rack_letter_indices):
        '''
        Given a word played down, compute it's score.

        Parameter {str} word the word to compute the score of.
        Parameter {list<int>} last_index the coordinates of the last letter
        of the word on the board.
        Parameter {list<int>} rack_letter_indices the indices of letters
        played from the rack.
        Returns {int} the score of the word.
        '''

        # Extract the last letter index.
        i, j = last_index

        # Keep up with the number of double and triple word cells played.
        dw = 0
        tw = 0

        # Compute the down word point value.
        down_word_score = 0
        for letter in word:
            down_word_score += LETTER_VALUES[letter]

        # Compute cross word point values.
        cross_words_scores = []
        for letter in word:
            cross_words_scores.append(0)

        for k in range(len(word)):
            if [i - k, j] in rack_letter_indices:
                if j != 0 and GAME_BOARD[i - k][j - 1] != ' ':
                    l = j - 1
                    while l > -1 and GAME_BOARD[i - k][l] != ' ':
                        cross_words_scores[k] += LETTER_VALUES[GAME_BOARD[i - k][l]]
                        l -= 1
                if j != 14 and GAME_BOARD[i - k][j + 1] != ' ':
                    l = j + 1
                    while l < 15 and GAME_BOARD[i - k][l] != ' ':
                        cross_words_scores[k] += LETTER_VALUES[GAME_BOARD[i - k][l]]
                        l += 1
                
                if (
                    j != 0 and GAME_BOARD[i - k][j - 1] != ' ' or
                    j != 14 and GAME_BOARD[i - k][j + 1] != ' '
                ):
                    cross_words_scores[k] += LETTER_VALUES[word[len(word) - k - 1]]

                # Compute bonus scores.
                # Double Letter.
                if GAME_BOARD_BONUSES[i - k][j] == 'DL':
                    down_word_score += LETTER_VALUES[word[len(word) - k - 1]]

                    if (
                        j != 0 and GAME_BOARD[i - k][j - 1] != ' ' or
                        j != 14 and GAME_BOARD[i - k][j + 1] != ' '
                    ):
                        cross_words_scores[k] += LETTER_VALUES[word[len(word) - k - 1]]
                # Triple Letter.
                elif GAME_BOARD_BONUSES[i - k][j] == 'TL':
                    down_word_score += LETTER_VALUES[word[len(word) - k - 1]] * 2

                    if (
                        j != 0 and GAME_BOARD[i - k][j - 1] != ' ' or
                        j != 14 and GAME_BOARD[i - k][j + 1] != ' '
                    ):
                        cross_words_scores[k] += LETTER_VALUES[word[len(word) - k - 1]] * 2
                # Double Word.
                elif GAME_BOARD_BONUSES[i - k][j] == 'DW':
                    dw += 1

                    cross_words_scores[k] *= 2
                # Triple Word.
                elif GAME_BOARD_BONUSES[i - k][j] == 'TW':
                    tw += 1

                    cross_words_scores[k] *= 3

        # Factor in double and triple words for the down word.
        for k in range(dw):
            down_word_score *= 2

        for k in range(tw):
            down_word_score *= 3
        
        # If the full rack is played, add 35 to the down word score.
        if len(rack_letter_indices) == 7:
            down_word_score += 35

        # Add cross word values to the down word value, and return it.
        for score in cross_words_scores:
            down_word_score += score

        return down_word_score

    def extend_down(index, rack, current_word, rack_played_incides):
        '''
        Given an anchor position, recursively compute possible down word plays by
        extending down on the board. For each word, compute its point value, and update
        the best_down_word score accordingly.

        Parameter {Array<int>} index the i, j index of the current position on the board.
        Parameter {Array<str>} rack the user's letter rack.
        Parameter {str} current_word the current permutation of the word.
        Parameter {Array<Array<int>>} rack_played_incides a list of the indices of letters played
        from the rack while extending down. 
        '''

        # Extract the gameboard coordinates.
        i, j = index

        # Base Case - no common letters or out of the gameboard bounds.
        if i > 14 or (GAME_BOARD[i][j] == ' ' and not intersection(rack, down_cross_checks[j][i])):
            return

        # For the current coordinate, find common letters between the rack and cross checks.
        common_letters = intersection(rack, down_cross_checks[j][i])

        # Case 1: empty cell.
        if GAME_BOARD[i][j] == ' ':
            for letter in common_letters:
                # Score the current word, if it's in the dictionary.
                if (current_word + letter).lower() in DICTIONARY:
                    if (i + 1 < 15 and GAME_BOARD[i + 1][j] == ' ') or i == 14:
                        word = current_word + letter
                        score = score_word_down(word, [i, j], rack_played_incides + [[i, j]])

                        # Update the best across word, if the score of the current word is better.
                        if score > best_down_word['score']:
                            best_down_word['last_letter_index'] = [i, j]
                            best_down_word['word'] = word
                            best_down_word['score'] = score
                
                # Keep extending down to form words.
                extend_down(
                    [i + 1, j],
                    filter_rack(rack, letter),
                    current_word + letter,
                    rack_played_incides + [[i, j]]
                )

        # Case 2: occupied cell.
        else:
            # Score the current word, if it's in the dictionary.
            if (current_word + GAME_BOARD[i][j]).lower() in DICTIONARY:
                if (i + 1 < 15 and GAME_BOARD[i + 1][j] == ' ') or i == 14:
                    word = current_word + GAME_BOARD[i][j]
                    score = score_word_down(word, [i, j], rack_played_incides)

                    # Update the best across word, if the score of the current word is better.
                    if score > best_down_word['score']:
                        best_down_word['last_letter_index'] = [i, j]
                        best_down_word['word'] = word
                        best_down_word['score'] = score

            # Keep extending down to form words.
            extend_down(
                [i + 1, j],
                rack,
                current_word + GAME_BOARD[i][j],
                rack_played_incides
            )

    def extend_down_with_top_part(index, rack, top_part):
        '''
        Given a position above an anchor, recursively compute possible down word
        plays by extending up before extending down on the board. For each word, compute 
        its point value, and update the best_down_word score accordingly.

        Parameter {Array<int>} index the i, j index of the current position on the board.
        Parameter {Array<str>} rack the user's letter rack.
        Parameter {str} top_part the current top_part of the word.
        '''

        # Extract the gameboard coordinates.
        i, j = index

        # Base Case - no common letters or out of the gameboard bounds.
        if i < 0 or not intersection(rack, down_cross_checks[j][i]):
            return

        # For the current coordinate, find common letters between the rack and cross checks.
        common_letters = intersection(rack, down_cross_checks[j][i])

        # Case 1: the cell above the current index is empty, or i = 0.
        if i == 0 or GAME_BOARD[i - 1][j] == ' ':
            for letter in common_letters:
                word = letter + top_part
                rack_played_incides = []

                for k in range(len(word)):
                    rack_played_incides += [[i + k, j]]

                # Extend down to form words.
                extend_down(
                    [i + len(word), j],
                    filter_rack(rack, letter),
                    word,
                    rack_played_incides
                )

                # Keep extending up.
                extend_down_with_top_part(
                    [i - 1, j],
                    filter_rack(rack, letter),
                    word
                )
        # Case 2: the cell above of the current index is occupied.
        else:
            pass

    # Compute best down word.
    for i in range(15):
        for j in range(15):
            if anchors[i][j]:
                # Case 1: cell above the anchor is empty.
                if i != 0 and GAME_BOARD[i - 1][j] == ' ':
                    extend_down(
                        [i, j],
                        RACK,
                        '',
                        []
                    )

                    extend_down_with_top_part(
                        [i - 1, j],
                        RACK,
                        ''
                    )
                # Case 2: cell above the anchor is occupied.
                else:
                    # Grab the word above the anchor, if there is one.
                    word = ''
                    k = i - 1
                    while k != -1 and GAME_BOARD[k][j] != ' ':
                        word = GAME_BOARD[k][j] + word
                        k -= 1

                    # Compute possible words extending down from the anchor.
                    extend_down(
                        [i, j],
                        RACK,
                        word,
                        []
                    )

    if best_across_word['score'] > best_down_word['score']:
        return best_across_word
    else:
        return best_down_word
