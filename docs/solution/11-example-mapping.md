# Example Mapping

## Format de restitution
*(rappel, pour chaque US)*

```markdown
## Titre de l'US (post-it jaunes)

> Question (post-it rouge)

### Règle Métier (post-it bleu)

Exemple: (post-it vert)

- [ ] 5 USD + 10 EUR = 17 USD
```

Vous pouvez également joindre une photo du résultat obtenu en utilisant les post-its.

## Story 1: Define Pivot Currency

```gherkin
As a Foreign Exchange Expert
I want to be able to define a Pivot Currency
So that I can express exchange rates based on it
```

## Bank can convert to same currency without exchange rate
Given a bank with pivot currency EUR
    And 10 EUR
When I convert to EUR
Then I get 10 EUR

## Bank can convert to an other currency with exchange rate
Given a bank with pivot currency EUR
    And exchange rate of 1.2 USD
    And 10 EUR
When I convert to USD
Then I get 12 USD

## Bank can convert non pivot currency to pivot currency
Given a bank with pivot currency EUR
    And exchange rate of 1.2 USD
    And 12 USD
When I convert to EUR by dividing the exchange rate
Then I get 10 EUR

## Bank can convert non pivot currency to an other currency with exchange rate
Given a bank with pivot currency EUR
    And exchange rate of 1.2 USD
    And 12 USD
When I convert to EUR by dividing the exchange rate
    And I convert to KRW by multiplying the exchange rate
Then I get 13440 KRW

<!-- ## Story 2: Add an exchange rate
```gherkin
As a Foreign Exchange Expert
I want to add/update exchange rates by specifying: a multiplier rate and a currency
So they can be used to evaluate client portfolios
``` -->

## Story 3: Convert a Money

```gherkin
As a Bank Consumer
I want to convert a given amount in currency into another currency
So it can be used to evaluate client portfolios
```

## Bank can convert non pivot currency to the same
Given a bank with pivot currency EUR
    And 12 KRW
When I convert to KRW by doing nothing
Then I get 12 KRW

## Bank can convert non pivot currency to pivot currency with rounded value
Given a bank with pivot currency EUR
    And exchange rate of 1344 KRW
    And 1 KRW
When I convert to EUR by dividing the exchange rate
    And I round the value at 2 decimals
Then I get 0.00 EUR

## Bank can convert a portfolio with not only pivot currency to an other currency with rounded value
Given a bank with pivot currency EUR
    And exchange rate of 1.2 USD
    And exchange rate of 1344 KRW
    And 12 USD
    And 1700 KRW
    And 50 EUR
When I convert to USD 
    And I convert KRW to EUR by dividing the exchange rate
    And I sum all EUR
    And I convert the sum in USD by multiplying
    And I round the value at 2 decimals
    And I sum all USD
Then I get 73.51 USD

## Story 4: Convert a Money without centime

```gherkin
As a Bank Consumer
I want to convert a given amount in currency into another currency that doesn't have centime (decimal)
So it can be used to evaluate client portfolios
```

## Bank can convert pivot currency to non pivot currency with rounded value
Given a bank with pivot currency EUR
    And exchange rate of 1344 KRW
    And 1.30 EUR
When I convert to EUR by dividing the exchange rate
    And we round the value without decimal
Then I get 1747 KRW

