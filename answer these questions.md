# what is the application used for

- it's overall business logic
- the failure of confidentiality: understand what is important for this particular team
  (something dangerous else where else might not be important here, e.g. email address leak)
- the failure of integrity: the integrity of the stuff that are important for the team.

# does the application have a special threat model

EX:
- getting 50% off in a internet taxi app.
- adding users more than limit on an invite only application.

# how does the application pass data

you should be able to know how the data is being transmitted and the
differences between them (e.g. capcut; [react](react) REST API)

you should know how the application is working, the architecture of the website,e.g.
programming language, JS framework. which then gives us more info of how the website is
working, whether it has REST API or old school filenames e.g. `pixiv.net/upload.php`.

- UI + back-end
- simple web app + jQuery
- single page web application + rest API / graphQL
- web-socket communication
- a combination of some of the above

e.g
`https://www.capcut.com/forget-password?aid=348188&code=623778¤t_page=&email=fyoumgk%40gmail.com&enter_from=&language=en&type=4&showType=password`

is a client side link that sends an http request to the server -> any change
should happen on the server not the client.

## [parameters handling](parameters handling)

# how are users handled

- what are the authentication schemes
- cookies, JWT, token, ...
- 2FA implementation
- account delegations (giving your account to others)
- are there other users levels
- is there any authentication transfer

# previous security vulnerabilities

Apps could be particularly weak in specific areas --> look into public reports

# is it using third parties

- why is it being used? Saving data?
- if the third party has it's own bug bounty, skip it, it's a whole other program.
- if the third party is not well known, work on it too.

# read API documentation

If available, read, implement.
It won't be easy but gives you much deeper insight.
