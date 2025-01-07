all_cards = [
    "AS", "KS", "QS", "JS", "10S", "9S", "8S", "7S", "6S", "5S", "4S", "3S", "2S",
    "AH", "KH", "QH", "JH", "10H", "9H", "8H", "7H", "6H", "5H", "4H", "3H", "2H",
    "AD", "KD", "QD", "JD", "10D", "9D", "8D", "7D", "6D", "5D", "4D", "3D", "2D",
    "AC", "KC", "QC", "JC", "10C", "9C", "8C", "7C", "6C", "5C", "4C", "3C", "2C"
]

rank_order = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, '10': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2}
hand_order = {'royal flush': 11, 
              'straight flush': 10, 
              'quads': 9, 
              'full house': 7, 
              'flush': 6, 
              'straight': 5, 
              'trios': 4, 
              'two pair': 3, 
              'pair': 2, 
              'high card': 1}

def all_equal_suit(lst):
    lst = [card[-1] for card in lst]
    # Check if all elements are equal to the first element
    return all(element == lst[0] for element in lst)

def order_ranks(card_ranks):
    # Sort the card ranks based on their numeric values
    return sorted(card_ranks, key=lambda x: rank_order[x])

def order_cards(cards):
    # Define a custom sort key function
    def sort_key(card):
        rank = card[:-1]
        return rank_order[rank]
    # Sort the cards based on the custom sort key function
    sorted_cards = sorted(cards, key=sort_key, reverse=True)
    return sorted_cards

def if_consecutive(card_ranks):
    numeric_ranks = [rank_order[rank] for rank in card_ranks]

    # Check if the difference between adjacent ranks is 1
    if numeric_ranks==[2,3,4,5,14]: return True
    for i in range(len(numeric_ranks) - 1):
        if numeric_ranks[i + 1] - numeric_ranks[i] != 1:
            return False
    return True

def all_combinations(items):
    permutations = []
    n = len(items)
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                for l in range(k+1, n):
                    for m in range(l+1, n):
                        permutations.append([items[i], items[j], items[k], items[l], items[m]])
    return permutations

def best_hand(full:list):
    # get all combs
    all_combs = all_combinations(full)
    # check for royal flush
    all_royals = [["AS", "KS", "QS", "JS", "10S"],
                  ["AH", "KH", "QH", "JH", "10H"],
                  ["AD", "KD", "QD", "JD", "10D"],
                  ["AC", "KC", "QC", "JC", "10C"]]
    for royal in all_royals:
        if royal in all_combs:
            return ["royal flush", royal[0][-1], "A",None,royal]
    # check for straight flush
    straight_flushes = []
    for comb in all_combs:
        # check same suit
        if all_equal_suit(comb):
            comb_vals = []
            for card in comb:
                if (len(card)==2):comb_vals.append(card[0])
                else:comb_vals.append(card[0:2])
            # order in ascending
            if if_consecutive(order_ranks(comb_vals)):
                straight_flushes.append(["straight flush", comb[0][-1], order_ranks(comb_vals)[-1],None,comb])
    if len(straight_flushes)!=0:
        top_ranks = order_ranks([straight_flush[2] for straight_flush in straight_flushes])
        top_ranks_dict = {straight_flush[2]:straight_flush for straight_flush in straight_flushes}
        return top_ranks_dict.get(top_ranks[-1])
    # check for quads
    for comb in all_combs:
        ranks = []
        for card in comb:
            if card[0]!="1":ranks.append(card[0]) 
            else: ranks.append(card[0:2])
        rank_count = {}
        for rank in ranks:
            rank_count[rank] = rank_count.get(rank, 0) + 1
        for count in rank_count.values():
            if count == 4:
                quad_rank = [k for k, v in rank_count.items() if v == 4]
                if len(quad_rank)==2:quad_rank=quad_rank[0]
                else: quad_rank=quad_rank[0:2]
                return ["quads", None,quad_rank[0],None, comb]
    # check for full house
    full_houses = []
    for comb in all_combs:
        ranks = []
        for card in comb:
            if len(card)==2:ranks.append(card[0]) 
            else: ranks.append(card[0:2])
        rank_count = {}
        for rank in ranks:
            rank_count[rank] = rank_count.get(rank, 0) + 1
        trees = {}
        for rank, count in rank_count.items():
            if count == 3:
                trees[rank] = rank_count[rank]
        if trees:
            twos = {}
            for rank, count in rank_count.items():
                if count == 2:
                    twos[rank] = rank_count[rank]
            if twos:
                trios = []
                pair = []
                for key, val in trees.items():
                    if val == 3:trios.append(key)
                for key, val in twos.items():
                    if val == 2:pair.append(key)
                full_houses.append(['full house', None, trios[0], pair[0], comb])
    if len(full_houses)!=0:
        top_ranks_trio = order_ranks([full_house[2] for full_house in full_houses])
        top_ranks_trio_dict = {str(n):full_house[2] for n,full_house in enumerate(full_houses)}
        top_trios = []
        for key, val in top_ranks_trio_dict.items():
            if val == top_ranks_trio[-1]:top_trios.append(full_houses[int(key)])
        top_ranks_duo = order_ranks([full_house_p[3] for full_house_p in top_trios])
        top_ranks_duo_dict = {full_house_p2[3]:full_house_p2 for full_house_p2 in top_trios}
        return top_ranks_duo_dict.get(top_ranks_duo[-1])  
    # check for flush
    flushes = []
    for comb in all_combs:
        # check same suit
        if all_equal_suit(comb):
            comb_vals = []
            for card in comb:
                if (len(card)==2):comb_vals.append(card[0])
                else:comb_vals.append(card[0:2])
            flushes.append(["flush", comb[0][-1], order_ranks(comb_vals)[-1],None,comb])
    if len(flushes)!=0:
        top_ranks = order_ranks([flush[2] for flush in flushes])
        top_ranks_dict = {flush[2]:flush for flush in flushes}
        return top_ranks_dict.get(top_ranks[-1])
    # check for straight
    straights = []
    for comb in all_combs:
        comb_vals = []
        for card in comb:
            if (len(card)==2):comb_vals.append(card[0])
            else:comb_vals.append(card[0:2])
        # order in ascending
        if if_consecutive(order_ranks(comb_vals)):
            straights.append(["straight", None, order_ranks(comb_vals)[-1],None,comb])
    if len(straights)!=0:
        top_ranks = order_ranks([straight[2] for straight in straights])
        top_ranks_dict = {straight[2]:straight for straight in straights}
        return top_ranks_dict.get(top_ranks[-1])
    # check for trios
    trios = []
    for comb in all_combs:
        ranks = []
        for card in comb:
            if len(card)==2:ranks.append(card[0]) 
            else: ranks.append(card[0:2])
        rank_count = {}
        for rank in ranks:
            rank_count[rank] = rank_count.get(rank, 0) + 1
        trees = {}
        for rank, count in rank_count.items():
            if count == 3:
                trees[rank] = rank_count[rank]
        if trees:
            three_comb = []
            for key, val in trees.items():
                if val == 3:three_comb.append(key)
            trios.append(['trios', None, three_comb[0], None, comb])
    if len(trios)!=0:
        top_ranks_trio = order_ranks([threeo[2] for threeo in trios])
        top_ranks_trio_dict = {threeo[2]:threeo for threeo in trios}
        return top_ranks_trio_dict.get(top_ranks_trio[-1])  
    # check for two pair
    two_pairs = []
    for comb in all_combs:
        ranks = []
        for card in comb:
            if len(card)==2:ranks.append(card[0]) 
            else: ranks.append(card[0:2])
        rank_count = {}
        for rank in ranks:
            rank_count[rank] = rank_count.get(rank, 0) + 1
        twos = {}
        for rank, count in rank_count.items():
            if count == 2:
                twos[rank] = rank_count[rank]
        if len(twos)>1:
            two_combs = []
            for key, val in twos.items():
                if val == 2:two_combs.append(key)
            two_pairs.append(['two pair', None, order_ranks(two_combs)[-1], order_ranks(two_combs)[-2], comb])
    if len(two_pairs)!=0:
        top_ranks_top_pair = order_ranks([pairo[2] for pairo in two_pairs])
        top_ranks_top_pair_dict = {str(n):pairo[2] for n,pairo in enumerate(two_pairs)}
        top_pairs = []
        for key, val in top_ranks_top_pair_dict.items():
            if val == top_ranks_top_pair[-1]:top_pairs.append(two_pairs[int(key)])
        top_ranks_bottom_pair = order_ranks([bottom_pair[3] for bottom_pair in top_pairs])
        top_ranks_top_bottom_dict = {bottom_pair[3]:bottom_pair for bottom_pair in top_pairs}
        return top_ranks_top_bottom_dict.get(top_ranks_bottom_pair[-1])     
    # check for pair
    pairs = []
    for comb in all_combs:
        ranks = []
        for card in comb:
            if len(card)==2:ranks.append(card[0]) 
            else: ranks.append(card[0:2])
        rank_count = {}
        for rank in ranks:
            rank_count[rank] = rank_count.get(rank, 0) + 1
        twos = {}
        for rank, count in rank_count.items():
            if count == 2:
                twos[rank] = rank_count[rank]
        if twos:
            two_comb = []
            for key, val in twos.items():
                if val == 2:two_comb.append(key)
            pairs.append(['pair', None, two_comb[0], None, comb])
    if len(pairs)!=0:
        top_ranks_pair = order_ranks([pairo[2] for pairo in pairs])
        top_ranks_pair_dict = {pairo[2]:pairo for pairo in pairs}
        return top_ranks_pair_dict.get(top_ranks_pair[-1])  
    # check for high card
    high_comb = order_cards(full)
    return ['high card', None, high_comb[0][0], None, high_comb]

def n_shared_cards(cards1, cards2):
    # Convert lists to sets to find the intersection (cards present in both lists)
    set1 = set(cards1)
    set2 = set(cards2)
    # Find the intersection of the two sets
    shared_cards = set1.intersection(set2)
    # Return the number of shared cards
    return len(shared_cards)

def compare(hand1:list,player1:list, hand2:list,player2:list):
    # compare on TYPE
    type_diff = hand_order[hand1[0]] - hand_order[hand2[0]]
    if type_diff>0:return [1., 0.]
    if type_diff<0:return [0., 1.]
    # if same type, compare on TYPE's top card
    if (hand1[0]=='royal flush'): return [0.5,0.5] # ALL royal flushes that two or more players have must be table royal flushes
    if (hand1[0]=='quads'): return [0.5,0.5] # ALL quads that two or more players have must be table quads
    # COMPARING TOP CARD:
    if hand1[2]!=hand2[2]: 
        top_card_diff = rank_order[hand1[2]] - rank_order[hand2[2]]
        if top_card_diff>0:return [1., 0.]
        if top_card_diff<0:return [0., 1.]
    # if same top card, and there is a TYPE bottom card, compare on TYPE bottom card
    if hand1[3]!=None:
        type_bottom_card_diff = rank_order[hand1[3]] - rank_order[hand2[3]]
        if type_bottom_card_diff>0:return [1., 0.]
        if type_bottom_card_diff<0:return [0., 1.]
    # if still same, compare on player hands
    this_diff = rank_order[order_cards(player1)[0][0]] - rank_order[order_cards(player2)[0][0]]
    if this_diff>0:return [1., 0.]
    if this_diff<0:return [0., 1.]
    that_diff = rank_order[order_cards(player1)[1][0]] - rank_order[order_cards(player2)[1][0]]
    if that_diff>0:return [1., 0.]
    if that_diff<0:return [0., 1.]
    return [0.5, 0.5]

def to_win_vector(numbers:list):
    max_value = max(numbers)
    max_count = numbers.count(max_value)
    
    max_value_replacement = 1 / max_count
    
    result = [max_value_replacement if x == max_value else 0 for x in numbers]
    return result

def winner(player_hands:dict, board:list):
    # find best combo for each player
    net = [0. for player in player_hands]
    for n,player in enumerate(player_hands):
        their_best = best_hand(player+board)
        for compare_player in player_hands:
            win = compare(their_best, player,best_hand(compare_player+board), compare_player)
            #print(f"player1: {their_best} player2: {best_hand(compare_player)} win: {win}")
            if win[0]==1.0: # current wins
                net[n] +=1.
            if win[0]==0.5: 
                net[n] +=0.5
    return to_win_vector(net)
    
def add_two_lists(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length")
    
    return [a + b for a, b in zip(list1, list2)]

def vector_to_probabilities(vector):
    total = sum(vector)
    if total == 0:
        raise ValueError("Sum of the input vector must not be zero")
    
    return [x / total for x in vector]

def vector_to_percentages(vector):
    total = sum(vector)
    if total == 0:
        raise ValueError("Sum of the input vector must not be zero")
    
    return [(x / total) * 100 for x in vector]

def odds(player_hands:list, board:list, show_ties=False):
    turn = len(board)
    rem = 5-turn # 2>flop, 1> turn, 0> river
    if rem==0:
        return vector_to_percentages(winner(player_hands, board))

    shown_cards = []
    for card in board:shown_cards.append(card)
    for player in player_hands:
        for card in player:shown_cards.append(card)
    #shown_cards contains all cards taken from deck
    remaining_cards = [item for item in all_cards if item not in shown_cards]
    all_odds = []
    if rem==1:
        for i in remaining_cards:all_odds.append([i])
    if rem==2:
        for card in remaining_cards:
            rem_after = [i for i in remaining_cards if i!=card]
            for sec_card in rem_after:all_odds.append([card, sec_card])

    # NOW THIS IS FOR TWO OR ONE OR ZERO CARDS, PROBABLY NOT USEFUL        
    if rem==5:
        import itertools
        for combo in itertools.combinations(remaining_cards, 5):
            all_odds.append(list(combo))

    #print(all_odds)
    wins_vector = [0. for player in player_hands]
    tot = len(all_odds)
    for n,odd in enumerate(all_odds):
        #print(f"{n}/{tot}, {(n/tot)*100}% Complete")
        this_board = odd + board
        #print(this_board)
        wins_vector = add_two_lists(wins_vector, winner(player_hands, this_board))
        #print(wins_vector)
    return vector_to_percentages(wins_vector)
            
def stats(player:list, board:list):
    turn = len(board)
    rem = 5-turn # 2>flop, 1> turn

    shown_cards = []
    for card in board:shown_cards.append(card)
    for card in player:shown_cards.append(card)
    #shown_cards contains all cards taken from deck
    remaining_cards = [item for item in all_cards if item not in shown_cards]
    all_odds = []
    if rem==1:
        for i in remaining_cards:all_odds.append([i])
    if rem==2:
        for card in remaining_cards:
            rem_after = [i for i in remaining_cards if i!=card]
            for sec_card in rem_after:all_odds.append([card, sec_card])
    tot = len(all_odds)
    statistics = {'royal flush': 0, 
              'straight flush': 0, 
              'quads': 0, 
              'full house': 0, 
              'flush': 0, 
              'straight': 0, 
              'trios': 0, 
              'two pair': 0, 
              'pair': 0, 
              'high card': 0}


    for n,odd in enumerate(all_odds):
        #print(f"{n}/{tot}, {(n/tot)*100}% Complete")
        this_full = odd + board+player
        #print(this_board)
        best = best_hand(this_full)[0]
        statistics[best]+=1
    
    for type, amount in statistics.items():
        print(f"{type}: {amount} possibilities, {(amount/tot)*100}% chance")
 
