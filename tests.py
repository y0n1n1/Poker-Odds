## TESTING ##
# Test case setup
def test_check_royal_flush():
    # Test case where a royal flush is present
    royal_flush_comb = ["AS", "KS", "QS", "JS", "10S"]
    all_combs = all_combinations(royal_flush_comb + ["AH", "KH", "QH"])  # Adding more cards to form other combinations
    result = check_royal_flush(all_combs)
    if result is not None and result[0] == "royal flush":
        print("test_check_royal_flush: Passed")
    else:
        print("test_check_royal_flush: Failed (Royal flush not detected or incorrect result)")

    # Test case where no royal flush exists
    non_royal_comb = ["AH", "KH", "QH", "JS", "10H"]
    all_combs = all_combinations(non_royal_comb + ["AC", "KD", "QC", "JC", "10C"])  # Adding more cards
    result = check_royal_flush(all_combs)
    if result is None:
        print("test_check_royal_flush (no royal flush): Passed")
    else:
        print("test_check_royal_flush (no royal flush): Failed (Royal flush detected)")

def test_check_straight_flush():
    # Test case where a straight flush is present
    straight_flush_comb = ["9S", "8S", "7S", "JS", "10S"]
    all_combs = all_combinations(straight_flush_comb + ["3H", "KH", "2H"])  # Adding more cards to form other combinations
    result = check_straight_flush(all_combs)
    if result is not None and result[0] == "straight flush":
        print("test_check_straight_flush: Passed")
    else:
        print("test_check_straight_flush: Failed (Straight flush not detected or incorrect result)")

    # Test case where no straight flush exists
    non_straight_flush_comb = ["AS", "KS", "QS", "JH", "10S"]
    all_combs = all_combinations(non_straight_flush_comb + ["AC", "4C", "QC", "JC", "10C"])
    result = check_straight_flush(all_combs)
    if result is None:
        print("test_check_straight_flush (no straight flush): Passed")
    else:
        print("test_check_straight_flush (no straight flush): Failed (Straight flush detected)")

def test_check_quads():
    # Test case where quads are present
    quads_comb = ["AS", "KS", "QS", "QD", "QC"]
    all_combs = all_combinations(quads_comb + ["AH", "KH", "QH"])
    result = check_quads(all_combs)
    if result is not None and result[0] == "quads":
        print("test_check_quads: Passed")
    else:
        print("test_check_quads: Failed (Quads not detected or incorrect result)")

    # Test case where no quads exist
    non_quads_comb = ["AS", "KS", "QS", "10S", "9S"]
    all_combs = all_combinations(non_quads_comb + ["AH", "KH", "QH", "JH", "10H"])
    result = check_quads(all_combs)
    if result is None:
        print("test_check_quads (no quads): Passed")
    else:
        print("test_check_quads (no quads): Failed (Quads detected)")

def test_check_full_house():
    # Test case where a full house is present
    full_house_comb = ["AS", "AS", "AS", "KS", "KS"]
    all_combs = all_combinations(full_house_comb + ["KH", "QH", "JH"])
    result = check_full_house(all_combs)
    if result is not None and result[0] == "full house":
        print("test_check_full_house: Passed")
    else:
        print("test_check_full_house: Failed (Full house not detected or incorrect result)")

    # Test case where no full house exists
    non_full_house_comb = ["AS", "KS", "QS", "JS", "10S"]
    all_combs = all_combinations(non_full_house_comb + ["AH", "KH", "QH", "JH", "10H"])
    result = check_full_house(all_combs)
    if result is None:
        print("test_check_full_house (no full house): Passed")
    else:
        print("test_check_full_house (no full house): Failed (Full house detected)")

def test_check_flush():
    # Test case where a flush is present
    flush_comb = ["3S", "7S", "QS", "AS", "10S"]
    all_combs = all_combinations(flush_comb + ["AH", "10H"])
    result = check_flush(all_combs)
    if result is not None and result[0] == "flush":
        print("test_check_flush: Passed")
    else:
        print("test_check_flush: Failed (Flush not detected or incorrect result)")

    # Test case where no flush exists
    non_flush_comb = ["7C", "6H", "5C", "4C", "3C"]
    all_combs = all_combinations(non_flush_comb + ["AH", "KH", "10H"])
    result = check_flush(all_combs)
    if result is None:
        print("test_check_flush (no flush): Passed")
    else:
        print("test_check_flush (no flush): Failed (Flush detected)")

def test_check_straight():
    # Test case where a straight is present
    straight_comb = ["AS", "KS", "QS", "JS", "10S"]
    all_combs = all_combinations(straight_comb + ["KH", "QH", "JH", "10H", "9H"])
    result = check_straight(all_combs)
    if result is not None and result[0] == "straight":
        print("test_check_straight: Passed")
    else:
        print("test_check_straight: Failed (Straight not detected or incorrect result)")

    # Test case where = straight exists
    non_straight_comb = ["AS", "4S", "5S", "7H", "10S"]
    all_combs = all_combinations(non_straight_comb + ["AC", "KC", "2C", "JC", "3C"])
    result = check_straight(all_combs)
    if result is not None and result[0] == "straight":
        print("test_check_straight (2): Passed")
    else:
        print("test_check_straight (2): Failed (Straight not detected)")

    # Test case where = straight doesn't exist
    non_straight_comb = ["AS", "4S", "6S", "7H", "10S"]
    all_combs = all_combinations(non_straight_comb + ["AC", "KC", "2C", "JC", "3C"])
    result = check_straight(all_combs)
    if result is  None:
        print("test_check_straight (no straight): Passed")
    else:
        print("test_check_straight (no straight): Failed (Straight detected)")

def test_check_trios():
    # Test case where trios are present
    trios_comb = ["AS", "AS", "AS", "KS", "QS"]
    all_combs = all_combinations(trios_comb + ["AH", "KH", "QH"])
    result = check_trios(all_combs)
    if result is not None and result[0] == "trios":
        print("test_check_trios: Passed")
    else:
        print("test_check_trios: Failed (Trios not detected or incorrect result)")

    # Test case where no trios exist
    non_trios_comb = ["AS", "KS", "QS", "10S", "9S"]
    all_combs = all_combinations(non_trios_comb + ["AH", "KH", "QH", "JH", "10H"])
    result = check_trios(all_combs)
    if result is None:
        print("test_check_trios (no trios): Passed")
    else:
        print("test_check_trios (no trios): Failed (Trios detected)")

def test_check_two_pair():
    # Test case where two pairs are present
    two_pair_comb = ["AS", "AS", "KS", "KS", "QS"]
    all_combs = all_combinations(two_pair_comb + ["AH", "KH", "QH"])
    result = check_two_pair(all_combs)
    if result is not None and result[0] == "two pair":
        print("test_check_two_pair: Passed")
    else:
        print("test_check_two_pair: Failed (Two pair not detected or incorrect result)")

    # Test case where no two pair exists
    non_two_pair_comb = ["AS", "KS", "QS", "10S", "9S"]
    all_combs = all_combinations(non_two_pair_comb + ["AH", "KH", "QH", "JH", "10H"])
    result = check_two_pair(all_combs)
    if result is None:
        print("test_check_two_pair (no two pair): Passed")
    else:
        print("test_check_two_pair (no two pair): Failed (Two pair detected)")

def test_check_pair():
    # Test case where a pair is present
    pair_comb = ["AS", "AS", "KS", "QS", "JS"]
    all_combs = all_combinations(pair_comb + ["AH", "KH", "QH"])
    result = check_pair(all_combs)
    if result is not None and result[0] == "pair":
        print("test_check_pair: Passed")
    else:
        print("test_check_pair: Failed (Pair not detected or incorrect result)")

    # Test case where no pair exists
    non_pair_comb = ["AS", "KS", "QS", "10S", "9S"]
    all_combs = all_combinations(non_pair_comb + ["AH", "KH", "QH", "JH", "10H"])
    result = check_pair(all_combs)
    if result is None:
        print("test_check_pair (no pair): Passed")
    else:
        print("test_check_pair (no pair): Failed (Pair detected)")

def test_if_consecutive():
    test_cases = [
        # Ace-low straight: A-2-3-4-5
        (['A', '2', '3', '4', '5'], True),
        
        # Ace-high straight: 10-J-Q-K-A
        (['10', 'J', 'Q', 'K', 'A'], True),
        
        # Regular straight: 2-3-4-5-6
        (['2', '3', '4', '5', '6'], True),
        
        # Regular straight: 6-7-8-9-10
        (['6', '7', '8', '9', '10'], True),
        
        # Non-consecutive: 2-3-5-6-7 (missing 4)
        (['2', '3', '5', '6', '7'], False),
        
        # Non-consecutive: 2-4-6-8-10 (even numbers only)
        (['2', '4', '6', '8', '10'], False),
        
        # Non-consecutive: 2-3-5-7-8 (missing 4 and 6)
        (['2', '3', '5', '7', '8'], False),
        
        # Non-consecutive: 10-K-Q-2-A (not consecutive)
        (['10', 'K', 'Q', '2', 'A'], False),
        
        # Regular straight: 4-5-6-7-8
        (['4', '5', '6', '7', '8'], True),
        
        # Non-consecutive: A-3-4-5-7 (missing 2)
        (['A', '3', '4', '5', '7'], False),
        
        # Non-consecutive: 10-8-9-J-Q (not consecutive)
        (['10', '8', '9', 'J', 'Q'], True),
        
        # Non-consecutive: 3-5-6-7-9 (missing 4 and 8)
        (['3', '5', '6', '7', '9'], False),
        
        # Straight with duplicate values: 2-2-3-4-5 (duplicate 2's)
        (['2', '2', '3', '4', '5'], False),
    ]

    for i, (cards, expected) in enumerate(test_cases):
        result = if_consecutive(cards)
        assert result == expected, f"Test case {i + 1} failed: {cards} => {result}, expected {expected}"
    print("test_if_consecutive: Passed")





def test_all():
    # Run all test functions
    test_check_royal_flush()
    test_check_straight_flush()
    test_check_quads()
    test_check_full_house()
    test_check_flush()
    test_check_straight()
    test_check_trios()
    test_check_two_pair()
    test_check_pair()
    test_if_consecutive()
