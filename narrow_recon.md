05 05-06
# phase zero

- work with the website like a *normal* user
- create a mind map of functionalities (don't get into the rabbit hole of testing
  without first browsing the website) that you are going to use later on to test your
  check list.
- accessing the paid plans will give you considerable opportunity

# answer these questions

## what is the application used for

- it's overall business logic
- the failure of confidentiality; understand what is important for the team (something
  dangerous else where else might not be important here, e.g. email address leak)
- the failure of integrity; the integrity of the stuff that are important for the team.

## does the application have a special threat model

EX:

- getting 50% off in a internet taxi app.
- adding users more than limit on a invite only application.

## how does the application pass data

you should be able to know how the data is being transmitted and the
differences between them (e.g. capcut; [react](react) REST API)


- UI + back-end
- simple web app + jQuery
- single page web application + rest API / graphQL
- web-socket communication
- a combination of some of the above

## how are users handled

- what are the authentication schemes
- cookies, JWT, toke, ...
- 2FA implementation
- account delegations (giving your account to others)
- are there other users levels
- is there any authentication transfer

## previous security vulnerabilities

Apps could have specific weaknesses --> look into public reports

## is it using third parties

- why is it being used? Saving data?
- if the third party has it's own bug bounty, skip it, it's a whole other program.
- if the third party is not well known, work on it too.

## read API documentation

If available, read, implement.
It's hard but gives you much deeper insight.

# eye catchings to work on

First work on these

- authentication class
  - oauth (all providers)
  - linking accounts
- switching between applications (desktop, mobile, web, sending you
  between them.)
- uploader sections
- links or HTML inputs
- application specific sections
- sensitive APIs
- deep links

# increase the attack surface

- side applications: mobile, pc
- hidden surfaces:
  - hidden parameters, path, files, etc.
  - paid, forgotten, custom features
  - stage instances (application-dev), might be out of scope but gives you insight on future
    features.
- [passive crawling](passive crawling) (all the time)
  - something interesting? find and read the JS.
  - also use dev tools networking to monitor stuff.
- active crawling (less useful)

# [fuzz](fuzz)
