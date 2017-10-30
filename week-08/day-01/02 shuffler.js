const Panama = {
    cash: 0,
    name: 'Panama',
    tax: '1%',
    deposit: function(amt) {
    }
}

const Cyprus = {
    cash: 0,
    name: 'Cyprus',
    tax: '5%',
    deposit: function(amt) {
    }
}

const Shuffler = {
    cash: 10000,
    transactionCount: 0,
    pick: function() {
        if (this.transactionCount % 2 === 0) {
            let countryName = Panama.name;
            console.log(countryName + " got 1000");
            Panama.cash += 1000;
            this.transactionCount = 1;
        } else if (this.transactionCount % 2 !== 0) {
            let countryName = Cyprus.name;
            console.log(countryName + " got 1000");
            Cyprus.cash += 1000;
            this.transactionCount = 0;
        }
    }
}

Shuffler.pick() // prints Panama got 1000
Shuffler.pick() // prints Cyprus got 1000
Shuffler.pick() // prints Panama got 1000
Shuffler.pick() // prints Cyprus got 1000

console.log( Panama.cash ) // 2000 
console.log( Cyprus.cash ) // 2000 