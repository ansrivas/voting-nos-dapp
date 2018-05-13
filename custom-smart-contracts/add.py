"""
NeoSense Smart Contract based Licensing
Created by Dean van Dugteren (City of Zion, VDT Network)
hello@dean.press
"""

from boa.interop.Neo.Runtime import CheckWitness, Log
from boa.interop.Neo.Storage import GetContext, Put, Delete, Get
from boa.builtins import concat


def is_owner(product_id):
    """
    Verify that the product is owned by the requesting user.
    """
    print('Am I the product owner?')
    product_owner = Get(GetContext(), product_id)
    is_product_owner = CheckWitness(product_owner)
    if not is_product_owner:
        print('Not the product owner!')
    return is_product_owner


def Main(operation, args):
    """
    Main definition for the smart contracts

    :param operation: the operation to be performed
    :type operation: str

    :param args: list of arguments.
        args[0] is always sender script hash
        args[1] is always product_id
        args[2] (optional) is always another script hash
    :param type: str

    :return:
        byterarray: The result of the operation
    """
    # Am I who I say I am?
    user_hash = args[0]
    authorized = CheckWitness(user_hash)
    if not authorized:
        Log("Not Authorized")
        return False
    Log("Authorized")

    if operation is not None:
        if operation == 'add':
            Log('add invoked')
            return args[1] + args[2]

    Log('Inknown operation')
    return False
