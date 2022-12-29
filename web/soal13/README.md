### Portswigger - Lab: Reflected XSS into attribute with angle brackets HTML-encoded

## Description
This lab contains a reflected cross-site scripting vulnerability in the search blog functionality where angle brackets are HTML-encoded. To solve this lab, perform a cross-site scripting attack that injects an attribute and calls the alert function.

## Solution
* send payload to Search box
* "onmouseover="alert(1)
* solver13.py