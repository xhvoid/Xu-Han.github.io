---
permalink: /projects/
title: "Research & engineering projects"
excerpt: "Adaptive optics, experimental apparatus development and weak-lensing research, with supporting optical simulation studies."
author_profile: true
---

Three projects bring together my work in optical modelling, experimental engineering and astronomical research. They span numerical validation, the development of a physical measurement apparatus and quantitative analysis of astronomical data.

{% include portfolio-styles.html %}

<nav class="portfolio-jump" aria-label="Project sections">
  <a href="#adaptive-optics">Adaptive optics</a>
  <a href="#experimental-apparatus">Experimental apparatus</a>
  <a href="#weak-lensing">Weak lensing</a>
  <a href="#additional-independent-projects">Further projects</a>
</nav>

<a id="adaptive-optics"></a>
<a id="adaptive-optics--basics"></a>

## Shack-Hartmann AO Simulation

<p class="project-role">Independent optical modelling project</p>

I developed a modular Python model of single-conjugate adaptive optics (SCAO), following the measurement chain from atmospheric wavefront disturbances to detector images, calibrated reconstruction, mirror commands and astronomical image quality.

- **Sensing and calibration:** Shack-Hartmann propagation, detector sampling, photon/read noise, reference centroids and interaction matrices.
- **Reconstruction and control:** Regularised inverse problems, gain and latency studies, deformable-mirror limits and explicit treatment of invalid measurements.
- **Performance and verification:** Residual wavefront error, Strehl ratio, FWHM and encircled energy; analytic references, numerical convergence checks and comparisons with independently implemented HCIPy optics.

Executed notebooks and recorded configurations make the experiments reviewable. The work connects optical assumptions to measurable quantities and shows how calibration, noise and control choices affect the resulting images.

[Repository](https://github.com/xhvoid/Shack-Hartmann-AO-Simulation) · [Executed tutorials](https://github.com/xhvoid/Shack-Hartmann-AO-Simulation/tree/main/notebooks/tutorials) · [Validation evidence](https://github.com/xhvoid/Shack-Hartmann-AO-Simulation#validation-evidence)

<details class="project-evidence">
  <summary>View a closed-loop demonstration</summary>
  <figure>
    <img src="https://raw.githubusercontent.com/xhvoid/Shack-Hartmann-AO-Simulation/main/figures/canonical_closed_loop_control.png" alt="Matched open-loop and corrected wavefront RMS in a simulated adaptive-optics control experiment" loading="lazy" decoding="async">
    <figcaption>A short, noiseless 1 m SCAO example at 500 Hz: 12 simulated frames, gain 0.5 and zero frame delay. Open and corrected wavefronts follow the same atmospheric trajectory. The executed tutorial records the configuration and measurement definitions.</figcaption>
  </figure>
</details>

My related [Adaptive Optics — Basics](https://github.com/xhvoid/Adaptive-Optics---Basics) project provides seven fundamentals notebooks with analytic checks, including an exploratory Fourier-optics pyramid-sensor study.

<a id="experimental-apparatus"></a>

## Experimental Collisional Charging Apparatus

<p class="project-role">B.Sc. Physics thesis · University of Duisburg-Essen · March–August 2021</p>

**Thesis:** *Design of an Experimental Setup for the Measurement of Collisional Charging on Granulate.*

I designed and built an apparatus to investigate charging in granular materials. The experiment tested a hypothesis concerning dust growth through collisions during the early stages of planet formation.

- Designed the mechanical components in CAD and fabricated prototype parts by 3D printing.
- Assembled the apparatus and integrated and debugged its electronic charge-measurement modules.
- Conducted experiments, analysed the grain-size dependence of charging and interpreted the measurements in relation to the physical hypothesis.

This work covered the complete experimental process: defining a measurement, developing and assembling an apparatus, obtaining data and testing a physical model.

**Supervisors:** Prof. Gerhard Wurm and Dr. Felix Jungmann.

<a id="weak-lensing"></a>
<a id="2d-voids"></a>

## Weak Lensing Void Finder

<p class="project-role">M.Sc. Astrophysics thesis · LMU Munich · March 2023–August 2024</p>

**Thesis:** *Watershed Cosmic Void Finder for Weak Gravitational Lensing Voids on 2D Full-Sky Convergence Maps.*

I developed a watershed algorithm for detecting cosmic voids in full-sky convergence maps and worked with Dark Energy Survey Year 3 (DES Y3) weak-lensing maps.

- Implemented void detection and studied the influence of algorithm parameters on the recovered populations.
- Characterised void abundance, effective radii, ellipticities and convergence profiles.
- Connected map-based algorithm development with the quantitative interpretation of astronomical measurements.

This research developed my experience with scientific computing, statistical reasoning and the relation between analysis choices and physical conclusions.

**Supervisors:** Prof. Joseph Mohr and Dr. Chris Davies.

[Thesis (PDF)]({{ '/files/Watershed_Voids%EF%BC%88thesis%EF%BC%89.pdf' | relative_url }}) · [2D-Voids repository](https://github.com/xhvoid/2D-Voids)

## Additional independent projects

These studies extend my interests into fibre-fed spectroscopy, IFU measurements and optoelectronic signal chains.

<a id="astrophotonics"></a>

### Astrophotonics

A conceptual Python study linking residual AO wavefront error, injection jitter and photonic-lantern mode count to fibre coupling, spectral signal-to-noise ratio and radial-velocity precision. It connects complex-field propagation and modal overlap to a synthetic spectroscopic measurement.

**Methods:** Wave optics, coherent modal coupling, noise budgets and parameter studies.

[Repository](https://github.com/xhvoid/Astrophotonics) · [Executed notebook](https://github.com/xhvoid/Astrophotonics/blob/main/notebooks/eso_astrophotonics_showcase.ipynb)

<a id="ifu-spectrograph"></a>

### AO-Fed IFU Spectrograph Simulation

An end-to-end numerical study carrying a synthetic datacube through AO PSF coupling, an image-slicer IFU, a spectrograph, detector response, calibration and cube reconstruction. Recovered flux, velocity and signal-to-noise are compared with the known input, making measurement biases and calibration sensitivity visible.

**Methods:** Fourier PSFs, spatial and spectral sampling, detector noise, reconstruction and comparison with synthetic truth.

[Repository](https://github.com/xhvoid/AO-Fed-IFU-Spectrograph-Simulation)

<a id="optoelectronics"></a>

### Optoelectronic Signal Chain Simulations

Python case studies of photodetector/APD noise, laser thermal control, LiDAR detection, camera sensors and spectrometer calibration. Parameter scans examine how component behaviour, noise and uncertainty affect a measurement.

**Methods:** Noise analysis, feedback control, calibration and engineering trade-offs.

[Repository](https://github.com/xhvoid/Optoelectronic-Signal-Chain-Simulations)

[Education and laboratory experience]({{ '/experience/' | relative_url }}) · [CV]({{ '/cv/' | relative_url }})
