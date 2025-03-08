
flask route definition:

```python
@app.route("/package", methods=["GET"])
@app.route("/package/<path:path>", methods=["GET"])
```
it only responds to the requests that start with `/package` or `/package/path`:
`curl "http://challenge.localhost:80/package/index.html"`