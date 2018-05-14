# custom-smartcontract-dApp

## Pre-requisites:

1. python installed in your system
2. `docker-compose` installed. `pip install -U docker-compose`
3. Edit your `/etc/hosts` file and append this line `127.0.0.1   neo-nodes`
4. `pip install -U neo-boa neo-python`

## Steps to create a simple dApp using nOS.

1. In case you need to remove previously running containers:
  `docker rm -f neo-scan neo-nodes db neo-python`

2. First step is to clone this repository and execute `python auto_create.py`

    ```
    $ git clone git@gitlab.com:ansrivas/voting-nos-dapp.git

    $ cd voting-nos-dapp

    $ python auto_create.py
    ```

    Check if all the containers are up and running:

    ```
    $ docker ps

      CONTAINER ID        IMAGE                       COMMAND                  CREATED             STATUS              PORTS                                                                        NAMES
    404409289bd2        cityofzion/neo-python       "/bin/sh -c /bin/bash"   4 hours ago         Up 4 hours                                                                                       neo-python
    984a81fe1386        neolocal_neo-scan           "/bin/sh -c 'sleep 3…"   4 hours ago         Up 4 hours          0.0.0.0:4000->4000/tcp                                                       neo-scan
    01d654c3062e        cityofzion/neo-privatenet   "/bin/bash /opt/run.…"   4 hours ago         Up 4 hours          0.0.0.0:20333-20336->20333-20336/tcp, 0.0.0.0:30333-30336->30333-30336/tcp   neo-nodes
    992b85b86e67        postgres:10.1               "docker-entrypoint.s…"   4 hours ago         Up 4 hours          5432/tcp                                                                     db

    ```

4. Now login inside your running neo-python container:

    `docker exec -it neo-python /bin/bash`

5. At this point, you are inside neo-python container. Few of the volumes inside docker are already mapped to your local disk. If you execute following, you will the following three directories. In case you need to add a new contract, you will add it in custom-smart-contracts directory locally on your disk and it will appear in the docker-container. If you run `ls` at this point:

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

6. While you are inside your docker-container, execute the following to enter the neo-python-prompt:

    ```root@your-pc:/neo-python# np-prompt -p -v```

7. Enable the smart-contract events:

    ```neo> config sc-events on```

8. Open the default wallet with all the Neo and Gas in it. **Default password is `coz`**

    ```neo> open wallet /neo-python/neo-privnet.wallet```

9. Build your first simple smart contract to add two numbers:

    ```
    neo> build /custom-smart-contracts/voting.py

    [I 180510 11:14:28 BuildNRun:48] Saved output to /custom-smart-contracts/voting.avm
    ```

10. Now you need to import this contract. This deploys this smart-contract in your privatenet. Here you will notice that your smart contract accepts `07=String` and `10=Array` as input and return `02=Integer` as output. `True` is to say that you will `testinvoke` your smartcontract.

    ```
    neo> import contract /custom-smart-contracts/voting.avm 0710 05 True False
    ```

11. Once you will import this contract, give it some useful name like `voting1`. You can skip the rest by pressing <kbd>enter</kbd> key.

    ```
    Please fill out the following contract details:
    [Contract Name] > voting1
    ```

12. Immediately after this step you will get a contract hash which will uniquely identify your smart-contract. Take a note of it and write it down somewhere to be used later. **Notice the last line below**

    ```
    Please fill out the following contract details:
  [Contract Name] > voting1
  [Contract Version] >
  [Contract Author] >
  [Contract Email] >
  [Contract Description] >
  Creating smart contract....
                   Name: voting1
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

13. Its time to test the deployed smartcontract. **Don't forget to change the smartcontract in the line below.**

    ```
    neo> testinvoke <your_smartcontract_hash> register ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y','BO']
    [I 180514 23:00:44 EventHub:71] [test_mode][SmartContract.Runtime.Log] [17adc98d0c3981f1146600ace57b107181a8c417] [b'register contender']
    [I 180514 23:00:44 EventHub:71] [test_mode][SmartContract.Storage.Get] [17adc98d0c3981f1146600ace57b107181a8c417] ["b'contender_BO' -> bytearray(b'')"]
    [I 180514 23:00:44 EventHub:71] [test_mode][SmartContract.Runtime.Log] [17adc98d0c3981f1146600ace57b107181a8c417] [b'No contender found']
    [I 180514 23:00:44 EventHub:71] [test_mode][SmartContract.Storage.Put] [17adc98d0c3981f1146600ace57b107181a8c417] ["b'contender_BO' -> bytearray(b'\\x01')"]
    [I 180514 23:00:44 EventHub:71] [test_mode][SmartContract.Runtime.Log] [17adc98d0c3981f1146600ace57b107181a8c417] [b'\x01']
    [I 180514 23:00:44 EventHub:71] [test_mode][SmartContract.Execution.Success] [17adc98d0c3981f1146600ace57b107181a8c417] [1]
    Used 1.212 Gas

    -------------------------------------------------------------------------------------------------------------------------------------
    Test invoke successful
    Total operations: 172
    Results ['1']
    Invoke TX GAS cost: 0.0
    Invoke TX fee: 0.0001

    ```

14. **Running your dApp**.

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

15. **Running your nos-client**.

    In another terminal run the following commands. This will launch your nos-client-browser locally.

    Login using WIF key: `KxDgvEKzgSBPPfuVfw67oPQBSjidEiqTHURKSDL1R7yGaGYAeYnr`

    ```
    git clone https://github.com/nos/client nos-client
    cd nos-client
    yarn && yarn start
    ```
16. Now you can register your app in nos with a domain name of your choice. Go back to neo-python prompt, as in step.4.
Build the smartContract provided by default, import it and wait for the contract to be deployed.

    ```
    build /nos-smart-contract/contract.py
    import contract /nos-smart-contract/contract.avm 0710 05 True False

    testinvoke 0xe60a3fa8149a853eb4dff4f6ed93c931646a9e22 RegisterDomain ['AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y', 'voting.neo', 'AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y', 'http://localhost:1234']```

16. At this point you have your **smart contract deployed**, **nos-client-browser running** and your **dApp running** on http://localhost:1234

17. Finally in the nos-client, in the url bar, write `localhost:1234`. You will see your dApp there.

18. Happy hacking !!
 
## License
MIT
