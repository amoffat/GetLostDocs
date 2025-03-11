# 🧅 Special layers

In the Tiled map editor, Get Lost uses special layer names that can have different effects in the engine. For example, if you create a layer named `zooms`, any primitive object (1) will designate a zoom area. When the player walks through this zoom area, the camera will zoom in or out, based on the properties you've assigned to the primitive object.
{ .annotate }

1. A primitive object is a rectangle or ellipse. Arbitrary polygon objects are not yet supported.

## Special layers

### `bounds`

The `bounds` object layer can only contain one object and it must be a rectangle. This rectangle defines an artificial bounds for the camera that the camera will not leave as the player moves.

!!! note

    Even though the camera will stay inside of the bounds, the player won't. The player can move anywhere where there isn't a collision object.

If you don't define a bounds layer, the bounds of the map's tiles will be used instead. So this is useful if you want a camera bounds that is different than that.

### collisions

The `collisions` layer defines large scale collision objects. You can use any primitive object (including the polygon object) to define a collision object. The objects in this layer will mark an areas that the player or NPC cannot move through. This is useful to block off entire sections of the map, for example, at the map's boundaries, or the edges of bridges.

### divider

The `divider` layer is a somewhat advanced layer. The layer contains should contain no objects. It's purpose is to separate the z-indices of any layers below above the divider from any layers below the divider. This is useful if you have a layer that the player will never walk on, for example, a bridge above the player. Most of the time, you will not need this layer, but when you need it, you'll know.

### player

The `player` layer sets the position (x, y) and the base z-index of the player's avatar. It should contain a single rectangle named `entry`. When your level loads in Get Lost, the player will be placed at the center of this rectangle. Move the rectangle around to where you want the player to start.

Everything below the `player` layer will be permanently below the player on the z-index. This means that the player layer should always sit above the ground layer, because the player will never move underneath the ground. However, everything above the `player` layer will be evaluated for z-index sorting.

### sensors

The `sensors` layer defines objects that trigger a sensor call in your level's code.

### sounds

### zooms

## Layer groups

Layer groups are useful to logically group together layers based on their contents. They have no functional effect on the Get Lost engine, meaning they won't influence the behavior of the game. It's only for your own personal organization. The only thing they do effect in the engine is the authoritative naming of the layers. When Get Lost loads your Tiled map, it uses the layer names as they're given. Except if the layer is in a group. Then it is prefixed with the group name. For example, a layer named "trees1" in the "trees" layer group becomes "trees/trees1".
