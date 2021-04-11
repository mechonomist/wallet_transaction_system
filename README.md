# Wallet System
A web application where users can create and maintain their online wallets.

## Tech Stack 
* Django
* Postgres

## Setup 

### Development

#### Prerequisites
* Install Docker

#### Cloning repository and setting up the project
* Here are the steps to clone the repository
    * Clone the repository
        * Using HTTPS:
            Click on the clone button on the repository home page and copy the provided link
            Run the following command in terminal: `git clone https://github.com/mechonomist/wallet_transaction_system.git`

* Here are the steps to setup the project in local environment:
    * Navigate to the working directory `cd wallet_transaction_system`
    * Configure all the environment variables as mentioned in `wallet_system/.env_sample` file in `wallet_system/.env file`.
    * Run `docker-compose up --build`
    * The above command will build the docker images for both Django App and Postgres Database and it will start both the containers.
    
#### API Endpoints

**Create Wallet**
----
Creates a wallet for a user
* **URL**<br /> 
  /wallet/

* **Method:**<br /> 
`POST`
  
*  **URL Params**<br /> 
   **Required:** None

* **Data Params**

  **Required:**<br /> 
   `wallet_id=email[str]` <br />
   `current_balance=[float]`

* **Success Response:**
  * **Code:** 201 <br />
    **Content:** `{"message": "A new wallet account with email: abc@example.com has been created"}`
 
* **Error Response:**

  * **Code:** 400 NOT FOUND <br />
    **Content:** `{ "message" : "Deposited amount below minimum balance requirements" }`


**Credit money to wallet**
----
  Credits money to a user's wallet

* **URL**<br /> 
  /wallet/

* **Method:**<br /> 
`PUT`
  
*  **URL Params**<br /> 
   **Required:** None

* **Data Params**

  **Required:**<br /> 
   `email=[str]` <br />
   `transaction_type=[str]`<br />
   `transaction_amount=[float]`

* **Success Response:**
  * **Code:** 200 OK <br />
    **Content:** `{ "message" : "Amount Credited, current available balance is 110.0`
 
* **Error Response:**
  * **Code:** 500 INTERNAL SERVER ERROR <br />
    **Content:** `{ "message" : "Unknown error has occurred}` <br />
   
   OR
  * **Code:** 400 BAD REQUEST<br />
    **Content:** `{ "message" : "Transaction type:abc is not valid}` <br />

**Debit money to wallet**
----
  Debits money from a user's wallet

* **URL**<br /> 
  /wallet/

* **Method:**<br /> 
`PUT`
  
*  **URL Params**<br /> 
   **Required:** None

* **Data Params**

  **Required:**<br /> 
   `email=[str]` <br />
   `transaction_type=[str]`<br />
   `transaction_amount=[float]`

* **Success Response:**
  * **Code:** 200 OK <br />
    **Content:** `{ "message" : "Amount Debited, current available balance is 110.0`
 
* **Error Response:**
  * **Code:** 400 BAD REQUEST <br />
    **Content:** `{ "message" : "Available wallet balance does not support transaction}` <br />
   
   OR
  * **Code:** 500 INTERNAL SERVER ERROR <br />
    **Content:** `{ "message" : "Unknown error has occurred}` <br />
   
   OR
  * **Code:** 400 BAD REQUEST<br />
    **Content:** `{ "message" : "Transaction type:abc is not valid}` <br />

**Get current balance**
----
Returns JSON data with current balance of a wallet
* **URL**<br /> 
  /wallet/:email

* **Method:**<br /> 
`GET`
  
*  **URL Params**<br /> 
   **Required:**<br />
   `email=[str]` <br />

* **Data Params**

  **Required:**<br /> 
None

* **Success Response:**
  * **Code:** 200 OK <br />
    **Content:** `{"email" : abc@example.com, "current_balance": 110.0}`
 
* **Error Response:**

  * **Code:** 400 NOT FOUND <br />
    **Content:** `{ "message" : "Deposited amount below minimum balance requirements" }`
