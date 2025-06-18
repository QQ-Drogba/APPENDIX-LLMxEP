# The predefined graph description language formats
def LAT_one_hop_format(u, v):
    """ LAT format for graph description language (one hop).
    :param u: The name of head entity.
    :param v: The name of tail entity.
    """
    return f"{v} is often used some time after {u} is used."

def CORR_one_hop_format(u, v):
    """ CORR format for graph description language (one hop).
    :param u: The name of head entity.
    :param v: The name of tail entity.
    """
    return f"{v} is often used with {u}."

def LAT_two_hop_format(u, v, w):
    """ LAT format for graph description language (two hops).
    :param u: The name of head entity.
    :param v: The intermediate entity.
    :param w: The name of tail entity.
    """
    return f"{w} is often used some time after {v} is used, which is often used some time after {u} is used."

def CORR_two_hop_format(u, v, w):
    """ CORR format for graph description language (two hops).
    :param u: The name of head entity.
    :param v: The intermediate entity.
    :param w: The name of tail entity.
    """
    return f"{w} is often used with {v}, which is often used with {u}."

def same_entity_pair_in_CORR_LAT_format(u, v, mode):
    """ Format for the same entity pair in CORR and LAT.
    :param u: The name of head entity.
    :param v: The name of tail entity.
    :param mode: '1' for both u -> v in CORR and LAT, '2' for u -> v in CORR, v -> u in LAT.
    """
    if mode == '1':
        return f"{v} is often used after {u} and occupies most of {u}'s operating time."
    elif mode == '2':
        return f"{v} is often used before {u} and occupies most of {u}'s operating time."

def entity_attribute_format(entity, attribute, value):
    """ Format for entity attributes.
    :param entity: The entity name.
    :param attribute: The attribute name.
    :param value: The attribute value.
    """
    return f"{entity} has the attribute {attribute} with value {value}."

def relation_format(relation, u, v):
    """ Format for relations between entities.
    :param relation: The relation type.
    :param u: The name of head entity.
    :param v: The name of tail entity.
    """
    if relation == 'CORR_WEEKDAY':
        return f"{v} is often used with {u} on weekdays."
    elif relation == 'CORR_WEEKEND':
        return f"{v} is often used with {u} on weekends."
    elif relation == 'LAT_WEEKDAY':
        return f"{v} is often used some time after {u} is used on weekdays."
    elif relation == 'LAT_WEEKEND':
        return f"{v} is often used some time after {u} is used on weekends."
    elif relation == 'BELONGS_TO':
        return f"{u} belongs to {v}."