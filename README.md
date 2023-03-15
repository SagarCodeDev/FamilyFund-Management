# birr_assignment
# Database used: MYSQL
# Here is the list of all the urls in the project:
<li>'api/accounts/'</li><br>
      <br>Supports following request
      <ul>GET-To recieve all the accounts</ul>
      <ul>POST-To post the new account
      <br>Test Case:<br>
      <ul>{
    "Account":{
        "family_fundname":"Sheoran Family",
        "family_fund":0,
        "goal_amount":1000000,
        "saved_money":0
    },
    "User":[{
        "username":"Sagar",
        "email":"sagarsheoran79@gmail.com",
        "number":"7727839857",
        "relation":"Child",
        "percentage":0.7,
        "salary":10000
    },
    {
        "username":"SagarDad",
        "email":"sagardad@gmail.com",
        "number":"7727839857",
        "relation":"Father",
        "percentage":0.7,
        "salary":100000
    },
    {
        "username":"SagarMom",
        "email":"sagarmom@gmail.com",
        "number":"7727839857",
        "relation":"Mother",
        "percentage":0.7,
        "salary":100000
    },
    {
        "username":"SagarGrandF",
        "email":"sagarGrandF@gmail.com",
        "number":"7727839857",
        "relation":"Grandfather",
        "percentage":0.7,
        "salary":50000
    },
    {
        "username":"SagarGrandM",
        "email":"sagarGrandM@gmail.com",
        "number":"7727839857",
        "relation":"Grandmother",
        "percentage":0.7,
        "salary":50000
    }]
            }</ul>
      </ul>
      <ul>JSON Payload-</ul>
      <ul>Account-Info regarding the account model</ul>
      <ul>User-All users associated with that account</ul>
<li>'api/accounts/{id}'</li> <br>
      <br>Supports following request
      <ul>GET-To recieve the account specified</ul>
      <ul>PATCH-To update the specified account info</ul><br>
      <ul>JSON Payload-</ul>
      <ul>Changes in the account model</ul>
      <ul>DELETE-To delete the specified account</ul>
<li>'api/expense/'</li>
<br>Supports following request
      <ul>GET-To recieve all the expenses</ul>
      <ul>POST-To post the new expense
      <br>Test Case:</br>
       {
    "expense":{
        "amount":15000,
        "date":"2023-01-01",
        "account":2
    },
    "type":"family"
}     </ul>
      <ul>JSON Payload-</ul>
      <ul>Expense-Info regarding the expense model</ul>
      <ul>Type- Type of the expense('personal' or 'family')</ul>
<li>'api/expense/{id}'</li>
      <br>Supports following request
      <ul>GET-To recieve the specified expense</ul>
      <ul>PATCH-To update the specified expense info</ul><br>
      <ul>JSON Payload-</ul>
      <ul>Changes in the expense model</ul>
      <ul>DELETE-To delete the specified expense</ul><br>
<li>'api/billing/'</li>
<br>Supports following request
      <ul>GET-To recieve all the billings</ul>
      <ul>POST-To post the new billing</ul><br>
      <ul>JSON Payload-</ul>
      <ul>Billing-Info regarding the billing model</ul>
<li>'api/billing/{id}'</li>
<br>Supports following request
      <ul>GET-To recieve the specified billing</ul>
      <ul>PATCH-To update the specified billing info</ul><br>
      <ul>JSON Payload-</ul>
      <ul>Changes in the billing model</ul>
      <ul>DELETE-To delete the specified billing</ul><br>
<li>'api/users/'</li>
<br>Supports following request
      <ul>GET-To recieve all the users</ul>
      <ul>POST-To post the new users</ul><br>
      <ul>JSON Payload-</ul>
      <ul>Info regarding the users model</ul>
<li>'api/users/{id}'</li>
<br>Supports following request
      <ul>GET-To recieve the specified users</ul>
      <ul>PATCH-To update the specified users info</ul><br>
      <ul>JSON Payload-</ul>
      <ul>Changes in the users model</ul>
      <ul>DELETE-To delete the specified users</ul><br>
<li>'api/monthchange/'</li>
<br>Supports following request
      <ul>GET- This API is just for presentation purpose. It is to signify that month is changed so that all the financial info of all the models can be updated.</ul>
<li>'api/users/expense/{id}/'</li>
<br>Supports following request
      <ul>GET-To check how much a particular user can spend more</ul>
<li>'api/accounts/goalamount/{id}'</li>
<br>Supports following request
      <ul>GET- To check how much more money is needed for goal amount</ul>
