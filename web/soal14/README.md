# Portswigger - Lab: Stored XSS into anchor href attribute with double quotes HTML-encoded

## Description
This lab contains a stored cross-site scripting vulnerability in the comment functionality. To solve this lab, submit a comment that calls the alert function when the comment author name is clicked.

## Solution
* post comment and send payload in url
* payload
```javascript
javascript:alert(1)
```

