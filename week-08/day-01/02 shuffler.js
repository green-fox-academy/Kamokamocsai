'use strict';

const Panama = {
    cash: 0,
    name: 'Panama',
    tax: '1%',
    deposit: function(amt) {
        this.cash += amt;        
    }
}

const Cyprus = {
    cash: 0,
    name: 'Cyprus',
    tax: '5%',
    deposit: function(amt) {
        this.cash += amt;
    }
}

const Shuffler = {
    cash: 10000,
    transactionCount: 0,
    pick: function() {
        let countryName = '';
        if (this.transactionCount % 2 === 0) {
            countryName = Panama;
        } else {
            countryName = Cyprus;
        }
        countryName.deposit(1000);            
        console.log(countryName.name + " got 1000");
        this.transactionCount += 1;
    }
}

Shuffler.pick() // prints Panama got 1000
Shuffler.pick() // prints Cyprus got 1000
Shuffler.pick() // prints Panama got 1000
Shuffler.pick() // prints Cyprus got 1000

console.log( Panama.cash ) // 2000 
console.log( Cyprus.cash ) // 2000 