---
permalink: /projects/
title: "Selected projects"
excerpt: "Independent projects in adaptive optics, astrophotonics, astronomical instrumentation and cosmology."
author_profile: true
---

My projects use scientific computing to explore how physical assumptions, optical performance and measurement noise affect astronomical and optoelectronic systems. I document the models, their scope and validation so that the analyses can be understood and reproduced.

## Adaptive Optics — Basics

A Python model of a single-conjugate adaptive-optics system, covering atmospheric turbulence, Shack–Hartmann wavefront sensing, reconstruction, closed-loop control and near-infrared imaging.

Tutorial notebooks connect each part of the simulation to analytic checks. The project explores phase-screen statistics, reconstruction regularisation, detector centroiding, control-loop delay and image quality.

**Methods:** NumPy/SciPy, Fourier optics, wavefront reconstruction, feedback control and validation against theory.

[View repository](https://github.com/xhvoid/Adaptive-Optics---Basics)

## Astrophotonics

A simulator linking adaptive-optics wavefront error, injection jitter and photonic-lantern mode count to fibre coupling, spectral signal-to-noise ratio and radial-velocity precision.

The project studies how better optical coupling trades against additional detector noise, connecting complex-field propagation and modal overlap to a synthetic spectroscopic measurement.

**Methods:** Wave optics, coherent modal coupling, noise budgets, parameter sweeps and statistical performance estimates.

This is an independent conceptual study inspired by astronomical instrumentation.

[View repository](https://github.com/xhvoid/Astrophotonics)

## AO-Fed IFU Spectrograph Simulation

An end-to-end Python model connecting adaptive-optics point-spread functions, image-slicer mapping, detector noise and datacube reconstruction.

The project follows the measurement chain from an optical image to reconstructed spatial and spectral data, supporting the study of throughput and reconstruction behaviour.

**Methods:** PSF modelling, instrument simulation, detector noise and scientific data reconstruction.

[View repository](https://github.com/xhvoid/AO-Fed-IFU-Spectrograph-Simulation)

## Optoelectronic Signal Chain Simulations

A collection of studies covering photodetectors, laser thermal control, LiDAR detection, camera sensors and spectrometer calibration.

The simulations examine how component behaviour and noise propagate through a measurement chain.

**Methods:** Signal-chain modelling, noise analysis, calibration and performance trade-offs.

[View repository](https://github.com/xhvoid/Optoelectronic-Signal-Chain-Simulations)

## 2D-Voids

A watershed cosmic-void finder for weak-lensing convergence maps. The code includes two methods for calculating void profiles, together with effective-radius and ellipticity calculations.

This project reflects my earlier work in cosmology and map-based scientific analysis.

**Methods:** Watershed segmentation, weak-lensing map analysis, FITS inputs and NumPy outputs.

[View repository](https://github.com/xhvoid/2D-Voids)

[More repositories on GitHub](https://github.com/xhvoid?tab=repositories)
