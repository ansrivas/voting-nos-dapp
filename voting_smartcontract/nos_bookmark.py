from boa.builtins import concat
from boa.interop.Neo.Runtime import CheckWitness, GetTrigger, Log, Serialize, Deserialize
from boa.interop.Neo.Storage import Delete, Get, GetContext, Put
from boa.interop.Neo.TriggerType import Application, Verification

from boa.interop.System.ExecutionEngine import GetCallingScriptHash

DELIMITER = '|'


def Main(operation, args):
    """Main definition of the nOS Bookmark dApp Smart Contract.

    :param operation: str The name of the operation to perform
    :param args: list A list of arguments along with the operation
    :return: bytearray: The result of the operation
    """
    # TODO: Carefully read http://neo-boa.readthedocs.io/en/latest/overview.html#what-parts-of-python-are-supported
    if len(args) == 0:
        Log("Address is required")
        return False

    address_from = args[0]

    # Verify if the address we want to operate from is the invoking address
    is_owner = CheckWitness(address_from)

    if not is_owner:
        Log("Must be owner of the address to operate from")
        return False

    ctx = GetContext()
    ctx_key = get_ctx_key(address_from)

    # Crud operations
    if operation == 'AddBookmark':
        if len(args) < 2:
            Log("Bookmark is required")
            return False
        bookmark = args[1]
        bookmarks = [bookmark]
        Put(ctx, ctx_key, Serialize(bookmarks))
        return True

    if operation == 'GetBookmarks':
        bookmarks = Deserialize(Get(ctx, ctx_key))
        return bookmarks

    if operation == 'SetBookmark':
        if len(args) < 2:
            Log("Bookmark is required")
            return False
        bookmark = args[1]
        bookmarks = [bookmark]
        Put(ctx, ctx_key, Serialize(bookmarks))
        return True

    if operation == 'DeleteBookmark':
        if len(args) < 2:
            Log("Bookmark is required")
            return False
        Delete(ctx, ctx_key)
        return True

    # Share operations
    if operation == 'ShareBookmark':
        return True

    if operation == 'ShareAllBookmarks':
        return True

    if operation == 'ApproveBookmark':
        return True

    if operation == 'RejectBookmark':
        return True

    return False


def get_ctx_key(name):
    """

    :param address: str The name to create the unique context key from
    :return str: The unique context key of the address
    """
    return name
