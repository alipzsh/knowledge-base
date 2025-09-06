# katana

[[crawl]]

Most useful in automation.

- Good for website that the source code is almost similar to the DOM.
- Not suitable for everything, e.g. modern websites, apps written in [react](react); DOM.
- Change it based on configuration, e.g. reduce the thread if WAF/CDN.

# JavaScript

A JS code to run in the console and get URls after loading the DOM.
Consider each result; search for it in inspect, then read the related code.

```js
javascript:(function(){var s=document.getElementsByTagName("script"),r=/(?<=(\"|'|`))[a-zA-Z0-9_?=\/\-\#\.\!]*(?=(\"|'|`))/g,n=new Set;for(var i=0;i<s.length;i++){var t=s[i].src;t&&fetch(t).then(e=>e.text()).then(e=>{for(let o of e.matchAll(r))n.add(o[0])}).catch(e=>console.log("Error:",e))}var p=document.documentElement.outerHTML;for(const m of p.matchAll(r))n.add(m[0]);function w(){n.forEach(e=>document.write(e+"<br>"))}setTimeout(w,3e3)})();
```
