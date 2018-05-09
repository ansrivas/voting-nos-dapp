import React from "react";
import injectSheet from "react-jss";
import PropTypes from "prop-types";
import { u, wallet } from '@cityofzion/neon-js'
import { unhexlify } from 'binascii'
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

  handleTestInvoke = async (scriptHash, operation, args) => {
    alert(await this.props.nos.testInvoke(scriptHash, operation, args));
  }

  handleInvoke = async (scriptHash, operation, args) =>
    alert(await this.props.nos.testInvoke(scriptHash, operation, args));

  handleGetStorage = async (scriptHash, key) =>
    alert(await this.props.nos.getStorage(scriptHash, key));

  render() {
    const { classes } = this.props;

    // Get Balance
    const neo = "c56f33fc6ecfcd0c225c4ab356fee59390af8560be0e930faebe74a6daff7c9b";
    // const gas = "602c79718b16e442de58778e148d0b1084e3b2dffd5de6b7b16cee7969282de7";
    // const rpx = "ecc6b20d3ccac1ee9ef109af5a7cdb85706b1df9";
    // (test) Invoke
    // const addressToScriptHash = (address) => u.reverseHex(wallet.getScriptHashFromAddress(address));
    // const scriptHashNeoAuth = addressToScriptHash("AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y");

    // A simple contract to add two numbers
    const scriptHashNeoAuth = "0xc05aaad23bd0174962cbbc918c00c22384e86bba";
    const operation = "add";
    const args = ["AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y", u.int2hex(1), u.int2hex(2)];

    // console.log(addressToScriptHash("AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y"));
    // Get Storage
    // const scriptHashNeoBlog = "85e9cc1f18fcebf9eb8211a128807e38d094542a";
    // const key = "post.latest";

    return (
      <React.Fragment>
        <button className={classes.button} onClick={this.handleGetAddress}>
          Get Address
        </button>
        <button className={classes.button} onClick={() => this.handleGetBalance(neo)}>
          Get NEO Balance
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
        <button className={classes.button} onClick={this.handleClaimGas}>
          Claim Gas
        </button>
        <button
          className={classes.button}
          onClick={() =>

            this.handleTestInvoke(scriptHashNeoAuth, operation, args)
          }
        >
          TestInvoke (NeoAuth)
        </button>
        {/*
          <button
            className={classes.button}
            onClick={() => this.handleInvoke(scriptHashNeoAuth, operation, args)}
          >
            Invoke (NeoAuth)
          </button>
        */}
        <button
          className={classes.button}
          onClick={() => this.handleGetStorage(scriptHashNeoBlog, key)}
        >
          GetStorage (NeoBlog)
        </button>
      </React.Fragment>
    );
  }
}

NOSActions.propTypes = {
  classes: PropTypes.objectOf(PropTypes.any).isRequired,
  nos: nosPropTypes.isRequired
};

export default injectNOS(injectSheet(styles)(NOSActions));
