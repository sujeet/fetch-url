fetch-url
=========

A Google App Engine app that fetches a given URL and
returns the contents in plaintext. Can be used as a proxy
for static content on third-party websites that can not
be queried through JavaScript because those third-party
websites do not have CORS enabled.

Example
-------
```javascript
function wget(url) {
  var request = new XMLHttpRequest();
  var fetcherApp = 'https://fetch-url.appspot.com';
  request.open('GET',
               fetcherApp + '?url=' + url,
               async=false);
  request.send(data=null);
  if (request.status == 200) {
    return request.responseText;
  }
  throw new Error('wget ' + 
                  url + 
                  ' returned status: ' + 
                  request.status);
}

var url = 'https://sujeet.github.io';

console.log(wget(url));
```
