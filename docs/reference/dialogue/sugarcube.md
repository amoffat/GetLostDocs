# ⬜ SugarCube

For [dialogue written with Twine](../tutorials/dialogue/creating-dialogue.md), Get Lost supports a very limited subset of the [`SugarCube`](https://www.motoslave.net/sugarcube/2/docs/) story format.(1)
{ .annotate }

1. A story format is what Twine calls a text templating language. There are several story formats that it supports, but Get Lost only supports SugarCube.

!!! note

    The subset of supported functionality is always expanding. If you want request something specific, make a request in the [Discord.](https://discord.gg/v4AAezkSEu)

## 🔀 Flow control

We support basic if/elseif/else flow control.

```
<<if visited() > 1>>
    Welcome back
<<elseif visited() > 2>>
    You again??
<<else>>
    Hello
<</if>>
```

Flow control can also be nested for complex branching.

## 🔡 Variables

A variable can be set in _any_ passage, like this:

`<<set $answer to 42>>`

This sets the variable named `$answer` to the number `42`. You can then access that variable in another passage, for example:

```
<<if $answer == 42>>
    The answer is 42.
<</if>>
```

The way this is typically used is to have some dialogue tree that eventually sets a variable if you make the right choices. Then you can access that variable in your level code or in later dialogue to advance the story.

### Level access

Your level code can access variables by using the `dialogue` namespace. On `dialogue` exists a `state` attribute, and on that object exists all of the variable names that you've set.

!!! example

    Suppose your level has a secure door that requires a password. You talk to an employee while they're on their break and you're able to finesse the password from them. The passage where the employee reveals the password would also have this:

    ```
    <<set $gotPassword to true>>
    ```

    Then, in your level code, when you interact with the door, you can check to see if you got the password before deciding to let the player in or not:

    ```typescript
    if (dialogue.state.gotPassword) {
        // open the door
    } else {
        // deny access
    }
    ```

### Initial value

For variables that you want to apply story-wide, you want to set an initial value to your variable. This is what the special `StoryInit` passage is for. Set initial values there and every passage will see that initial value.

```
<<set $gotPassword to false>>
```

## 🧰 Builtin functions

These functions are defined in `.internal/assemblyscript/@gl/utils/twine.ts`. You can use them freely throughout your dialogue as either as an expression or as a function call.

### `visited()`

Returns the number of times that the player has visited a passage. If no arguments are passed, it assumes the current passage.

```
<<if visited() > 3>>
    How many times do I have to tell you?
<</if>>
```

!!! warning

    It is counter-intuitive, but `visited()` will always return 1, not 0, the first time you visit the passage.

### `hasVisited()`

Returns a boolean if the player has visited a passage. If no arguments are passed, it assumes the current passage.

### `isNight()`

Returns a boolean of whether or not the player's current time of day is night.

### `isDay()`

Returns a boolean of whether or not the player's current time of day is day.

### `hasPickup(tags)`

Returns true if the player possesses a pickup that matches the provided tags, false otherwise. Use this to change the dialogue based on a particular item, for example:

```
<<if hasPickup({type: "map"})>>
    You have the map! Let me see it!
    [[Ok, here.]]
    [[What do you want with it?]]
<<else>>
    Let me know when you find the map.
<</if>>
```

### `random(min, max)`

Returns a random integer between min and max, inclusive.

### `randomFloat(min, max)`

Returns a random float between min and max, inclusive.

### `exit(exitName, force=false)`

Exits the map, using the exit `exitName`. If `force` is false, the player will be given the option to exit. If `force` is true, they will not.

## 🎒 Level functions

Your SugarCube code can also call functions defined in your level's `main.ts` file. To call these functions, just prefix your call with `level`. For example:

```
<<if level.isCorrect($answer)>>
    You guessed correctly.
<</if>>
```

And in your `main.ts` file, define `isCorrect`:

```typescript
export function isCorrect(num: i32): bool {
  return num === 42;
}
```

## Widgets

!!! warning

    Widgets are an advanced topic, and might have some rough edges.

Widgets let you define some passage markup that you can re-use as often as you want. It's useful for things like player choices that you want to appear in multiple passages and stay in sync.

TODO finish this.
