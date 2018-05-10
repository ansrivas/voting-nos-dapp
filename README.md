# voting-smartcontract

Short Description.


docker exec -it neo-python /bin/bash
ls /custom-smart-contracts/
ls /nos-smart-contract/
ls /smart-contracts


np-prompt -p -v
config sc-events on

open wallet /neo-python/neo-privnet.wallet
password is `coz`

build /custom-smart-contracts/add.py

import contract /custom-smart-contracts/add.avm 0710 02 True False
addContract

Note down the hash of your contract.
Wait for sometime until the contract is deployed. You will see lots of log messages.

testinvoke 0xc05aaad23bd0174962cbbc918c00c22384e86bba add ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y',1,2]
```
[I 180510 00:40:02 EventHub:71] [test_mode][SmartContract.Runtime.Log] [c05aaad23bd0174962cbbc918c00c22384e86bba] [b'Authorized']
[I 180510 00:40:02 EventHub:71] [test_mode][SmartContract.Runtime.Log] [c05aaad23bd0174962cbbc918c00c22384e86bba] [b'add']
[I 180510 00:40:02 EventHub:71] [test_mode][SmartContract.Execution.Success] [c05aaad23bd0174962cbbc918c00c22384e86bba] [3]
Used 0.253 Gas

-------------------------------------------------------------------------------------------------------------------------------------
Test invoke successful
Total operations: 76
Results ['3']
Invoke TX GAS cost: 0.0
Invoke TX fee: 0.0001
```

Now run nos-client
Login using WIF: KxDgvEKzgSBPPfuVfw67oPQBSjidEiqTHURKSDL1R7yGaGYAeYnr


Now run your-app
Edit the smart contract address in your app to the hash what you used above in testinvoke

## License
MIT
