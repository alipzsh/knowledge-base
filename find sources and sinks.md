DOM source -> redirect_url // takes value from URL
DOM sink   -> redirect     // does some action

1. search the parameter in the devtools
2. go through every result
3. add a breakpoint if the parameter's value is:
  - being `get` (it's not 100% from the URL)
  - being passed to an interesting variable (e.g. q)
4. reload
5. find where the parameter is passed to a sink
  multiple times one parameter could be used, but not all are source.

  - notice of other variables in the same function, if they aren't related, remove the
    breakpoint

    e.g if there is something related to forget pass but you aren't in that path.

  - guess the sink, notice:
    - what is happening in the app (e.g redirection)
    - what is expected to be in the code to do that (e.g `windowlocation.href`)
    - what you see immediately after the source, it could be the possible sink.
  - notice where the repetition is happening, it could be that.
  - read the code and infer if its what we are looking for.
  - read the files that aren't in the game
  - at the end if you are only in couple of files, you could find it by searching the
    possible sink.
  - if not, repeat the process for other possible sinks.
6. put a breakpoint on the possible sink and observe

