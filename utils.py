def kendall_tau_distance(r1, r2):
    """Compute the Kendall tau distance between two rankings.
    
    :param r1: Preference ranking 1
    :param r2: Preference ranking 2

    :return: Kendall tau distance (non-negative integer)
    """
    index_r1 = {c: i for i, c in enumerate(r1)}
    index_r2 = {c: i for i, c in enumerate(r2)}
    
    distance = 0
    n = len(r1)
    for i in range(n):
        for j in range(i + 1, n):
            a, b = r1[i], r1[j]
            if (index_r1[a] < index_r1[b] and index_r2[a] > index_r2[b]):
                distance += 1
    return distance

def squared_kendall_tau_distance(r1, r2):
    """Compute the squared Kendall tau distance between two rankings.
    
    :param r1: Preference ranking 1
    :param r2: Preference ranking 2

    :return: Squared Kendall tau distance (non-negative integer)
    """
    return kendall_tau_distance(r1, r2) ** 2

def spearman_footrule_distance(r1, r2):
    """Compute the Spearman's footrule distance between two rankings.
    
    :param r1: Preference ranking 1 (list of candidate IDs)
    :param r2: Preference ranking 2 (same candidates, permuted)

    :return: Footrule distance (non-negative integer)
    """
    index_r1 = {c: i for i, c in enumerate(r1)}
    index_r2 = {c: i for i, c in enumerate(r2)}
    
    distance = 0
    for c in r1:
        distance += abs(index_r1[c] - index_r2[c])
    
    return distance

def is_satisfied(voter_ranking, output_ranking, threshold=0):
    """Determines whether the voter is satisfied with the output ranking 
    based on the specified threshold. This is the case if the Kendall tau
    distance between the voter ranking and output ranking is not greater
    than the threshold value.
    
    :param voter_ranking: Voter's preference ranking
    :param output_ranking: Output ranking
    :param threshold: A non-negative integer specifying the satisfaction threshold. Defaults to 0.
    :return: 'True' if the voter is satisfied, 'False' otherwise.
    """
    if kendall_tau_distance(voter_ranking, output_ranking) <= threshold:
        return True
    return False

