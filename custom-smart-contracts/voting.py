# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Initialize module utils."""

from boa.builtins import concat, has_key, keys, list
from boa.interop.Neo.Runtime import CheckWitness, GetTrigger, Log, Serialize, Deserialize
from boa.interop.Neo.Storage import Delete, Get, GetContext, Put
from boa.interop.Neo.TriggerType import Application, Verification

from boa.interop.System.ExecutionEngine import GetCallingScriptHash
from boa.interop.Neo.Storage import Get, Put, Delete, GetContext


ALLOWED_CONTENDERS = {
    'BO': 'Barack Obama',
    'DT': 'Donald Trump'
}


def check_vote(ctx, address, contender):
    """
    Looks up the KYC status of an address
    :param address:bytearray The address to lookup
    :param storage:StorageAPI A StorageAPI object for storage interaction
    :return:
        bool: KYC Status of address
    """
    kyc_storage_key = concat('voted_', contender, address)
    return Get(ctx, kyc_storage_key)


def vote(ctx, address, contender):
    """."""
    kyc_storage_key = concat('voted_', contender, address)
    cur_vote = Get(ctx, kyc_storage_key)
    Put(ctx, kyc_storage_key, cur_vote + 1)
    print('cur_vote')
    print(cur_vote)
    return True


def Main(operation, args):
    """."""

    # Am I who I say I am?
    user_hash = args[0]
    contender = args[1]
    authorized = CheckWitness(user_hash)
    if not authorized:
        print("Not Authorized")
        return False
    print("Authorized")

    ctx = GetContext()

    if operation == 'vote':
        status = vote(ctx, user_hash, contender)
        print("voted")
        print(status)
        return status

    elif operation == 'checkVote':
        print("Check voted")
        status = check_vote(ctx, user_hash, contender)
        print("status is", status)
        return status
    return False
