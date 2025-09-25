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
3. URL
  - look for parameters
   (search for them in DOM to see how out of reach they are)
  - different parameters would be effective in different situations
    --> breakpoint and observer in loop
    --> if it doesn't break, it means we are not there.
   - how is the parameter handled?
     - http -> reflection
     - JS   -> DOM
        - let it go when you can't modify the input (it's out of my league even
          if possible.)
    * an http redirection doesn't give you XSS but JS one does
4. login/register/forgetpassword
   - look for the parameters that are effective for the whole process
     - js   -> DOM
     - http -> reflections
   - notice the request bodies
6. [threat modelling](threat modeling)

- go through the whole process, observer the parameters added, remain along the
  way
7. map the workflows

determine the order of functionalities:
e.g checker functions and functions to interact with the servers

- what are the type of the [ratelimitation](ratelimit.md)


# attention

- custom features are more interesting because they aren't common/tested
  everywhere.


# what makes a URL interesting?

- not reachable through DOM.
- has parameters -> work on those parameters
