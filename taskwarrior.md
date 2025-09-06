https://github.com/pjf/talks/tree/af3be3b80e21ea410103c46ac835450e12405f8a/taskwarrior

it can make a calendar

# tags

- add tags: `task add {task} +{tag}`
- modify latest tag: `task +LATEST modify -{tag} +{tag}`
- get all tasks with a certain tag: `task +{tag}`
- tasks with due date will have automatic tags
- tasks without some tags
  `task -SCHEDULE | -PROJECT | -UNTIL`

# projects

- `task add {task} project:{project},{sub project},{sub sub project}`
- `task projects` all projects
- `task project:{project}` specific project
- `task project.not:{project}`

# context

having separate context related stuff all in one place

- `task context define {context}`

  e.g:

  ```
  task context define work project:work
  task context define personal project.not:work project.not:fun -fun
  task context define fun project:fun or +fun
  ```

- `task context {context}` to switch contexts
- `context list` all contexts
- `context show`
- `context none` clear current context

# annotation

- `task {id} done {description about it}`

# wait

hide until a date

- `task add {task} wait:{date}`
- `task waiting` see waiting tasks
- `task {id} modify wait:tomorrow` relative timing to put the task for tomorrow
- `task {id} modify wait:+5d`

# schedule

add deadline
task wont be shown on `task ready`

- `task add {task} wait:{date} schedule:{date}` add to the list on wait, deadline on
  schedule

# until

if task not done by schedule, wait unto until, then remove it.

# relative date

-
  ```
  task add {task} \
    due:{date} \
    wait:"due - 6d" \
    schedule:"due - 3d" \
    until:"due + 3d" \
  ```

- relative to other tasks
  ```
  task add {task} \
    schedule: "8.due - 30" \
    until: "8.due"
  ```

# search

- `task /{something in the title}/ ids`

# priority

- `task {id} modify prio:H|M|L`

# urgency

you can change how it calculates the urgency in ~/.taskrc

`urgency.inherit=on`

# dependency

- `... \
  depends: {id}
  `
# hooks


perhaps would be useful with this? https://timewarrior.net/reference/timew-durations.7/
