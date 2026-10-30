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

## Shack-Hartmann Wavefront Sensing & Adaptive Optics Simulation

<p class="project-role">Independent project · March 2026–present · Ongoing development</p>

I developed a modular Python model of single-conjugate adaptive optics (SCAO), following the measurement chain from atmospheric wavefront disturbances to detector images, calibrated reconstruction, mirror commands and astronomical image quality.

- **Sensing and calibration:** Shack-Hartmann propagation, detector sampling, photon/read noise, reference centroids and interaction matrices.
- **Reconstruction and control:** Regularised inverse problems, gain and latency studies, deformable-mirror limits and explicit treatment of invalid measurements.
- **Performance and verification:** Residual wavefront error, Strehl ratio, FWHM and encircled energy; analytic references, numerical convergence checks and comparisons with independently implemented HCIPy optics.

The interactive explorer presents **precomputed results and recorded AO experiments**; it performs no online simulation. Executed notebooks and saved configurations provide the methods and evidence behind the displays.

<nav class="portfolio-jump" aria-label="AO project links">
  <a href="https://xhvoid.github.io/Shack-Hartmann-AO-Simulation/">Interactive explorer</a>
  <a href="https://github.com/xhvoid/Shack-Hartmann-AO-Simulation">Source code</a>
  <a href="https://xhvoid.github.io/Shack-Hartmann-AO-Simulation/#ngs22">Loss-of-lock case study</a>
</nav>

### Selected case study — diagnosing a closed-loop reconstruction failure

In a simulated 2.2 m natural-guide-star AO system, I investigated a reconstruction failure associated with measurement dropout and weakly constrained inverse modes. Stronger TSVD regularisation maintained usable reconstruction throughout a matched two-second atmospheric trajectory. The original and revised runs, diagnostic evidence and model limitations are available in the interactive explorer.

<figure class="project-case-figure">
  <a href="https://xhvoid.github.io/Shack-Hartmann-AO-Simulation/#ngs22">
    <img src="{{ '/images/projects/ngs-22m-comparison.png' | relative_url }}" alt="Recorded synthetic AO results: the original 2.2 m run loses usable reconstruction near one second, while stronger TSVD regularisation maintains reconstruction through the matched two-second trajectory; H-band Strehl, usable measurement rows and DM limits are shown" width="1760" height="1520" loading="lazy" decoding="async">
  </a>
  <figcaption>Recorded simulation results, reproduced unchanged from the project analysis. The 2.2 m v1/v2 runs share the same atmosphere and calibration; the separate 2 m reference ends at one second and is not a paired comparison. Select the figure to inspect the case.</figcaption>
</figure>

This is a **synthetic model study**, not measured Robo-AO-2 performance. The paired result supports improvement for this input and time window. The added recovery safeguard did not activate, so the demonstrated improvement supports the stronger regularisation rather than automatic recovery; the initial noise trigger was not uniquely identified.

[Methods and validation evidence](https://github.com/xhvoid/Shack-Hartmann-AO-Simulation#validation-evidence) · [Case configurations, diagnosis and limitations](https://github.com/xhvoid/Shack-Hartmann-AO-Simulation/tree/main/web/ao-explorer/derived/ngs-22m-53663e0742d1d106)

<section class="project-evidence" aria-labelledby="ao-explorer-preview">
  <h3 id="ao-explorer-preview">AO correction in motion</h3>
  <div class="ao-preview-layout">
    <figure class="ao-preview-media">
      <input type="checkbox" id="ao-preview-still" class="ao-preview-toggle">
      <label for="ao-preview-still">Show still image</label>
      <div class="ao-preview-images">
        <picture class="ao-preview-animation">
          <source media="(prefers-reduced-motion: reduce)" srcset="{{ '/images/projects/ao-galaxy-comparison-poster.png' | relative_url }}">
          <img src="{{ '/images/projects/ao-galaxy-comparison.gif' | relative_url }}" alt="Animated comparison of NGC 1705 with uncorrected and AO-corrected simulated PSFs, with synchronized instantaneous PSF Strehl values at 1.65 micrometres, original frame numbers and simulated time" width="600" height="480" loading="lazy" decoding="async">
        </picture>
        <img class="ao-preview-poster" src="{{ '/images/projects/ao-galaxy-comparison-poster.png' | relative_url }}" alt="Still comparison at simulated time 0.200 seconds, with the corresponding uncorrected and AO-corrected PSF Strehl values" width="600" height="480" loading="lazy" decoding="async">
      </div>
      <figcaption>A recorded 2 m model: the same HST/F814W template through uncorrected and AO-corrected simulated PSFs, on one fixed brightness scale. Strehl readouts describe the corresponding 1.65 μm PSFs. One simulated second is replayed over 20 seconds; the loop repeats the same 126 recorded samples.</figcaption>
    </figure>
    <div class="ao-preview-more">
      <h4>Explore the full experiment</h4>
      <p>Replay the wavefronts and images, compare recorded cases, and inspect performance curves, methods and model limitations in the interactive explorer.</p>
      <div class="portfolio-actions">
        <a class="btn btn--primary" href="https://xhvoid.github.io/Shack-Hartmann-AO-Simulation/#galaxy-panel">Open AO Explorer</a>
      </div>
      <p class="ao-preview-credit">Template: HST/WFC3 F814W, LEGUS (GO-13364), via MAST. This mock observation retains the template’s resolution and residual noise; no additional image noise is added.</p>
    </div>
  </div>
</section>

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

These studies extend my interests into fibre-fed spectroscopy and optoelectronic signal chains.

<a id="astrophotonics"></a>

### Astrophotonics

A conceptual Python study linking residual AO wavefront error, injection jitter and photonic-lantern mode count to fibre coupling, spectral signal-to-noise ratio and radial-velocity precision. It connects complex-field propagation and modal overlap to a synthetic spectroscopic measurement.

**Methods:** Wave optics, coherent modal coupling, noise budgets and parameter studies.

[Repository](https://github.com/xhvoid/Astrophotonics) · [Executed notebook](https://github.com/xhvoid/Astrophotonics/blob/main/notebooks/eso_astrophotonics_showcase.ipynb)

<a id="optoelectronics"></a>

### Optoelectronic Signal Chain Simulations

Python case studies of photodetector/APD noise, laser thermal control, LiDAR detection, camera sensors and spectrometer calibration. Parameter scans examine how component behaviour, noise and uncertainty affect a measurement.

**Methods:** Noise analysis, feedback control, calibration and engineering trade-offs.

[Repository](https://github.com/xhvoid/Optoelectronic-Signal-Chain-Simulations)

[Education and laboratory experience]({{ '/experience/' | relative_url }}) · [CV]({{ '/cv/' | relative_url }})
