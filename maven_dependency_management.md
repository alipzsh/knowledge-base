# maven dependency management

uses [transitive dependencies](101/README.md):

A
  ├── B
  │   └── C
  │       └── D 2.0
  ├── E
  │   └── D 1.0
  │
  └── D 2.0

E is chosen, because it's shorter, unless, D is explicitly added.

having projects that inherit from a common parent. we'll have a common POM, then each
project will have it's own POM.

```xml
  < !-- group or organization that created the dependency -->
  <groupId>group-a</groupId>
  < !-- name of the dependency -->
  <artifactId>artifact-a</artifactId>
```
