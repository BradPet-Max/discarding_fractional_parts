# =============================================================================
# 1.1 - Hotel Room Calculator
# =============================================================================

def rooms_needed(guests):
    """
    Calculates the minimum number of rooms needed for a group of guests,
    where each room can hold a maximum of 3 people.
    Returns None if guests is not a positive integer.
    """
    if not isinstance(guests, int) or guests <= 0:
        return None

    ROOM_CAPACITY = 3
    return -(-guests // ROOM_CAPACITY)  # Ceiling division


# --- Example usage ---
print("1.1 - rooms_needed()")
print(rooms_needed(9))    # 3 rooms (3 x 3)
print(rooms_needed(10))   # 4 rooms (3 + 3 + 3 + 1)
print(rooms_needed(1))    # 1 room
print(rooms_needed(0))    # None


# =============================================================================
# 1.2 - Subnetting 192.168.1.0/24
# =============================================================================

"""
SUBNETTING EXPLANATION
======================

Given:
    Network:        192.168.1.0/24
    Max hosts/subnet: 30

Step 1 - Find the number of host bits needed.
    We need enough host bits to support at least 30 hosts.
    Formula: 2^h - 2 >= 30   (subtract 2 for network and broadcast addresses)

    h = 5 -> 2^5 - 2 = 30  ✓  (exactly 30 usable hosts)

Step 2 - Calculate the new subnet mask.
    Total bits in IPv4 address = 32
    Host bits (h)              =  5
    Network bits               = 32 - 5 = 27
    New subnet mask            = /27  (255.255.255.224)

Step 3 - Calculate the number of subnets.
    Original prefix length     = 24
    New prefix length          = 27
    Subnet bits borrowed       = 27 - 24 = 3
    Number of subnets          = 2^3 = 8

ANSWER: 8 subnets can be created.

Subnet breakdown (block size = 32):
    Subnet 1:  192.168.1.0   - 192.168.1.31   (usable: .1   - .30)
    Subnet 2:  192.168.1.32  - 192.168.1.63   (usable: .33  - .62)
    Subnet 3:  192.168.1.64  - 192.168.1.95   (usable: .65  - .94)
    Subnet 4:  192.168.1.96  - 192.168.1.127  (usable: .97  - .126)
    Subnet 5:  192.168.1.128 - 192.168.1.159  (usable: .129 - .158)
    Subnet 6:  192.168.1.160 - 192.168.1.191  (usable: .161 - .190)
    Subnet 7:  192.168.1.192 - 192.168.1.223  (usable: .193 - .222)
    Subnet 8:  192.168.1.224 - 192.168.1.255  (usable: .225 - .254)
"""

import math

def subnetting(network_prefix, max_hosts):
    """
    Calculates the number of subnets that can be created given a network
    prefix length and the maximum number of hosts per subnet.

    Args:
        network_prefix (int): The original prefix length (e.g. 24 for /24)
        max_hosts (int):      Maximum number of usable hosts per subnet

    Returns:
        dict with host_bits, new_prefix, subnet_bits, num_subnets
    """
    # Find host bits needed: 2^h - 2 >= max_hosts
    host_bits = math.ceil(math.log2(max_hosts + 2))

    new_prefix   = 32 - host_bits
    subnet_bits  = new_prefix - network_prefix
    num_subnets  = 2 ** subnet_bits
    usable_hosts = (2 ** host_bits) - 2

    return {
        "original_prefix" : f"/{network_prefix}",
        "new_prefix"      : f"/{new_prefix}",
        "host_bits"       : host_bits,
        "subnet_bits"     : subnet_bits,
        "num_subnets"     : num_subnets,
        "usable_hosts"    : usable_hosts
    }


# --- Example usage ---
print("\n1.2 - subnetting()")
result = subnetting(24, 30)
for key, value in result.items():
    print(f"  {key}: {value}")
