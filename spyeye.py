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
    
    for i in range(20): print("")
    for type, amount in statistics.items():
        if(amount!=0):
            print(f"{type}: {amount} possibilities, {(amount/tot)*100}% chance")
 



from inference import InferencePipeline
from inference.core.interfaces.camera.entities import VideoFrame
from inference.core.interfaces.stream.sinks import render_boxes

# Create an instance of FPSMonitor
# import opencv to display our annotated images
import cv2
# import supervision to help visualize our predictions
import supervision as sv
fps_monitor = sv.FPSMonitor()

# create a bounding box annotator and label annotator to use in our custom sink
label_annotator = sv.LabelAnnotator()
box_annotator = sv.BoxAnnotator()
import json

# Define the dictionary you want to s
from datetime import datetime

# Get the current time
from collections import Counter

def filter_by_copies(input_dict, min_copies, min_confidence):
    """
    Filters out items in predictions whose class_id does not appear at least min_copies times,
    but allows single items if their confidence is above the given min_confidence.

    Args:
        input_dict (dict): The input dictionary containing a "predictions" key.
        min_copies (int): The minimum number of times a class_id must appear to be retained.
        min_confidence (float): The minimum confidence threshold to consider for filtering.

    Returns:
        dict: The updated dictionary with filtered predictions.
    """
    

    # Get all predictions
    predictions = input_dict.get("predictions", [])
    
    # Step 1: Check if any item has confidence above the threshold
    if any(prediction["confidence"] > min_confidence for prediction in predictions):
        return input_dict  # If any item has high confidence, return the input_dict unchanged
    
    # Step 2: Count the occurrences of each class_id
    class_counts = Counter(prediction["class_id"] for prediction in predictions)

    # Step 3: Filter predictions to retain only those where:
    # - The class_id appears at least min_copies times, or
    # - The confidence is above the min_confidence
    filtered_predictions = [
        prediction for prediction in predictions
        if class_counts[prediction["class_id"]] >= min_copies or prediction["confidence"] > min_confidence
    ]

    # Step 4: Update the input dictionary with filtered predictions
    input_dict["predictions"] = filtered_predictions

    return input_dict


def filter_to_class(input_dict):
    # Create a dictionary to store the highest confidence for each class_id
    class_dict = {}
    # Create a dictionary to store the sum of confidence values for each class_id
    class_confidence_sum = {}

    # Iterate over each prediction
    for prediction in input_dict.get("predictions", []):
        class_id = prediction["class_id"]
        confidence = prediction["confidence"]
        
        # If this class_id is not in class_dict or if the confidence is higher than the stored one
        if class_id not in class_dict or confidence > class_dict[class_id]["confidence"]:
            class_dict[class_id] = prediction
        
        # Add the confidence to the sum for this class_id
        if class_id in class_confidence_sum:
            class_confidence_sum[class_id] += confidence
        else:
            class_confidence_sum[class_id] = confidence

    # Add the confidence sum to each prediction in class_dict
    for prediction in class_dict.values():
        class_id = prediction["class_id"]
        prediction["confidence_sum"] = class_confidence_sum[class_id]

    # Update the "predictions" key to only include the filtered predictions
    input_dict["predictions"] = list(class_dict.values())

    return input_dict

import math
def filter_by_confidence(input_dict, min_confidence):
    """
    Filters the predictions list to include only items with a confidence score
    greater than or equal to min_confidence.

    Args:
        input_dict (dict): The input dictionary containing a "predictions" key.
        min_confidence (float): The minimum confidence score to retain an item.

    Returns:
        dict: The updated dictionary with filtered predictions.
    """
    filtered_predictions = [
        prediction for prediction in input_dict.get("predictions", [])
        if prediction["confidence"] >= min_confidence
    ]

    # Update the input dictionary with the filtered predictions
    input_dict["predictions"] = filtered_predictions
    return input_dict


def filter_by_proximity(input_dict, max_distance):
    """
    Filters the predictions list by removing items with very similar (x, y) coordinates,
    keeping only the one with the highest confidence value.

    Args:
        input_dict (dict): The input dictionary containing a "predictions" key.
        max_distance (float): The maximum Euclidean distance between (x, y) coordinates
                              to consider them "similar".

    Returns:
        dict: The updated dictionary with filtered predictions.
    """
    predictions = input_dict.get("predictions", [])
    filtered_predictions = []
    processed_indices = set()

    for i, pred1 in enumerate(predictions):
        if i in processed_indices:
            continue

        # Group predictions that are within max_distance of pred1
        similar_predictions = [pred1]
        for j, pred2 in enumerate(predictions):
            if i != j and j not in processed_indices:
                distance = math.sqrt((pred1["x"] - pred2["x"])**2 + (pred1["y"] - pred2["y"])**2)
                if distance <= max_distance:
                    similar_predictions.append(pred2)
                    processed_indices.add(j)

        # Keep only the one with the highest confidence
        best_prediction = max(similar_predictions, key=lambda p: p["confidence"])
        filtered_predictions.append(best_prediction)
        processed_indices.add(i)

    # Update the input dictionary with the filtered predictions
    input_dict["predictions"] = filtered_predictions
    return input_dict

def spy(predictions):
    predictions_list = []
    for prediction in predictions.get("predictions", []):
        confidence = prediction["confidence"]
        x, y = prediction["x"], prediction["y"]
        class_name = prediction['class']
        w, h = prediction["width"], prediction["height"]
        predictions_list.append(f"C:{class_name} Conf: {confidence}. ({x},{y}), WH ({w}, {h})")
    
    for it in predictions_list:
        print(it)

def remove_ghost_pairs(input_dict):
    """
    Removes 'ghost' items from predictions if their confidence is below 0.2
    when a matching item with more than 0.2 confidence exists for the given class.

    Args:
        input_dict (dict): Dictionary containing a "predictions" key with a list of predictions.
        ghost_pairs (dict): Dictionary mapping class names of items that can appear as ghosts.

    Returns:
        dict: The input_dict with the ghost items removed.
    """
    ghost_pairs = {
        "3H": ["2H"],  # Class 3S can have ghost items of Class 2S
        "3S": ["2S"],  
        "5C": ["4C"],  
        "KH": ["QH"],  
        "AD": ["2D"],  
        "9H": ["JH"],  
        "JD": ["KD"],  
        "JS": ["QS"],  
        "6C": ["5C"],  
        "6S": ["5S"],  
        "6D": ["5D"],  
        "6H": ["5H"],  
        "7D": ["8D"],  
        "7S": ["8S"],  
        "7C": ["6C"],  
        "7C": ["8C"],  
        "7H": ["6H"],  
        "8H": ["7H"],  
        "9D": ["TD"]
        # Add other class relationships as needed
    }
    
    # Step 1: Store the predictions
    predictions = input_dict.get("predictions", [])
    
    # Step 2: Identify and store items that have confidence greater than 0.2
    active_items = {}
    for prediction in predictions:
        class_name = prediction["class"]
        confidence = prediction["confidence"]
        
        if confidence > 0.2:
            if class_name not in active_items:
                active_items[class_name] = []
            active_items[class_name].append(prediction)
    
    # Step 3: Filter out ghost items with less than 0.2 confidence based on the ghost_pairs
    filtered_predictions = []
    for prediction in predictions:
        class_name = prediction["class"]
        confidence = prediction["confidence"]
        
        # Check if this prediction is a potential ghost (confidence < 0.2)
        if confidence < 0.2:
            # Check if this class_name has a corresponding 'active' class_name in ghost_pairs
            for active_class in ghost_pairs.get(class_name, []):
                if active_class in active_items:
                    filtered_predictions.append(prediction)  # Keep the ghost if no active item exists
                    break
        else:
            # Keep the item with confidence > 0.2
            filtered_predictions.append(prediction)
    
    # Update the predictions with filtered results
    input_dict["predictions"] = filtered_predictions
    return input_dict

def remove_ghost_trios(input_dict):
    ghost_trios = {
        "7H": ["7D", "8H"],  # Define ghost trios
        "6D": ["7D", "8H"],  # Define ghost trios
    }
    
    # Step 1: Store the predictions
    predictions = input_dict.get("predictions", [])
    
    # Step 2: Identify and store items that have confidence greater than 0.25
    active_items = {}
    for prediction in predictions:
        class_name = prediction["class"]
        confidence = prediction["confidence"]
        
        if confidence > 0.25:
            if class_name not in active_items:
                active_items[class_name] = []
            active_items[class_name].append(prediction)
    
    # Step 3: Filter out ghost items with less than 0.25 confidence based on the ghost_trios
    filtered_predictions = []
    for prediction in predictions:
        class_name = prediction["class"]
        confidence = prediction["confidence"]
        
        if confidence < 0.25:
            # If the class is part of a ghost trio and the corresponding classes are active with confidence > 0.25
            if class_name in ghost_trios:
                required_classes = ghost_trios[class_name]
                
                # Check if both required classes have confidence > 0.25
                if all(required_class in active_items and any(p["confidence"] > 0.25 for p in active_items[required_class]) for required_class in required_classes):
                    continue  # Skip this ghost item (7H) if the required classes are present with high confidence
            
        # If the item should not be removed, append it to the result
        filtered_predictions.append(prediction)
    
    # Update the predictions with filtered results
    input_dict["predictions"] = filtered_predictions
    return input_dict

    predictions_list = []

import numpy as np
from itertools import combinations

# Function to calculate the line's deviation for a given set of points
def calculate_line_deviation(points):
    # Extracting x and y coordinates
    x_vals = np.array([p[0] for p in points])
    y_vals = np.array([p[1] for p in points])
    
    # Fit a line using polyfit (degree 1)
    coefficients = np.polyfit(x_vals, y_vals, 1)
    
    # Calculate the fitted y-values based on the line equation
    y_fit = np.polyval(coefficients, x_vals)
    
    # Calculate the sum of squared deviations from the fitted line
    deviation = np.sum((y_vals - y_fit) ** 2)
    
    return deviation

# Function to detect community cards and player cards based on the input predictions
def detect_card_groups(predictions):
    coords = [(prediction["x"], prediction["y"], prediction["class"]) for prediction in predictions.get("predictions", [])]
    
    # Sort the points based on their x-coordinate to maintain left-to-right order
    coords = sorted(coords, key=lambda x: x[0])

    num_coords = len(coords)
    
    # Set the number of community cards based on the number of input coordinates
    if num_coords == 5:
        community_card_count = 3  # 5 coordinates, 3 community cards
    elif num_coords == 6:
        community_card_count = 4  # 6 coordinates, 4 community cards
    elif num_coords == 7:
        community_card_count = 5  # 7 coordinates, 5 community cards
    else:
        raise ValueError("Input should contain 5, 6, or 7 coordinates.")
    
    community_cards = []
    player_cards = []

    best_deviation = float('inf')
    best_combination = []

    # Generate all combinations of points of length community_card_count
    for comb in combinations(coords, community_card_count):
        # Calculate deviation for this combination
        deviation = calculate_line_deviation(comb)
        
        # Update the best combination if this one has a smaller deviation
        if deviation < best_deviation:
            best_deviation = deviation
            best_combination = comb
    
    # The selected best combination are the community cards
    community_cards = list(best_combination)

    # The remaining points are considered as player cards
    community_set = set((card[0], card[1]) for card in community_cards)
    for card in coords:
        if (card[0], card[1]) not in community_set:
            player_cards.append(card)

    # Create output lists for class names
    community_classes = [card[2] for card in community_cards]
    player_classes = [card[2] for card in player_cards]

    return community_classes, player_classes

def on_prediction_test(predictions, video_frame):
    for i in range(20): print("")
    spy(predictions)
    end_preds = filter_by_confidence(remove_ghost_trios(
        remove_ghost_pairs(
                filter_to_class(
                    filter_by_proximity(
                        filter_by_copies(predictions, 2, 0.10), 50)))), 0.1)
    groups = detect_card_groups(end_preds)
    
    print("")
    print("FINAL")
    spy(end_preds)
    print("")
    print(groups)

    render_boxes(
        predictions=end_preds,
        video_frame=video_frame,
        fps_monitor=fps_monitor,  # Pass the FPS monitor object
        display_statistics=True, # Enable displaying statistics
        display_size=(600, 400)
    )

def on_prediction_run(predictions, video_frame):
    end_preds = filter_by_confidence(remove_ghost_trios(
        remove_ghost_pairs(
                filter_to_class(
                    filter_by_proximity(
                        filter_by_copies(predictions, 2, 0.10), 50)))), 0.1)
    groups = detect_card_groups(end_preds)
    
    stats(groups[1], groups[0])

    render_boxes(
        predictions=end_preds,
        video_frame=video_frame,
        fps_monitor=fps_monitor,  # Pass the FPS monitor object
        display_statistics=True, # Enable displaying statistics
        display_size=(600, 400)
    )



# initialize a pipeline object
pipeline = InferencePipeline.init(
    model_id="pokeryoloyolo/2", # Roboflow model to use
    video_reference=1, # Path to video, device id (int, usually 0 for built in webcams), or RTSP stream url
    on_prediction=on_prediction_run, # Function to run after each prediction
    api_key="TYPE IN HERE",
    confidence=0.1,
    mask_decode_mode="fast",
    max_candidates=1000,
    max_detections=30,
    iou_threshold=0.2,
    tradeoff_factor=1
)
pipeline.start()
pipeline.join()
pipeline.finish()

