# ruby
In the case of Ruby, the terms marshalling and unmarshalling are used to serialize and
deserialize.

```ruby
>> Marshal.dump(p)
=> "\x04\bo:\vPerson\x06:\n@nameI\"\x10Luke Jahnke\x06:\x06ET"

>> Marshal.load("\x04\bo:\vPerson\x06:\n@nameI\"\x10Luke Jahnke\x06:\x06ET")
=> #<Person:0x00005584ba995dd8 @name="Luke Jahnke">
```


if a standard library `require`s another, it will be loaded too.

```ruby
module Gem
...
  def self.deflate(data)
    require 'zlib'
    Zlib::Deflate.deflate data
  end
...
end
```

```
$ irb
>> Zlib
NameError: uninitialized constant Zlib
...

>> Gem.deflate("")
=> "x\x9C\x03\x00\x00\x00\x00\x01"

>> Zlib
=> Zlib
```

and in this manner, the `SortedSet` of the standard library needs a third party :
`RBTree`.
