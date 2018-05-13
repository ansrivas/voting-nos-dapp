# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Initialize module utils."""

from boa.builtins import concat, has_key, keys, list
from boa.interop.Neo.Runtime import CheckWitness, GetTrigger, Log, Serialize, Deserialize
from boa.interop.Neo.Storage import Delete, Get, GetContext, Put
from boa.interop.Neo.TriggerType import Application, Verification

from boa.interop.System.ExecutionEngine import GetCallingScriptHash
from boa.interop.Neo.Storage import Get, Put, Delete, GetContext

REGISTER_KEY = b"contender_"


def contender_register(ctx,  contender):
    """
    :param contenders:list a list of addresses to register
    :param token:Token A token object with your ICO settings
    :return:
        int: The number of addresses to register for KYC
    """
    ok_count = 0
    print("register contender")
    kyc_storage_key = concat(REGISTER_KEY, contender)
    cur_vote = Get(ctx, kyc_storage_key)
    if not cur_vote:
        Log("No contender found")
        Put(ctx, kyc_storage_key, True)
        ok_count += 1
        Log(ok_count)
        return ok_count
    return 1


def check_vote(ctx, contender):
    """
    Looks up the KYC status of an address
    :param address:bytearray The address to lookup
    :param storage:StorageAPI A StorageAPI object for storage interaction
    :return:
        bool: KYC Status of address
    """
    kyc_storage_key = concat(REGISTER_KEY, contender)
    return Get(ctx, kyc_storage_key)


def vote(ctx, contender):
    """."""
    kyc_storage_key = concat(REGISTER_KEY, contender)
    cur_vote = Get(ctx, kyc_storage_key)
    Log('cur_vote')
    if not cur_vote:
        Log("No contender found")
        return False

    if cur_vote is True:
        new_votes = 1
    else:
        new_votes = cur_vote + 1
    Log('new_votes')
    Log(new_votes)
    Put(ctx, kyc_storage_key, new_votes)
    return True


def Main(operation, args):
    """."""

    # Am I who I say I am?
    user_hash = args[0]
    contender = args[1]
    if len(args) == 3:
        return False

    # authorized = CheckWitness(user_hash)
    # if not authorized:
    #     Log("Not Authorized")
    #     return False
    # Log("Authorized")
    ctx = GetContext()

    if operation == 'register':
        count = contender_register(ctx, contender)
        return count
    elif operation == 'vote':
        status = vote(ctx, contender)
        Log("voted")
        Log(status)
        return status

    elif operation == 'checkVote':
        Log("Check voted")
        status = check_vote(ctx, contender)
        Log("status is")
        Log(status)
        return status
    return False
