# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.1] - 2025-01-09

### Fixed

- Fixed a bug that [prevented showing and saving certain animations](https://github.com/LuCEresearchlab/pytamaro/issues/42) 

## [1.1.0] - 2024-11-28

### Changed

- Improved debug visualization, now showing the nine points on the bounding box for `pin` mimicking the style of vector graphics programs

## [1.0.2] - 2024-11-15

### Fixed

- Fixed setuptool configuration, the previous version was not importable

## [1.0.1] - 2024-11-15

### Changed

- Housekeeping: update `__version__` string and move to `uv` as a project/package manager

## [1.0.0] - 2024-11-14

PyTamaro is now mature enough for a 1.X release!

### Changed

- The library is now compatible with Python 3.13 and requires at least Python 3.10
- English names are no longer importable from modules dedicated to other languages (e.g., `pytamaro.it`)

## [0.7.3] - 2024-08-14

### Changed

- Instead of workarounds, [perform antialias using SSAA (4x) to avoid seams and stroke-related artifacts when circular shapes are at the edges](https://github.com/LuCEresearchlab/pytamaro/commit/4244cc44b4011aadaa6ff7fbb42b0f0265e516fc) 

## [0.7.2] - 2024-07-31

### Changed

- Names of parameters and types in error messages are now reported inside backticks to make them more distinguishable from the rest of the message 
- Raise an error when trying to show an animation whose frames are not all of type `Graphic`
- Rendered text now includes leading and trailing glyphs without outline (such as spaces)

### Fixed

- Avoid crashing when showing graphics with a zero area after rounding
- Avoid crashing when showing animations with zero area frames
- [Reduce visible seams when rendering adjacent shapes with antialiasing](https://github.com/LuCEresearchlab/pytamaro/issues/34)

## [0.7.1] - 2024-06-21

### Changed

- [Check the type of optional parameters for output functions](https://github.com/LuCEresearchlab/pytamaro/issues/35)

### Fixed

- Fixed some inconsistent names for localized parameters in the documentation

## [0.7.0] - 2024-06-03

### Added

- [Enable antialiasing](https://github.com/LuCEresearchlab/pytamaro/issues/29) for better rendering

### Changed

- [Faster rendering of images](https://github.com/LuCEresearchlab/pytamaro/pull/33), especially noticeable for GIFs with several frames

### Fixed

- [Fix GIFs overlaying frames within a loop](https://github.com/LuCEresearchlab/pytamaro/commit/57850c696f9323a1ac71a041ebdad174692b5f7f), which was visibile in certain cases with transparency

## [0.6.3] - 2024-02-18

### Changed

- Round the size of graphics used as GIF frames (mainly to accommodate rounding errors) 
- Raise an error when graphics of different sizes are used as GIF frames
- Proper `Point`'s `repr` for unknown points 

## [0.6.2] - 2024-02-15

### Fixed

- Support Python 3.12 for real (upgrade `skia-python` to v121)
- Fix SVG output of (semi-)transparent black color ([#24](https://github.com/LuCEresearchlab/pytamaro/issues/24)) 

## [0.6.1] - 2023-12-05

### Added

- Support Python 3.12 (skia-python upgrade)

### Changed

- Produce a warning message when a font that is not available is used to produce a graphic with `text`

### Fixed

- Do not show subclasses of `Graphic` in error messages

## [0.6.0] - 2023-11-20 

### Added

- French version of the library (importable from `pytamaro.fr`): full translation of the API and the documentation (#25 by @karma-riuk)
- Graphics (as well as points and colors) now have a `__repr__` method which returns a more useful, localized string representation

## [0.5.2] - 2023-08-01

### Fixed

- Fix SVG files' transparent background rendered as black in edge cases
- Fix the pinning position for a `circular_sector` of 360 degrees
- Attempt to prevent a rare condition in which saving an SVG file could fail

## [0.5.1] - 2023-06-03

### Changed

- Data URIs (used in one of the output modes) are now wrapped in special markers so that they can be recognized within a larger output.

### Fixed

- Fix rendering of reasonably big graphics (by increasing the recursion limit)

## [0.5.0] - 2023-05-29

### Added

- New function `show_animation` to show an animation (without having to explicitly save it to a file) in an appropriate viewer (e.g., a Jupyter notebook, Safari on macOS, ...). Multi-OS support is still experimental.

### Changed

- The function `save_gif` has been renamed to `save_animation` to decouple the concept (an animation) from the format (GIF). There is now a nice symmetry between `show_graphic`, `save_graphic`, `show_animation` and `save_animation`.
- SVG files are now saved with an extra attribute (`shape-rendering="crispEdges"`) to achieve a better rendering for our use case and avoid the occasional tiny gaps between adjacent shapes. 

## [0.4.1] - 2023-04-06

### Fixed

- Improve Jupyter notebook detection to include Google Colab

## [0.4.0] - 2023-02-27

This version introduces a number of API breaking changes. [The documentation of the old version is still available under the `version_2022` tag.](https://pytamaro.readthedocs.io/en/version_2022/).

### Changed

- Functions' parameters (their types and values) are now explicitly checked at runtime to provide less confusing error messages when the supplied values are not valid
- `pin` now takes a parameter of type `Point` to specify the pinning position, instead of two strings; the usual nine notable points on the bounding box are available as constants (e.g., `top_left`, `center`, `bottom_right`
- The initial pinning position for certain primitive graphics is no longer at the center of the bounding box, but at a custom documented point of interest (e.g., the centroid for triangles, or the leftmost point on the baseline for text)
- `triangle` can now create arbitrary triangles, not just equilateral ones, by specifying two sides and the angle between them
- `circular_sector` now allows only for degrees in the range [0, 360] (where 360 effectively produces a full circle)
- Counterclockwise rotation is consistently used throughout the library (e.g., for rotation, `circular_sector`, `triangle`)
- `save_graphic` now allows saving a graphic using the SVG format; both `save_graphic` and `save_gif` now require the extension of the desired file to be specified as part of the filename 
- `beside`, `above` and `overlay` now pin the resulting graphic at its center (this makes them truly associative, and allows to explain their behavior without the need to explain the pinning position in the beginning)
- Showing or saving as a PNG a graphic with no area now produces a warning
- Equality of graphics is now based on the equality of their scene graphs and their pinning positions, instead of the rendered bitmaps

## [0.3.1] - 2023-01-13

### Added

- `show_graphic` prints a data URI representation of the graphic when the environment variable `PYTAMARO_OUTPUT_DATA_URI` is set

## [0.3.0] - 2022-11-30

### Added

- New `hsl_color` and `hsv_color` functions to specify colors using HSL / HSV

### Changed

- `rgb_color` (and the newly added functions) now takes an optional `opacity` parameter (which defaults to a fully-opaque color)
- Improved the documentation of colors

### Removed

- `rgba_color` is now superseeded by `rgb_color` with the `opacity` parameter

## [0.2.4] - 2022-10-31

### Added

- Add `py.typed` to comply with PEP 561

## [0.2.3] - 2022-10-27

### Fixed

- Fixed the coding style (due to a bad previous release)  

## [0.2.2] - 2022-10-27

### Fixed

- Fixed a bug that was causing the pinning position to be shown in the wrong place (in debug mode)

## [0.2.1] - 2022-10-26

### Fixed

- Upgraded to `pillow` 9.2.0 fixing an issue with transparent GIFs

## [0.2.0] - 2022-08-16

### Added

- New `loop` parameter for `save_gif`

### Fixed

- Show localized types in the documentation

## [0.1.1] - 2022-03-04

### Changed

- Graphics are now represented as a scene graph, based on `skia-python`

### Fixed

- Support glyphs without outline (e.g., the space character) in `text`

## [0.1.0] - 2022-01-28

### Added

- Initial Version based on `pillow`
