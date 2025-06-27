# phase zero

- work with the website like a *normal* user
- build a mindmap for the app
- don't get into the rabbit hole of testing without browsing the webstie
- figure as much functionality as possible.
- it's huge opportunity to access the paid plans

# answer these questions

## what is the application used for

- overall business logic
- the failure of confidentiality; understand what is important for the
  aplication/ team (something dangerous else where else might not be
  important here, e.g. email address leak)
- the failure of integrity the integrity of which stuff is important for
  the team.

## does the application have a special threat model

e.g.
- getting 50% off in a internet taxi app.
- changing stuff without permission.
- adding users more than limit on a invite only application.

## how does the application pass data

- UI + backend
- simple web app + jQuery
- single page web application + rest API / graphQL
- web-socket communication
- a comination of some of the above

## how are users handled

- what are authentication shcemes
- cookies, JWT, toke, ...
- 2FA implementation
- account delegations (giving your account to others)
- are there other users levels
- is there any authentication transfer

## previous security vulnearbilities

apps could have specific weaknesses
look into public reports

## is it using third parties

- why is it being used? saving data?
- if the third party has it's own bugbounty, skip it, it's a whole other
  program.
- if the third party is not well known, wrok on it too.

## read API documentation

if available, read, implement.
it's hard but could work out.

## eye catchings to work on

first work on these

- authentication class
  - oauth (all providers)
  - linking accounts
- switching between applications (desktop, mobile, web, sending you
  between them.)
- uploader sections
- links or HTML inputs
- application specific sections
- sensitive APIs

# increase the attack surface

# fuzz


[[narrow_recon_handson]]
