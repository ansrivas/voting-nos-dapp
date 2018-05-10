# custom-smartcontract-dApp

## Pre-requisites:

1. python installed in your system
2. `docker-compose` installed. `pip install -U docker-compose`
3. Edit your `/etc/hosts` file and append this line `127.0.0.1   neo-nodes`

## Steps to create a simple dApp using nOS.

1. In case you need to remove previously running containers:
  `docker rm -f neo-scan neo-nodes db neo-python`

2. `docker exec -it neo-python /bin/bash`

3. At this point, you are inside neo-python container. Few of the volumes inside docker are already mapped to your local disk. If you execute following, you will the following three directories. In case you need to add a new contract, you will add it in custom-smart-contracts directory locally on your disk and it will appear in the docker-container. If you run `ls` at this point:

    ```sh
    root@your-pc:/neo-python# ls
    CHANGELOG.rst  MANIFEST.in  README.rst  docs      fixtures  neo-privnet.sample.wallet  neo_python.egg-info  requirements.txt       setup.cfg
    LICENSE.md     Makefile     docker      examples  neo       neo-privnet.wallet         readthedocs.yml      requirements_docs.txt  setup.py

    root@your-pc:/neo-python# ls /custom-smart-contracts/
    __init__.py  add.py  compile.py

    root@your-pc:/neo-python# ls /nos-smart-contract/
    README.md  contract.py

    root@your-pc:/neo-python# ls /smart-contracts
    wake_up_neo.py

    ```

4. While you are inside your docker-container, execute the following to enter the neo-python-prompt:

    ```root@your-pc:/neo-python# np-prompt -p -v```

5. Enable the smart-contract events:

    ```neo> config sc-events on```

6. Open the default wallet with all the Neo and Gas in it. **Default password is `coz`**

    ```neo> open wallet /neo-python/neo-privnet.wallet```

7. Build your first simple smart contract to add two numbers:

    ```
    neo> build /custom-smart-contracts/add.py

    [I 180510 11:14:28 BuildNRun:48] Saved output to /custom-smart-contracts/add.avm
    ```

8. Now you need to import this contract. This deploys this smart-contract in your privatenet.

  * Here you will notice that your smart contract accepts `07=String` and `10=Array` as input and return `02=Integer` as output.
  * `True` is to say that you will `testinvoke` your smartcontract.

    ```neo> import contract /custom-smart-contracts/add.avm 0710 02 True False```

9. Once you will import this contract, give it some useful name like `addContract`. You can skip the rest by pressing <kbd>enter</kbd> key.

    ```
    Please fill out the following contract details:
    [Contract Name] > addContract
    ```

10. Immediately after this step you will get a contract hash which will uniquely identify your smart-contract. Take a note of it and write it down somewhere to be used later. **Notice the last line below**

    ```
    Please fill out the following contract details:
  [Contract Name] > addContract
  [Contract Version] >
  [Contract Author] >
  [Contract Email] >
  [Contract Description] >
  Creating smart contract....
                   Name: addContract
                Version:
                 Author:  
                  Email:  
            Description:  
          Needs Storage: True
   Needs Dynamic Invoke: False
  {
      "hash": "0xc05aaad23bd0174962cbbc918c00c22384e86bba",
      ```
**Note down the hash of your contract.
Wait for sometime until the contract is deployed. You will see lots of log messages.**

11. Its time to test the deployed smartcontract. **Don't forget to change the smartcontract in the line below.**

    ```
    neo> testinvoke <your_smartcontract_hash> add ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y',1,2]

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

12. **Running your dApp**.

    In the root level of the project you will find `contract-frontend`.

    ```
    cd contract-frontend
    ```
    Edit the file `src/components/NOSActions/index.jsx`. Look for line number 52:

    `const scriptHashNeoAuth= your_smartcontract_hash`. Change this to your smartcontract hash which you have noted down earlier in **step 10**.

    Now run your-app. The server will run at **http://localhost:1234**
    ```
    yarn && yarn start
    Server running at http://localhost:1234
    ```

13. **Running your nos-client**.

    In another terminal run the following commands. This will launch your nos-client-browser locally.

    Login using WIF key: `KxDgvEKzgSBPPfuVfw67oPQBSjidEiqTHURKSDL1R7yGaGYAeYnr`

    ```
    git clone https://github.com/nos/client nos-client
    cd nos-client
    yarn && yarn start
    ```

14. At this point you have your **smart contract deployed**, **nos-client-browser running** and your **dApp running** on http://localhost:1234

15. Finally in the nos-client, in the url bar, write `localhost:1234`. You will see your dApp there.

16. Happy hacking !!


## License
MIT
