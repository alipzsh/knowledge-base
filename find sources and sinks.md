EX1:
source -> token         (input)
sink   -> xhr request   (apply/use)

EX2:
source -> username
sink   -> print in HTML

1. search the parameter in the devtools
2. go through every result
3. add a breakpoint if the parameter's value is:
  - being `get` e.g. `get("redirect_url")`
  - we are looking for places in the code that the parameter is being explicitly
    `get`
    ==> if there is a `sink` around without the parameter being `get` this is
    not what we are looking for (source).
    e.g.
    ```js
    window.location.href = (0, s.C)("".concat(location.origin, "/signup?redirect_url=").concat(O), null, 
    ```
  - being passed to an interesting variable (e.g. q): `tA = "redirect_url"`

4. reload
5. find where the parameter is passed to a sink

  Q1: is where the breakpoint stopped the source we want?
    - not necessarily
      our input could be retrieved by multiple sources, but only one of them
      passes it to a sink:

      input -> 10 sources -> 1 sink (at this point we know this exists, we
      should only find it)

  --> continue the debugger
  1. notice the repetitions (getting stopped by the same breakpoints multiple
     times)
  2. guess the sink, notice:
    - what is happening in the app (e.g redirection)
    - what is expected to be in the code to do that (e.g `windowlocation.href`)
    - if the function happens immediately after a breakpoint that could be it.

  - read the code and infer if its what we are looking for.
  3. if you are only in couple of files, you could find it by searching the
     possible sinks and breakpointing them.
     --> if not, repeat 3 for other possible sinks

# attention

- repetitions could be due to the need to get user's input and doing in in
  intervals.
- while doing these, remove the unnecessary overhead:
    e.g. if you are not in the `forgetpass` path, but you had a breakpoint in
    a related function, remove it.
    e.g if you put a breakpoint in file but that doesn't stop you, close the
    file.
- at any point of this (and other similar stuff) you might find other info
  (e.g. links) that aren't related to finding sinks but have high values in term
  of reconnaissance.
- use [[devtools]] 
