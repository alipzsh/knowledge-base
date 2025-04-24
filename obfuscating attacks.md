The exact sequence of decoding steps that are performed depends on the context
in which the data appears.

- a query parameter is typically URL decoded server-side
- the text content of an HTML element may be HTML decoded client-side.

you should figure out how your payload is being decoded to find alternative representations of the same payload.

blocking injection payloads are easy because they contain user supplied code,
which doesn't exist in the regular code.

Filters must decode input the same way the backend does. If not, attackers can bypass them using alternate encodings.