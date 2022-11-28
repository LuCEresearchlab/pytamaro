# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- New `hsl_color` and `hsv_color` functions to specify colors using HSL / HSV

### Changed

- `rgb_color` (and the newly added functions) now takes an optional `alpha` parameter (which defaults to a fully-opaque color)

### Removed

- `rgba_color` is now superseeded by `rgb_color` with the `alpha` parameter

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
