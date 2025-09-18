helps you to either get to a vulnerable URL or helpful data:

- Search engine --> URL --> vuln
- Search engine --> URL --> data --> helps to find vuln

# sensitive info

# interesting paths

you will get some paths, that could have functions behind them,
`../certificate/:username/:data`, take note of those, then exclude them to get to other
results by removing the noise.  `-certificate` or `-www` to work on a specific sub.

improve your dorks step by step

- in general if you want to know how unique a path or resource you found is,
  search it in the DOM.

```
site:
inurl:& // URLs with parameters
ext:php | ext:aspx
```
