# Pull the latest images from Docker hub
docker pull cityofzion/neo-python
docker pull cityofzion/neo-privatenet

# Start the private network container. Maps the current working directory on the host into
# `/neo-python/sc/` and exposes the ports.
docker run --rm -d --name neo-privatenet -p 20333-20336:20333-20336/tcp -p 30333-30336:30333-30336/tcp cityofzion/neo-privatenet

# Start the neo-python container
docker run --rm -it --net=host -v $(pwd):/neo-python/sc -h neo-python --name neo-python cityofzion/neo-python /bin/bash


docker exec -it neo-python /bin/bash


# Start neo-python
np-prompt -p -v
config sc-events on

create wallet /path/to/wallet

open wallet /neo-python/neo-privnet.wallet


/neo-python/sc/voting_smartcontract
/smart-contracts/voting_smartcontract/neosense.py


/neo-python

CHANGELOG.rst  MANIFEST.in  README.rst  docs      fixtures  neo-privnet.sample.wallet  neo_python.egg-info  requirements.txt       sc         setup.py
LICENSE.md     Makefile     docker      examples  neo       neo-privnet.wallet         readthedocs.yml      requirements_docs.txt  setup.cfg

import contract /neo-python/sc/voting_smartcontract/neosense.avm 0710 05 True False

0xc05aaad23bd0174962cbbc918c00c22384e86bba= smart contract
AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y = address
031a6c6fbbdf02ca351745fa86b9ba5a9452d785ac4f7fc2b7548ca2a46c4fcf4a = pubkey

contract 0xc05aaad23bd0174962cbbc918c00c22384e86bba

build /neo-python/sc/voting_smartcontract/neosense.py
import contract /neo-python/sc/voting_smartcontract/neosense.avm


testinvoke 0xc05aaad23bd0174962cbbc918c00c22384e86bba RegisterProduct ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y','InternetExplorer']

testinvoke 0xc05aaad23bd0174962cbbc918c00c22384e86bba LicenseProduct ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y','InternetExplorer']

testinvoke 0xc05aaad23bd0174962cbbc918c00c22384e86bba GetLicense ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y','InternetExplorer','AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y']
testinvoke 0xc05aaad23bd0174962cbbc918c00c22384e86bba GetLicense ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y','InternetExplorer','Ac82Sr7nrVMt5iCHYmKVn1fEt85XVfn9wZ']

----

testinvoke 0xc05aaad23bd0174962cbbc918c00c22384e86bba add ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y',1,2]
----


another-wallet:Ac82Sr7nrVMt5iCHYmKVn1fEt85XVfn9wZ
pubkey: 021f3197f9ab65c9d649e01ff11aa6741a7765a5e90a49eba6a536382edd836a69


docker exec -it neo-python np-prompt -p -v

Original wallet

WIF key: KxDgvEKzgSBPPfuVfw67oPQBSjidEiqTHURKSDL1R7yGaGYAeYnr
Address: AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y
Script hash (for use with CheckWitness): b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9'



Signature00,Boolean01,Integer02,Hash16003,Hash25604,ByteArray05,PublicKey06,String07,Array10,InteropInterfacef0,Void f
