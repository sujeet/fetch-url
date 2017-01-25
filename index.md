fetch-url
=========

A nifty URL fetcher returning source in JSONP.

Example
-------
```javascript
function myCallback (json) {
    var page_source = json.source;
    // do stuff with page source here.
}

var url = "http://google.com";

$.ajax({
  url: "http://fetch-url.appspot.com"
               + "?url=" + url
               + "&funcname=myCallback",
  dataType: "jsonp"
});
```
