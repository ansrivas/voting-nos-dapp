import React from "react";
import injectSheet from "react-jss";
import PropTypes from "prop-types";
import { u, wallet } from '@cityofzion/neon-js';
import { unhexlify } from 'binascii';
import { str2hexstring, int2hex, hexstring2str } from '@cityofzion/neon-js/src/utils'
import { nosPropTypes } from "@nosplatform/api-functions/es6";

import { injectNOS } from "../../nos";

const styles = {
  button: {
    margin: "16px",
    fontSize: "14px"
  }
};

class NOSActions extends React.Component {

  handleGetAddress = async () => alert(await this.props.nos.getAddress());

  handleClaimGas = () =>
    this.props.nos
      .claimGas()
      .then(alert)
      .catch(alert);


  handleGetBalance = async scriptHash => alert(await this.props.nos.getBalance(scriptHash));

  handleTestInvoke = async (scriptHash, operation, arg1, args2) => {
  const output = await this.props.nos.testInvoke(scriptHash, operation, arg1, args2);
  const finalOutput = JSON.stringify(output);

  console.log(finalOutput);
  const valueObj = output.stack[0];
  console.log(unhexlify(valueObj.value));

  }

  handleInvoke = async (scriptHash, operation, args) =>
    alert(await this.props.nos.testInvoke(scriptHash, operation, args));

  handleGetStorage = async (scriptHash, key) =>
    alert(await this.props.nos.getStorage(scriptHash, key));

  render() {
    const { classes } = this.props;

    const scriptHashNeoAuth = "82a2c20627565eac1738e21a6ad9a5bf6d8f1cdd";

    const operation = "register";
    const operationCheckVote = "checkVote";
    const operationVote = "vote";

    const walletAddress ="AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y" ;
    // const addressToScriptHash1 = (address) => u.reverseHex(wallet.getScriptHashFromAddress(address));
    // const addressToScriptHash2 = (address) => u.reverseHex(address);

    // const address1 = addressToScriptHash1(args1);
    // const address2 = addressToScriptHash2(args1);
    // console.log(wallet.getScriptHashFromAddress(walletAddress));
    // console.log(wallet.getScriptHashFromAddress("APBUyZNkemciUQurabSQBnnma7kGGhUPPL"));
    // console.log(u.reverseHex(wallet.getScriptHashFromAddress("APBUyZNkemciUQurabSQBnnma7kGGhUPPL")));
    // console.log(u.str2hexstring(walletAddress));
    // console.log(unhexlify(u.reverseHex(wallet.getScriptHashFromAddress(walletAddress))));

    const args1 = unhexlify(u.reverseHex(wallet.getScriptHashFromAddress(walletAddress)));

    const args2 =  "BO";
    const args3 = "DT";


    return (
      <React.Fragment>
        <button className={classes.button} onClick={this.handleGetAddress}>
          Get Address
        </button>


        <button className={classes.button} onClick={() => this.handleTestInvoke(scriptHashNeoAuth, operationCheckVote, args1, args2)}>
          Check Barack Obama's votes
        </button>
        <button className={classes.button} onClick={() => this.handleTestInvoke(scriptHashNeoAuth, operationVote, args1, args2)}>
          Vote Obama
        </button>

        <button className={classes.button} onClick={() => this.handleTestInvoke(scriptHashNeoAuth, operationCheckVote, args1, args3)}>
          Check Donald Trump's votes
        </button>
        <button className={classes.button} onClick={() => this.handleTestInvoke(scriptHashNeoAuth, operationVote, args1, args3)}>
          Vote Trump
        </button>
        {/*
          <button
            className={classes.button}
            onClick={() => this.handleGetBalance(gas)}
          >
            Get GAS Balance
          </button>
          <button
            className={classes.button}
            onClick={() => this.handleGetBalance(rpx)}
          >
            Get RPX Balance
          </button>
        */}

        <button
          className={classes.button}
          onClick={() =>

            this.handleTestInvoke(scriptHashNeoAuth, operation, args1, args2)
          }
        >
          Register candidate for voting process
        </button>
        {/*
          <button
            className={classes.button}
            onClick={() => this.handleInvoke(scriptHashNeoAuth, operation, args)}
          >
            Invoke (NeoAuth)
          </button>
        */}

      </React.Fragment>
    );
  }
}

NOSActions.propTypes = {
  classes: PropTypes.objectOf(PropTypes.any).isRequired,
  nos: nosPropTypes.isRequired
};

export default injectNOS(injectSheet(styles)(NOSActions));
