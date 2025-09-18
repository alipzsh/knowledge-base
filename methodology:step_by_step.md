1. passive recon (vulnerable URLs or useful data)
  1. waybackurls
  2. gau
  3. google dork        =>  interesting urls
                        => maybe do it at first to get familiar with the
                        application
  5. archive wayback

2. find interesting URLs
  - browse the website for interesting links
  - while dorking
  - passive/active recon (scriptted)
    - look manually
    - unfurl -> look for interesting params manually -> search for that URL
4. URL
  - look for parameters
   (search for them in DOM to see how out of reach they are)
   - how is the parameter handled?
     - http -> reflection
     - JS   -> DOM
        - let it go when you can't modify the input (it's out of my league even
          if possible.)

# what makes a URL interesting?

- not reachable through DOM.
- has parameters -> work on those parameters
