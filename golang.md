# golang
# slice

a slice is a *piece* of an array.
length and a pointer to an element of an array

## basic slice definition:

`letters := []string{"a", "b", "c", "d"}`
or

## array definition:

`var buffer [256]byte`

turn it into slice:

```go
var slice []byte = buffer[100:150]
var slice = buffer[100:150]
slice := buffer[100:150]
```

## empty slice

this defines an empty slice that points to an empty array
`temp := []byte{}`
or
`var temp = []byte`

## nil slice

that points to no array yet
`var responseBuffer []string`

you can append to both and go will allocated the underlying array

## nested slices

slice of slices of bytes

`buffer := [][]byte{}`

you shouldn't have `{}` part in the function definition, because that is the slice declaration syntax.

## append

`responseBuffer = append(responseBuffer, responseStr)`

## make

`slice := make([]int, 10, 15)`

make built-in function. It allocates a new array and creates a slice header to
describe it.

## copy

`
newSlice := make([]int, len(slice), 2*cap(slice))
copy(newSlice, slice)
`
`slice[i:]` == `slice[i:len(slice)]`

`slice[:]` all the slice itself.

## compare slices

`if !bytes.Equal(temp, body)`

# strings

Strings are actually very simple: they are slices of bytes that you can't grow them.

# get user's flags

`domain := flag.String("d", "", "target domain")
flag.Parse()`

Domain is of type pointer to a string

and check if it's empty:
`if *domain == ""`

# write to a file

`err := os.WriteFile("testdata/hello", []byte(*domain), 0666)`

`domain` is a pointer to a string.

## write to a file line by line

first write everything line by line to a buffer
`
var buf bytes.Buffer
buf.WriteString(fmt.Sprintf("%d, %v, %v\n", i, formData, resp.Status))
`
then write a buffer to the line
`_ = os.WriteFile("log.txt", buf.Bytes(), 0666)`

# read from a file

```go
file, _ := os.ReadFile("domain.txt")
*domain = string(file)
```

## read a file line by line using `bufio.NewScanner(file`

```go
myFile, _ := os.Open("p/06_read_line_by_line/test.csv") // open the file
scanner := bufio.NewScanner(myFile)                     // takes as input io.Reader interface
   for scanner.Scan() {                                 // moves to the next line by default
      fmt.Printf(scanner.Text())
   }
myFile.Close()
```

## read lines into a buffer

```go
buffer := []string{}
    for _, entry := range readLines("pwd.txt") {
        buffer = append(buffer, fmt.Sprintf("%s", entry))

    }
```

# send post request

## in `username=sth&password=sth` form


```go
formData := url.Values{}
formData.Set("username", "carlos")
formData.Set("password", "password")
```

if you don't encode it, it can't be passed to `strings.NewReader`

```go
req, _ := http.NewRequest("POST", target, strings.NewReader(formData.Encode()))

req.Header.Set("Content-Type", "application/x-www-form-urlencoded")

client := &http.Client{}
resp, _ := client.Do(req)
defer resp.Body.Close()

body, _ := ioutil.ReadAll(resp.Body) //human readable
```

### simpler:

```
resp, err := http.Post("https://example.com/login", "application/x-www-form-urlencoded", reqBody)
```

## body in JSON form

```go
reqBody := map[string]interface{}{
       "username": uname,
       "password": pwd,
   }

   jsonData, _ := json.Marshal(reqBody)

   req, _ := http.NewRequest("POST", target, bytes.NewBuffer(jsonData))
```

and the rest is like the previous one.

## simpler way to add body

```go
formData := "mfa-code=sfdsdf"
req, err := http.NewRequest("POST", url, bytes.NewBufferString(formData))
```

## no redirect

```go
client := &http.Client{
         // no redirect
         CheckRedirect: func(req *http.Request, via []*http.Request) error {
             return http.ErrUseLastResponse
         },
     }
```

or check for redirects and `found` like this:

```go
// Check response for success (e.g., 302 redirect or specific response content)
if resp.StatusCode == http.StatusFound { // 302 Found
	fmt.Printf("2FA successful with code %s\n", codeStr)
	return nil
}
```

## read http response and check if a string exists in it

```go
body, _ := ioutil.ReadAll(resp.Body)

if strings.Contains(string(body), "administrator")
```

## get header

```go
session = resp.Header.Get("Set-Cookie")[:40]
```

# for loop

## range

```go
for _, resp := range buffer {
    if bytes.Equal(resp, body) {
        return true
    }
}
```

# function

```go
func exists(body []byte, buffer [][]byte) bool {}
```
