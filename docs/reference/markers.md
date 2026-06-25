# 📜 Markers

Markers are how your level can change a player's future interactions. A marker is an event set on the player that you or other levels can check for.

Markers are super simple&mdash;they're just some text attached to the player. Something like `lied-about-stealing` or `FinishedRace<30s`. It can be anything really. Some examples:

- The player picked an extra spicy dialogue option
- The player entered an specific area
- The player completed a puzzle or race

The best kinds of markers are ones that other levels can use to learn something about the player's history, like something that represents an accomplishment, or a personality trait of the player. Other levels can check for these markers and change how the level behaves, for example:

- Adding new dialogue options
- Hiding NPCs from the level

!!! note "Finding markers"

    There is no way to get all of the markers for a player. To learn about the markers that the player could have, you need to [look at the source code](../tutorials/code/learning.md) of other levels to see which markers they set.

## ✍🏻 Recording a marker

Before you can set a marker on the player, you need to tell Get Lost that the names of the markers you want to set. This is so a level can't spam a million markers on a player

### From dialogue

`<< recordMarker(name) >>`

### From level code

`host.markers.record(name)`

## 🕵 Checking a marker

!!! tip

    Name can be a string, like `"lied-about-x"`, or a string version of a [Javascript RegExp](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_expressions), like `"/.*lied.*/"`. The regexp version gives you much more flexibility, but it is more complicated to write.

### From dialogue

```
<<if queryMarker(name)>>
Oh so you're a thief?
<</if>>
```

### From level code

`host.markers.query(name)`
