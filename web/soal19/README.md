# Portswigger - 

## Description

## Solution
* post a comment
* observe the script js process that data 
* resources/js/loadCommentsWithVulnerableEscapeHtml.js
* send payload:
```javascript
<><img src=1 onerror=alert(1)>
```