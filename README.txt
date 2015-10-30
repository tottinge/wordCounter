This code is to help prove or disprove a theory.

In OO, the code you write should be a kind of DSL that helps you solve your problems.
If we count all the terms in your code base (splitting camelcase, in case you use
such a convention) then your domain terms should be some of the most-used terms, 
where as primitive types and operations should appear far lower on the list.


In an accounting system, we would expect "account" and "ledger" and "transaction"
and "debit" and "credit" to be highly common, more common than mere technical 
terms like "if" and "int" and "for"

So here is a tool to try to count your terms. It's silly. It's simple, but let's see
where it takes us.

