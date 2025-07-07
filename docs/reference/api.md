# 👨‍💻 API

The api is how your level interacts with the engine to do things like displaying dialogs, triggering sensors, and exiting the level.

!!! warning

    The api is incomplete, weird, and buggy. However, it will solidify over time. Also, the api is pinned, so the engine version that your level is built with will never see a regression.

## Camera

[camera.ts](https://github.com/amoffat/getlost-level-template/blob/main/.internal/assemblyscript/%40gl/api/w2h/camera.ts) controls how the virtual camera behaves.

## Character

[char.ts](https://github.com/amoffat/getlost-level-template/blob/main/.internal/assemblyscript/%40gl/api/w2h/char.ts) has functions related to what the character is currently doing.

## Controls

[controls.ts](https://github.com/amoffat/getlost-level-template/blob/main/.internal/assemblyscript/%40gl/api/w2h/controls.ts) lets you display custom buttons on the screen for the player to click.

## Debug

[debug.ts](https://github.com/amoffat/getlost-level-template/blob/main/.internal/assemblyscript/%40gl/api/w2h/debug.ts) is primarily for logging in the dev environment.

## Filters

[filters.ts](https://github.com/amoffat/getlost-level-template/blob/main/.internal/assemblyscript/%40gl/api/w2h/filters.ts) is for cool stuff like blurs, color grading, and other shader FX.

## Lights

[lights.ts](https://github.com/amoffat/getlost-level-template/blob/main/.internal/assemblyscript/%40gl/api/w2h/lights.ts) will let you control light objects in your map.

## Map

[map.ts](https://github.com/amoffat/getlost-level-template/blob/main/.internal/assemblyscript/%40gl/api/w2h/map.ts) handles various map and exit related functions.

## Markers

[markers.ts](https://github.com/amoffat/getlost-level-template/blob/main/.internal/assemblyscript/%40gl/api/w2h/markers.ts) is for storing and retrieving persistent player decisions (markers).

## NPC

[npc.ts](https://github.com/amoffat/getlost-level-template/blob/main/.internal/assemblyscript/%40gl/api/w2h/npc.ts) controls NPCs.

## Particles

[particles.ts](https://github.com/amoffat/getlost-level-template/blob/main/.internal/assemblyscript/%40gl/api/w2h/particles.ts) can create and update particle systems.

## Physics

[physics.ts](https://github.com/amoffat/getlost-level-template/blob/main/.internal/assemblyscript/%40gl/api/w2h/physics.ts) does all things physics related.

## Pickup

[pickup.ts](https://github.com/amoffat/getlost-level-template/blob/main/.internal/assemblyscript/%40gl/api/w2h/pickup.ts) gives the player a pickup, or lets you check if they have a pickup.

## Player

[player.ts](https://github.com/amoffat/getlost-level-template/blob/main/.internal/assemblyscript/%40gl/api/w2h/player.ts) is primarily for sprite-related player functions.

## Sensors

[sensors.ts](https://github.com/amoffat/getlost-level-template/blob/main/.internal/assemblyscript/%40gl/api/w2h/sensors.ts) handles invisible triggers (sensors)

## Sound

[sound.ts](https://github.com/amoffat/getlost-level-template/blob/main/.internal/assemblyscript/%40gl/api/w2h/sound.ts) for loading, playing, and updating music and sound fx.

## Sprite

[sprite.ts](https://github.com/amoffat/getlost-level-template/blob/main/.internal/assemblyscript/%40gl/api/w2h/sprite.ts) for basic spritesheet manipulation.

## Stdlib

[stdlib.ts](https://github.com/amoffat/getlost-level-template/blob/main/.internal/assemblyscript/%40gl/api/w2h/stdlib.ts) exposes some basic javascript functions, like `Math.random` and `Date.now`

## Text

[text.ts](https://github.com/amoffat/getlost-level-template/blob/main/.internal/assemblyscript/%40gl/api/w2h/text.ts) for displaying dialogue to the player.

## Tiles

[tiles.ts](https://github.com/amoffat/getlost-level-template/blob/main/.internal/assemblyscript/%40gl/api/w2h/tiles.ts) to manipulate individual tiles on the map.

## Time

[time.ts](https://github.com/amoffat/getlost-level-template/blob/main/.internal/assemblyscript/%40gl/api/w2h/time.ts) changes the lighting according to a specific time of day.

## Timer

[timer.ts](https://github.com/amoffat/getlost-level-template/blob/main/.internal/assemblyscript/%40gl/api/w2h/timer.ts) lets you set asynchronous timers that will call code after some amount of time.

## UI

[ui.ts](https://github.com/amoffat/getlost-level-template/blob/main/.internal/assemblyscript/%40gl/api/w2h/ui.ts) is used for displaying UI elements, like progress bars, rating widgets, etc.
