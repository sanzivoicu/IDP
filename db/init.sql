CREATE DATABASE ATM;
use ATM;

CREATE TABLE Users(
    firstName VARCHAR(20),
    lastName VARCHAR(20),
    secretPassword VARCHAR(20),
    cardNumber INTEGER(20),
    pin INTEGER(5),
    amount INTEGER(10)
);

CREATE TABLE History(
    cardNumber VARCHAR(20),
    transactionType VARCHAR(20),
    transactionDate DATE
);
