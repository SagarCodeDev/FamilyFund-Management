# birr_assignment
Here is the list of all the urls in the project:
<li>'api/accounts/'</li><br>
      <br>Supports following request
      <ul>GET-To recieve all the accounts</ul>
      <ul>POST-To post the new account</ul><br>
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
      <ul>POST-To post the new expense</ul><br>
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
