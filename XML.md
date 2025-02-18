# XML
# What is XML

XML or "extensible markup language" is designed for storing and transporting data. it uses a
tree like structure of tags and tags are not predefined and can be given arbitrary names.

*XML entities* are a way of representing an item of data within an XML document instead of
using the data itself; like `&lt;` and `&gt;` that stand for `<` and `>`.

*document type definition (DTD)* defines the structure and the legal elements and attributes
of an XML document. Defined in `DOCTYPE`. can be loaded "external DTD" or contained within
the document "internal DTD" or can be hybrid.

XML custom entities: any usage of the entity reference `&myentity;` will be replace by `my
entity value`.

```xml
<!DOCTYPE foo [ <!ENTITY myentity "my entity value" > ]>
```

XML external entities: custom entities defined outside of DTD.

```xml
<!DOCTYPE foo [ <!ENTITY ext SYSTEM "<http or file>://normal-website.com" > ]>
```
