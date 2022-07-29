# Ajax

Ajax (Asynchronous JavaScript and XML) is a mechanism to allow a website to update (send/recieve) data asynchronously to the backend server without having to reload the entire page ([Flask tutorial][tutorial]). This is a huge utility to allow to contant updates of the website when either new notifications come or new data is available. Another alternative is [websocket][] which is a bit heavier (and requires a tad more setup), but some data indicates its a touch faster. 


below is an example:

```javascript
$.ajax({
    type: "POST", # request type: GET, POST, UPDATE, etc. 
    url: "/search_ingredient", # Endpoint for API
    data: JSON.stringify({ 'query': search_string }), # Data to be sent as json
    contentType: "application/json", # What is being sent
    dataType: 'json', # Data type being sent
    success: function(result) { # What to do if successful
        console.log("Result:");
        console.log(result);
    },
    error: (result) => { # What to do if failure
        console.log("Sadness:");
        console.log(result)
    }
});
```


[tutorial]: https://towardsdatascience.com/using-python-flask-and-ajax-to-pass-information-between-the-client-and-server-90670c64d688 "Flask AJAX tutorial"
[websocket]: https://youtu.be/1BfCnjr_Vjg "Fireship: Websockets"
[wsblog]: https://javascript.info/websocket "Javascript websockets"
