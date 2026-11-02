## API
(Application Programming Interface):- (here interface the layer where  we do the programming)
 API is a set of rules that allows two program to talk to each other.


Ex:- GitHub.com:- it is webpage
api.github.com:- Response:-What is Response:-It is also called endpoint
REST API:-- it gives the response in the form of JSON.
---> client(e.g. customer) sends the HTTP request to the server(e.g. cheif) there is API(waiter) b/w client and server then the server give the response in the JSON format of the request.


--> Request:It consists  basically 4 things:-
1. Method(Action that you want to perform [PUT,PATCH,DELETE,GET])
2. URL(link)
3. Body(you want to update data ,it contains the data)
4. Header(It contains tokens to authentication,what type of content) 


--> According to the request the server sends the respond :-it contains (body [data in json format],  status code:-eg:501,200 )
status code:-GET request the successful response:- 200  , unauthorized:-401  ,POST request the successful response:-201 ,
 Not found(not successfully logedin):-404 ,  Too Many Requests/Rate Limiting:- 429 ,successfully deleted:- 204, forbidden (not alowed to access successfully logedin):-403, Bad Gateway(means error from server side):-502
  ->something started with 2 is success
  ->Something is started 3 is updateing
  ->anything starts with 4 is client error,
  ->something with 5 is server error no issue from client.


# METHODS:-Action that  client want to perform.
GET:- Read/fetch the data from the server 
POST:-Creating a new resource.
PUT:- Used for updating the existing request .It will overwrite it fully  update
PATCH (In 2010):-Used for updating the existing request.It will replace the specific key or the particular value .it is partial update
DELETE:-Delete the resource.
new one 28-June-2026 --> QUERY:- 


pip:- it is used to install library in python
Diference b/w module and library in python: - any file with .py is module, collection of module is called package , collection of mulitplt packages is a library


POSTMAN:- It is a tool used for test the API.

API KEY:- 