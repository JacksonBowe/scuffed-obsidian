## Engine Testing

Testing suite via PyTest

## GameSave

## GameState

The GameState needs a system for recording events

Mafioso attempting to kill should play shots sound, if kill is a success prints text

Unless there's a bodyguard or a vet, in which case it plays those sounds?

Does actor append to events or do roles append to events

Seems like it must come from the actor because that's where all the logic is

## Roles

### <font color="greenYellow">Town</font>

#### Citizen

* [x] Find Allies

* [x] Find Possible Targets

* [ ] Night action

  - \[x\] Goes night immune

  - \[x\] self.remaining_vests goes down by 1

  - \[ \] Events should contain log "You don your bullet proof vest, you have {x} remaining"

#### Doctor

* [x] Find Allies

* [x] Find Possible Targets

* [ ] Night action

  - \[x\] Successful heal?

  - \[ \] Events should contain log of what happened

#### Detective

* [ ] Find allies

* [ ] Find Possible Targets

* [ ] Night Action

  - \[ \] At targets house?

  - \[ \] Successfull track?

### <font color="red">Mafia</font>

#### Mafioso

* [x] Find Allies

* [x] Find Possible Targets

* [x] Basic kill (target not protected/healed/etc)

  - \[x\] At targets house?

* [ ] Target Night Immune

  - \[x\] Target should be alive

  - \[ \] Events should contain log "Target is Night Immune"

### <font color="yellow">Neutral</font>

### <font color="violet">Cult</font>

### <font color="deepSkyBlue">Triad</font>
